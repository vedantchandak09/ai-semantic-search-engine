from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from search import semantic_search, documents

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search_api(query: str):
    results = semantic_search(query)
    return {"results": [documents[i] for i in results]}

@app.get("/")
def serve_frontend():
    return FileResponse("frontend/index.html")