# ==========================================
# 1. IMPORTACIONES
# ==========================================
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# ==========================================
# 2. INICIALIZACIÓN (El motor de la API)
# ==========================================
# OJO: Lleva paréntesis () porque estás creando un objeto/instancia de la clase FastAPI
app = FastAPI(title="Mi Primera API", version="1.0.0")

# ==========================================
# 3. MODELOS DE DATOS (Moldes Pydantic)
# ==========================================
# Define qué forma tienen los datos que entran y salen (en JSON)
class Empleado(BaseModel):
    nombre: str
    edad: int
    salario_base: float
    departamento: str | None = None  # Campo opcional

# Base de datos simulada en memoria para practicar
lista_empleados = [
    {"id": 1, "nombre": "Ana", "edad": 28, "salario_base": 2200.0, "departamento": "IT"}
]

# ==========================================
# 4. RUTAS / ENDPOINTS (El menú del restaurante)
# ==========================================

# --- GET: Leer / Consultar ---
@app.get("/")  # El '@' es un decorador; "/" es la ruta raíz
def saludar():
    return {"mensaje": "Bienvenido a FastAPI"}

# --- GET con parámetro de RUTA (Path) ---
# Ejemplo URL: http://127.0.0
@app.get("/empleados/{emp_id}")
def obtener_empleado(emp_id: int):
    for emp in lista_empleados:
        if emp["id"] == emp_id:
            return emp
    # Si no lo encuentra, lanza error 404 controlado
    raise HTTPException(status_code=404, detail="Empleado no encontrado")

# --- GET con parámetro de CONSULTA (Query) ---
# Ejemplo URL: http://127.0.0
@app.get("/saludo")
def saludar_persona(nombre: str, edad: int = 18):
    return {"saludo": f"Hola {nombre}, tienes {edad} años"}

# --- POST: Crear un nuevo registro ---
# Recibe un JSON con la forma de la clase Empleado
@app.post("/empleados", status_code=201)
def crear_empleado(nuevo_emp: Empleado):
    datos = nuevo_emp.model_dump()  # Convierte el objeto Pydantic a diccionario
    datos["id"] = len(lista_empleados) + 1
    lista_empleados.append(datos)
    return {"mensaje": "Empleado creado", "empleado": datos}

# --- PUT: Actualizar un registro existente ---
@app.put("/empleados/{emp_id}")
def actualizar_empleado(emp_id: int, emp_actualizado: Empleado):
    for index, emp in enumerate(lista_empleados):
        if emp["id"] == emp_id:
            datos = emp_actualizado.model_dump()
            datos["id"] = emp_id
            lista_empleados[index] = datos
            return {"mensaje": "Empleado actualizado", "empleado": datos}
    raise HTTPException(status_code=404, detail="Empleado no encontrado")

# --- DELETE: Borrar un registro ---
@app.delete("/empleados/{emp_id}")
def eliminar_empleado(emp_id: int):
    for index, emp in enumerate(lista_empleados):
        if emp["id"] == emp_id:
            eliminado = lista_empleados.pop(index)
            return {"mensaje": "Empleado eliminado", "empleado": eliminado}
    raise HTTPException(status_code=404, detail="Empleado no encontrado")
