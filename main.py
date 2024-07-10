from typing import List
from fastapi import FastAPI
from fastapi.params import Depends
from starlette.responses import RedirectResponse
import app.models as models,app.schemas as schemas
from app.Conexion import SessionLocal
from app.Conexion import engine
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get('/detalleventa/',response_model=List[schemas.DetalleVenta])
def show_Detalleventa(db:Session=Depends(get_db)):
    detalleventa = db.query(models.Detalleventa).all()
    return detalleventa

@app.post('/detalleventa/',response_model=schemas.DetalleVenta)
def create_Detalleventa(entrada:schemas.DetalleVenta,db:Session=Depends(get_db)):
    Detalleventas = models.Detalleventa(id_factura = entrada.id_factura,cod_factura=entrada.cod_factura,pago=entrada.pago,modelo=entrada.modelo,licencia=entrada.licencia,tipoSI=entrada.tipoSI)
    db.add(Detalleventas)
    db.commit()
    db.refresh(Detalleventas)
    return Detalleventas

@app.put('/detalleventa/{id_factura}',response_model=schemas.DetalleVenta)
def update_Detalleventa(id_factura:int,entrada:schemas.DetalleVentaUpdate,db:Session=Depends(get_db)):
    Detalleventas = db.query(models.Detalleventa).filter_by(id=id_factura).first()
    Detalleventas.id_factura=entrada.id_factura
    db.commit()
    db.refresh(Detalleventas)
    return Detalleventas

@app.delete('/detalleventa/{id_factura}',response_model=schemas.Respuesta)
def delete_Detalleventa(id_factura:int,db:Session=Depends(get_db)):
    Detalleventas = db.query(models.Detalleventa).filter_by(id=id_factura).first()
    db.delete(Detalleventas)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta

@app.get('/ciudades/',response_model=List[schemas.Ciudades])
def show_Cuiudad(db:Session=Depends(get_db)):
    ciudades = db.query(models.Ciudades).all()
    return ciudades

@app.post('/ciudades/',response_model=schemas.Ciudades)
def create_Cuiudad(entrada:schemas.Ciudades,db:Session=Depends(get_db)):
    ciudades = models.Ciudades(id_ciudad = entrada.id_ciudad,cod_ciudad=entrada.cod_ciudad, nombre_ciu=entrada. nombre_ciu)
    db.add(ciudades)
    db.commit()
    db.refresh(ciudades)
    return ciudades

@app.put('/ciudades/{id_ciudad}',response_model=schemas.Ciudades)
def update_Cuiudad(id_ciudad:int,entrada:schemas.CiudadesUpdate,db:Session=Depends(get_db)):
    ciudades = db.query(models.Ciudades).filter_by(id=id_ciudad).first()
    ciudades.id_ciudad=entrada.id_ciudad
    db.commit()
    db.refresh(ciudades)
    return ciudades

@app.delete('/ciudades/{id_ciudad}',response_model=schemas.Respuesta)
def delete_Cuiudad(id_ciudad:int,db:Session=Depends(get_db)):
    ciudades = db.query(models.Ciudades).filter_by(id=id_ciudad).first()
    db.delete(ciudades)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta

@app.get('/detallesmarcas/',response_model=List[schemas.Detallesmarcas])
def show_Detallesmarcas(db:Session=Depends(get_db)):
    detallemarca = db.query(models.Detallesmarcas).all()
    return detallemarca 

@app.post('/detallesmarcas/',response_model=schemas.Detallesmarcas)
def create_Detallesmarcas(entrada:schemas.Detallesmarcas,db:Session=Depends(get_db)):
    detallemarca = models.Detallesmarcas(id_marca  = entrada.id_marca ,cod_marca=entrada.cod_marca, marca=entrada. marca, tipo=entrada. tipo)
    db.add(detallemarca)
    db.commit()
    db.refresh(detallemarca)
    return detallemarca

@app.put('/detallesmarcas/{id_marca}',response_model=schemas.Detallesmarcas)
def update_Detallesmarcas(id_marca:int,entrada:schemas.DetallesmarcasUpdate,db:Session=Depends(get_db)):
    detallemarca = db.query(models.Detallesmarcas).filter_by(id=id_marca).first()
    detallemarca.id_marca=entrada. id_marca
    db.commit()
    db.refresh(detallemarca)
    return detallemarca

@app.delete('/detallesmarcas/{id_marca}',response_model=schemas.Respuesta)
def delete_Cuiudad(id_marca:int,db:Session=Depends(get_db)):
    detallemarca = db.query(models.Detallesmarcas).filter_by(id=id_marca).first()
    db.delete( detallemarca)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta

@app.get('/clientes/',response_model=List[schemas.Clientes])
def show_Clientes(db:Session=Depends(get_db)):
    cliente = db.query(models.Clientes).all()
    return cliente

@app.post('/clientes/',response_model=schemas.Clientes)
def create_Clientes(entrada:schemas.Clientes,db:Session=Depends(get_db)):
    cliente = models.Clientes( id_cliente = entrada.id_cliente ,cod_cliente=entrada.cod_cliente, DUI=entrada. DUI, telefono=entrada. telefono, direccion=entrada. direccion, correo=entrada. correo, estado=entrada. estado, EstadoFactura=entrada. EstadoFactura)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

@app.put('/clientes/{id_cliente}',response_model=schemas.Clientes)
def update_Clientes(id_cliente:int,entrada:schemas.ClientesUpdate,db:Session=Depends(get_db)):
    cliente = db.query(models.Clientes).filter_by(id=id_cliente).first()
    cliente.id_cliente=entrada. id_cliente
    db.commit()
    db.refresh(cliente)
    return cliente

@app.delete('/clientes/{id_cliente}',response_model=schemas.Respuesta)
def delete_Clientes(id_cliente:int,db:Session=Depends(get_db)):
    cliente = db.query(models.Clientes).filter_by(id=id_cliente).first()
    db.delete( cliente)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta

@app.get('/producto/',response_model=List[schemas.Productos])
def show_Productos(db:Session=Depends(get_db)):
    producto = db.query(models.Productos).all()
    return producto

@app.post('/producto/',response_model=schemas.Productos)
def create_Productos(entrada:schemas.Productos,db:Session=Depends(get_db)):
    producto = models.Productos( id_cliente = entrada.id_cliente ,cod_cliente=entrada.cod_cliente, DUI=entrada. DUI, telefono=entrada. telefono, direccion=entrada. direccion, correo=entrada. correo, estado=entrada. estado, EstadoFactura=entrada. EstadoFactura)
    db.add(producto)
    db.commit()
    db.refresh(producto)
    return producto 

@app.put('/clientes/{id_cliente}',response_model=schemas.Clientes)
def update_Clientes(id_cliente:int,entrada:schemas.ClientesUpdate,db:Session=Depends(get_db)):
    cliente = db.query(models.Clientes).filter_by(id=id_cliente).first()
    cliente.id_cliente=entrada. id_cliente
    db.commit()
    db.refresh(cliente)
    return cliente

@app.delete('/clientes/{id_cliente}',response_model=schemas.Respuesta)
def delete_Clientes(id_cliente:int,db:Session=Depends(get_db)):
    cliente = db.query(models.Clientes).filter_by(id=id_cliente).first()
    db.delete( cliente)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta
