from fastapi import FastAPI
from app.presentation.animal_controller import router

app = FastAPI(
    title="HelpPet API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "HelpPet API funcionando!"}