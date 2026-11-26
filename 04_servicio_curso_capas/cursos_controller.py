from typing import List
from fastapi import FastAPI,HTTPException
from cursos_service import Curso, Cursos_service

""" class Curso(BaseModel):
    codigo:int
    nombre:str
    tematica:str
    precio:float
     """
app=FastAPI()
lista_cursos=[]
@app.post("/curso",response_model=Curso)
def alta_curso(curso:Curso):
    service=Cursos_service()
    return service.alta_curso(curso)
@app.get("/cursos",response_model=List[Curso])
def cursos_tematica(tematica:str):
    service=Cursos_service()
    return service.buscar_tematica(tematica)
@app.delete("/curso")
def eliminar_curso(codigo:int):
    if codigo<=0:
        raise HTTPException(status_code=409,detail="Código de curso inválido!")
    service=Cursos_service()
    service.eliminar_curso(codigo)