# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import datetime

import randomname
from dotenv import load_dotenv
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session

from models import Cazadores

load_dotenv()  # take environment variables from .env.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # conexión con la base de datos
    engine = create_engine(os.getenv('DATABASE'))

    # iniciamos una sesión
    session = Session(engine)

    # obtener último ID de los cazadores
    print("LastID:")
    lastId = session.query(Cazadores.id_cazador).order_by(Cazadores.id_cazador.desc()).first().id_cazador
    if lastId is None:
        lastId = 1
    print(lastId)

    print()
    print("Creamos cazadores...")
    for x in range(10):
        lastId = lastId + 1
        stmt = insert(Cazadores).values(id_cazador=lastId, nombre=randomname.get_name() + str(lastId), rango='El mejor',
                                        pais_origen='Chile',
                                        birthday=datetime.datetime.now())
        result = session.execute(stmt)
    session.commit()

    print()
    print("Mostramos todos los cazadores...")
    for jugador in session.query(Cazadores).all():
        print(jugador.nombre)

    print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
