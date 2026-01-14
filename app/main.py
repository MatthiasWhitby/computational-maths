from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_method=["*"],
  allow_headers=["*"],
)

queries = []

@app.post("/queries/")
async def add_query(query: dict):
  queries.append(query)
  return {"status": "ok", "query_received": query}