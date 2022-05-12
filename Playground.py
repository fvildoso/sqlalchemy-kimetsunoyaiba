import logging
import os
from operator import or_

import coloredlogs
from dotenv import load_dotenv
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

from models import Cazadores, Ataques, CazadoresAtaques

# create logger
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

# take environment variables from .env.
load_dotenv()

if __name__ == '__main__':
    # conexión con la base de datos
    engine = create_engine(os.getenv('DATABASE'))

    # iniciamos una sesión
    session = Session(engine)

    # 1. cazadores que tienen en el nombre one
    query = session.query(Cazadores.nombre, Cazadores.birthday, Cazadores.rango, Cazadores.pais_origen) \
        .where(Cazadores.nombre.like("%one%"))

    for row in query:
        logger.info(row)

    # 2. Ataques que mas se repiten para Cazador con Tan o Jiro
    logger.info("Ataques que más se repiten")
    query = session.query(Ataques.nombre_ataque, Ataques.id_ataque, Cazadores.nombre, func.count(Ataques.id_ataque)) \
        .join(CazadoresAtaques.ataques) \
        .join(Cazadores) \
        .where(or_(Cazadores.nombre.like("%milk%"), Cazadores.nombre.like("%test 1%"))) \
        .group_by(Ataques.id_ataque) \
        .order_by(func.count(Ataques.id_ataque).desc()).filter(Ataques.nombre_ataque == 'genetic_milk')
    logger.info(query.statement)

    for row in query:
        logger.info(row)

    # cerramos la sesión con la base de datos
    session.close()
