import datetime
import logging
import os

import coloredlogs
import randomname
from dotenv import load_dotenv
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session

from models import Cazadores, Ataques

# create logger
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

# take environment variables from .env.
load_dotenv()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # conexión con la base de datos
    engine = create_engine(os.getenv('DATABASE'))

    # iniciamos una sesión
    session = Session(engine)

    # obtener último ID de los cazadores
    lastId = session.query(Cazadores.id_cazador).order_by(Cazadores.id_cazador.desc()).first().id_cazador
    if lastId is None:
        lastId = 1
    logger.info("LastID Cazador=" + str(lastId))

    print()
    logger.info("Creamos cazadores...")
    for x in range(10):
        lastId = lastId + 1
        stmt = insert(Cazadores).values(id_cazador=lastId, nombre=randomname.get_name(), rango='El mejor',
                                        pais_origen='Chile',
                                        birthday=datetime.datetime.now())
        result = session.execute(stmt)
    session.commit()

    print()
    logger.info("Mostramos todos los cazadores...")
    for jugador in session.query(Cazadores).all():
        logger.info(jugador.nombre)

    print()

    # obtener último ID de los ataques
    lastId = session.query(Ataques.id_ataque).order_by(Ataques.id_ataque.desc()).first().id_ataque
    if lastId is None:
        lastId = 1
    logging.info("LastID Ataque=" + str(lastId))

    logger.info("Creamos ataques...")
    for x in range(10):
        lastId = lastId + 1
        stmt = insert(Ataques).values(id_ataque=lastId, nombre_ataque=randomname.get_name(), arma=randomname.get_name())
        result = session.execute(stmt)
    session.commit()

    logger.info("Mostramos todos los ataques...")
    for ataque in session.query(Ataques).all():
        logger.info(ataque.nombre_ataque)

    print()

    # cerramos la sesión con la base de datos
    session.close()
