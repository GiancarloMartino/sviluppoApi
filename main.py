from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
app = FastAPI()

# Dati di esempio
database = []

# Definizione del modello di dati per gli utenti
class User(BaseModel):
    id: int
    name: str
    email: str

# Endpoint per creare un nuovo utente
@app.post("/users", response_model=User)
def create_user(user: User):
    database.append(user)
    return {"message": "Utente creato correttamente"}

# Endpoint per ottenere tutti gli utenti
@app.get("/users", response_model=list[User])
def get_users():
    return database

# Endpoint per ottenere un singolo utente in base all'ID
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in database:
        if user.id == user_id:
            return user
    return {"message": "Utente non trovato"}

# Endpoint per eliminare un utente in base all'ID
@app.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int):
    for user in database:
        if user.id == user_id:
            database.remove(user)
            return {"message": "Utente eliminato correttamente"}
    return {"message": "Utente non trovato"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)