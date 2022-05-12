# coding: utf-8
from sqlalchemy import Column, Date, DateTime, ForeignKey, text
from sqlalchemy.dialects.mysql import INTEGER, TINYTEXT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Ataques(Base):
    __tablename__ = 'ataques'

    id_ataque = Column(INTEGER(11), primary_key=True)
    nombre_ataque = Column(TINYTEXT)
    arma = Column(TINYTEXT, nullable=False)


class Cazadores(Base):
    __tablename__ = 'cazadores'

    id_cazador = Column(INTEGER(11), primary_key=True)
    nombre = Column(TINYTEXT)
    birthday = Column(Date)
    rango = Column(TINYTEXT)
    pais_origen = Column(TINYTEXT, nullable=False)


class Demonios(Base):
    __tablename__ = 'demonios'

    id_demonio = Column(INTEGER(11), primary_key=True)
    nombre = Column(TINYTEXT, nullable=False)
    rango = Column(TINYTEXT, nullable=False)


class Enfrentamientos(Base):
    __tablename__ = 'enfrentamientos'

    id_enfrentamiento = Column(INTEGER(11), primary_key=True)
    fecha = Column(DateTime)


class CazadoresAtaques(Base):
    __tablename__ = 'cazadores_ataques'

    id_cazador_ataque = Column(INTEGER(11), primary_key=True)
    id_ataque = Column(ForeignKey('ataques.id_ataque'), index=True)
    id_cazador = Column(ForeignKey('cazadores.id_cazador'), index=True)
    desde = Column(DateTime, server_default=text("current_timestamp()"))

    ataques = relationship('Ataques')
    cazadores = relationship('Cazadores')


class DetalleEnfrentamientos(Base):
    __tablename__ = 'detalle_enfrentamientos'

    id_detalle_enfrentamiento = Column(INTEGER(11), primary_key=True)
    id_cazador = Column(ForeignKey('cazadores.id_cazador'), index=True)
    id_demonio = Column(ForeignKey('demonios.id_demonio'), index=True)
    id_enfrentamiento = Column(ForeignKey('enfrentamientos.id_enfrentamiento'), index=True)
    estado_cazador = Column(TINYTEXT)
    estado_demonio = Column(TINYTEXT)

    cazadores = relationship('Cazadores')
    demonios = relationship('Demonios')
    enfrentamientos = relationship('Enfrentamientos')
