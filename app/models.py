from sqlalchemy import Column, Integer, String
from .Conexion import Base

class Detalleventa(Base):
    __tablename__ = 'detalleventa'
    id_factura  = Column(Integer, primary_key=True, index=True)
    cod_factura = Column(Integer, unique=True)
    pago = Column(Integer)
    modelo = Column(String(50))
    licencia = Column(String(10))
    tipoSI = Column(String(25))

class Ciudades(Base):
    __tablename__ = 'ciudades'
    id_ciudad  = Column(Integer, primary_key=True, index=True)
    cod_ciudad = Column(String(3))
    nombre_ciu = Column(String(50))

class Detallesmarcas(Base):
    __tablename__ = 'detallesmarcas'
    id_marca  = Column(Integer, primary_key=True, index=True)
    cod_marca = Column(Integer, unique=True)
    marca = Column(String(50))
    tipo = Column(String(50))

class Clientes(Base):
    __tablename__ = 'clientes'
    id_cliente  = Column(Integer, primary_key=True, index=True)
    cod_cliente = Column(Integer, unique=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    DUI = Column(String(9), unique=True)
    telefono = Column(String(50))
    ciudad = Column(String(50))
    direccion = Column(String(50))
    correo = Column(String(50))
    estado = Column(String(1))
    EstadoFactura = Column(String(50))

class Productos(Base):
    __tablename__ = 'producto'
    id_producto   = Column(Integer, primary_key=True, index=True)
    cod_producto = Column(String(50))
    nombre = Column(String(50))
    tipo = Column(String(50))
    cantidad = Column(Integer)
    marca = Column(String(50))
    garantia = Column(String(50))
 

