from fastapi import FastAPI, status
from contextlib import asynccontextmanager
from app.core.db import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
  print ("Lifespan start")
  try:
    init_db()
    yield
  except Exception as e:
    print(f"error {e}")
    print ("Lifespan Ends")


#  app initialization to create server
app = FastAPI(
  lifespan=life_span
)


@app.get("/", status_code = status.HTTP_200_OK)
async def root():
   return {"status":True, "message":"Welcome to my personal blog"}
