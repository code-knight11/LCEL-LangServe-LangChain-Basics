from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

# Step 1: Loading the API key and setting up the model

grop_api_key= os.getenv("GROQ_API_KEY")
model= ChatGroq(model="openai/gpt-oss-120b", api_key=grop_api_key)

# Step 2: Creating the prompt template

system_template= "Translate the following text into {language} :"

prompt_template=ChatPromptTemplate.from_messages([
    ('system',system_template),
    ('user','{text}')
])

# Step 3: Initializing the Output Parser

parser= StrOutputParser()

# Step 4: Create the chain

chain= prompt_template|model|parser

# App Definition

app=FastAPI(title="Langchain Server",
            version="1.0",
            description="A simple API server using Langchain  runnable interfaces")

# Adding chain routes
add_routes(
    app,
    chain,
    path="/chain"
    
)

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)