import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.connection import init_db
from routes.products import product_router

app = FastAPI()

# Register routes
app.include_router(product_router, prefix="/product")

# register origins
origins = ["*"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=False,
                   allow_methods=["*"],
                   allow_headers=["*"])


@app.on_event("startup")
async def start_db():
    await init_db()

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
