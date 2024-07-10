from typing import Optional
from pydantic import BaseModel

class DetalleVenta(BaseModel):
    id_factura: Optional[int] = None  # Usar anotaciones de tipo correctamente
    cod_factura: int  # Asumiendo que el código de factura es un entero
    pago: float  # Asumiendo que el pago es un valor decimal
    modelo: str  # Modelo como cadena de texto
    licencia: str  # Licencia como cadena de texto
    tipoSI: str  # Tipo de Sistema de Información como cadena de texto

    class Config:
        orm_mode = True

class DetalleVentaUpdate(BaseModel):   
    id_factura: Optional[int] = None
   

    class Config:
        orm_mode =True

class Respuesta(BaseModel):   
    mensaje:str


class Ciudades(BaseModel):
    id_ciudad: Optional[int] = None  # Usar anotaciones de tipo correctamente
    cod_ciudad: str  # Modelo como cadena de texto
    nombre_ciu: str  # Licencia como cadena de texto
    

    class Config:
        orm_mode = True

class CiudadesUpdate(BaseModel):   
    id_ciudad: Optional[int] = None
   

    class Config:
        orm_mode =True

class Respuesta(BaseModel):   
    mensaje:str
   

class Detallesmarcas(BaseModel):
    id_marca : Optional[int] = None  # Usar anotaciones de tipo correctamente
    cod_marca: int
    marca: str  # Modelo como cadena de texto
    tipo: str  # Licencia como cadena de texto
    

    class Config:
        orm_mode = True

class DetallesmarcasUpdate(BaseModel):   
    id_marca: Optional[int] = None
   

    class Config:
        orm_mode =True

class Respuesta(BaseModel):   
    mensaje:str
   
class Clientes(BaseModel):
    id_cliente : Optional[int] = None  # Usar anotaciones de tipo correctamente
    cod_cliente: int
    apellido : str
    DUI : str
    telefono : str
    ciudad : str
    direccion : str
    correo : str
    estado : str
    EstadoFactura : str

    class Config:
        orm_mode = True

class ClientesUpdate(BaseModel):   
    id_cliente: Optional[int] = None
   

    class Config:
        orm_mode =True

class Respuesta(BaseModel):   
    mensaje:str
   


class Productos(BaseModel):
    id_producto :  Optional[int] = None
    cod_producto : str
    nombre : str
    tipo : str
    cantidad : int
    marca : str
    garantia : str

    class Config:
        orm_mode = True

