import requests
from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os
load_dotenv()
app = FastAPI()

def fun(role, text):
    url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/chat?version=2023-05-29"

    body = {
        "messages": [
            {"role": "system", "content": role},
            {"role": "user", "content": text}
        ],
        "project_id": os.getenv("projid"),
        "model_id": "ibm/granite-20b-code-instruct",
        "frequency_penalty": 0,
        "max_tokens": 7000,
        "presence_penalty": 0,
        "temperature": 0,
        "top_p": 1
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.getenv("token")  # Store securely in real projects
    }

    response = requests.post(url, headers=headers, json=body)

    if response.status_code != 200:
        return {"error": response.text}

    return response.json()
@app.post("/reqclass")
async def requirement_classification(req: Request):
    data = await req.json()
    role = (
        "You are an expert AI for software requirement classification. Your job is to read raw, "
        "unstructured software requirements and classify each sentence into one of the five SDLC phases: "
        "Requirements, Design, Development, Testing, or Deployment. Be accurate and detailed."
    )
    return fun(role, data["prompt"])

@app.post("/codegen")
async def code_generator(req: Request):
    data = await req.json()
    role = (
        "You are an expert software developer. Generate clean, production-ready code based on the given "
        "natural language prompt or user story. Ensure the output is syntactically correct and well-structured."
    )
    return fun(role, data["prompt"])

@app.post("/bugfix")
async def bug_fixer(req: Request):
    data = await req.json()
    role = (
        "You are a software debugging expert. Fix bugs in the given code snippet and return the corrected version. "
        "Also ensure the code is optimized and logically sound."
    )
    return fun(role, data["prompt"])

@app.post("/testcase")
async def test_case_generator(req: Request):
    data = await req.json()
    role = (
        "You are a test automation engineer. Based on the provided function or requirement, generate test cases "
        "using Python unittest or pytest. Ensure full coverage and correctness."
    )
    return fun(role, data["prompt"])
@app.post("/chatbot")
async def chatbot_assistant(req: Request):
    data = await req.json()
    role = (
        "You are an AI assistant that answers questions related to the software development lifecycle. "
        "Provide clear, accurate, and helpful responses on topics like testing, design, requirement analysis, and debugging."
    )
    return fun(role, data["prompt"])
@app.post("/codesum")
async def code_summarizer(req: Request):
    data = await req.json()
    role = (
        "You are a documentation specialist. Read the given code and summarize its purpose, logic, and usage "
        "in simple terms to help other developers understand it easily."
    )
    return fun(role, data["prompt"])

@app.post("/chatbot")
async def chatbot_assistant(req: Request):
    data = await req.json()
    role = (
        "You are an AI assistant that answers questions related to the software development lifecycle. "
        "Provide clear, accurate, and helpful responses on topics like testing, design, requirement analysis, and debugging."
    )
    return fun(role, data["prompt"])