from dotenv import load_dotenv
import os
from src.helper import load_pdf_file, filter_to_minimal_docs, text_split, download_embeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

#load env file
load_dotenv()

#get api keys from the env file and set them as environment variables
pinecone_api_key = os.getenv("PINECONE_MEDICAL_CHATBOT")
os.environ["PINECONE_API_KEY"] = pinecone_api_key
gemini_api_key = os.getenv("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = gemini_api_key

#extract data from the pdf file
extracted_data = load_pdf_file(data='data/')

#clean the data by removing the unwanted metadata
filter_data = filter_to_minimal_docs(extracted_data)

#make text chunks
text_chunks = text_split(filter_data)

#download the embedding model
embeddings = download_embeddings()

#setup for calling pinecone api
pc = Pinecone(api_key=pinecone_api_key)

index_name = "medical-chatbot"

# if not pc.has_index(index_name):
#     pc.create_index(
#         name=index_name,
#         dimension=384,
#         metric="cosine",
#         spec=ServerlessSpec(cloud="aws", region="us-east-1")
#     )

index = pc.Index(index_name)

#load existing index

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

print("DB loaded successfully\n")
