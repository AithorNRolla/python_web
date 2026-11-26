from typing import List
from fastapi import FastAPI,HTTPException
from model.libros_model import Libro
from service.libros_service import LibrosService
app=FastAPI()
service=LibrosService()
@app.post("/libro",response_model=Libro)
def guardar_libro(libro:Libro):
    if service.alta_libro(libro)==None:
        raise HTTPException(status_code=409,detail="No admite isbn repetido")
    return libro
@app.get("/libro/{isbn}",response_model=Libro)
def buscar_libro(isbn:int):
    return service.buscar_libro(isbn)
@app.delete("/libro/{isbn}")
def eliminar_libro(isbn:int):
    service.eliminar_libro(isbn)