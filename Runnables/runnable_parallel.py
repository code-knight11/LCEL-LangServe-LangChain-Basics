from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


model= ChatGroq(api_key=groq_api_key, model="openai/gpt-oss-120b")

prompt1= PromptTemplate(
    template='Generate a LinkedIn post about {topic}',
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template='Generate a Twitter post about {topic}',
    input_variables=['topic']
)

parser= StrOutputParser()

parallel_chain= RunnableParallel({
    'tweet': RunnableSequence(prompt1,model,parser),
    'linkedin_post': RunnableSequence(prompt2,model,parser)
})

response= parallel_chain.invoke({'topic': 'AI in Healthcare'})