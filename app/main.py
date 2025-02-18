from fastapi import FastAPI
from routers.books_router import router as book_router

app = FastAPI()

app.include_router(book_router)



