#Project Description
Medical Assistment system, trained on data. Can get feedback on questions.

#Architecture
To make a task specific inference system:
There are two methods:  1. RAG Based --> Create Knowledge base with the custome data, connect LLM with the knowledge base. 
                        2. Finetuning Based --> Need lots of data, need lots of compute power, lots of cost involved.

We are using RAG in this project.

Create a vector data base on PINECONE, use LANGCHAIN orchestration, connect application with the help of it.

#Data for the project
Book --> Gale Encyclopedia of Medicine

Using Langchain:
    1. From pdf extract documents of the book.
    2. Perform chunking(As it not possible to pass entire book pdf to the LLM we do chunking)
    3. Embedding the chunks. We get vector embedding.
    4. Store vector embeddings on vector database.(Pinecone)

Frontend and Backend using Flask

#Techstack
Python
OpenAI api
Langchain
Pinecone
Flask
AWS --> CI/CD

#CI/CD Piple line

Github Project Code --> Github Actions --> AWS Cloud --> EC2(virtual Machine)

Create a Docker Image on ECR for the Github actions, pull that image on EC2
EC2 do port mapping, release IP addr and user can use application

