from fastapi import FastAPI

#Hacer un API REST con una función que reciba el dni del alumno, 
#devuelva su ficha formada por dni, nombre, edad y email. 
class Alumno:
    def __init__(self,dni,nombre,edad,email):
        self.dni=dni
        self.nombre=nombre
        self.edad=edad
        self.email=email 
        
app=FastAPI()
@app.get("/ficha/{dni}")
def ficha(dni):
    if dni==None:
        return None 
    return Alumno(dni,"prueba",22,"prueba@gmail.com")