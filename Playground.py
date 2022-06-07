import csv
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

    # 0. RawQuery
    logger.info("")
    logger.info("# 0. RawQuery")

    # corremos la query que queremos
    resultSet = session.execute('SELECT * FROM cazadores')

    # si vamos a usar mas de una vez los resultados, nos serive hacer un fetchall
    data = resultSet.fetchall()

    # obtenemos el nombre de las columnas
    columns = resultSet.keys()
    logger.info(columns)
    logger.info(resultSet)

    # iteramos sobre la data cruda
    for row in data:
        logger.info(row)

    # generamos un csv con la data
    outfile = open('query0.csv', 'w', newline='')
    outcsv = csv.writer(outfile, delimiter=',')
    outcsv.writerow(columns)
    outcsv.writerows(data)

    # 1. cazadores que tienen en el nombre one
    logger.info("")
    logger.info("# 1. cazadores que tienen en el nombre one")
    query = session.query(Cazadores.nombre, Cazadores.birthday, Cazadores.rango, Cazadores.pais_origen) \
        .where(Cazadores.nombre.like("%one%"))

    # obtenemos las columnas si estamos usando las funcionalidades del ORM
    columns = [column.get("name") for column in query.column_descriptions]
    logger.info(columns)

    # iteramos sobre la data, en este caso no es necesario hacer un fetchall
    for row in query:
        logger.info(row)

    # ahora generamos un tsv
    outfile = open('query1.tsv', 'w', newline='')
    outcsv = csv.writer(outfile, delimiter='\t')
    outcsv.writerow(columns)
    outcsv.writerows(query.all())

    # 2. Ataques que mas se repiten para Cazador con Tan o Jiro
    logger.info("")
    logger.info("# 2. Ataques que mas se repiten para Cazador con Tan o Jiro")
    query = session.query(Ataques.nombre_ataque, Ataques.id_ataque, Cazadores.nombre, func.count(Ataques.id_ataque)) \
        .join(CazadoresAtaques.ataques) \
        .join(Cazadores) \
        .where(or_(Cazadores.nombre.like("%milk%"), Cazadores.nombre.like("%test 1%"))) \
        .group_by(Ataques.id_ataque) \
        .order_by(func.count(Ataques.id_ataque).desc()).filter(Ataques.nombre_ataque == 'genetic_milk')

    logger.info("")
    logger.info("Revisamos la query que está corriendo.")
    logger.info(query.statement)

    for row in query:
        logger.info(row)

    # cerramos la sesión con la base de datos
    logger.info("")
    logger.info("# cerramos la sesión con la base de datos")
    session.close()
