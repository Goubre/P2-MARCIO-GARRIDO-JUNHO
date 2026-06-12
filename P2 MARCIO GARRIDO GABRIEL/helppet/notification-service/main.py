from fastapi import FastAPI

app = FastAPI(title="HelpPet Notification Service", version="1.0.0")


@app.get("/")
def home():
    return {"message": "Notification Service funcionando!"}


@app.post("/notifications")
def send_notification(animal_name: str):
    return {
        "message": f"Notificação enviada: o animal {animal_name} foi encontrado!"
    }