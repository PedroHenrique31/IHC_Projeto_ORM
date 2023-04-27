"""
Author: Pedro Henrique Carneiro de Araújo

    Treinando mapeamento Objeto-Relacional
    Vou copiar uns codigos aqui, mpra entender como usar o SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

# ------- Variáveis globais ---------------------------------------------------
# Ligação com o DB feita por um objeto motor -engine- do SQLAlchemy ele que realiza o trabalho de conectar e mapear
motor=create_engine("mysql+mysqlconnector://pedro:senha@localhost/db_escola?charset=utf8mb4")
# estrutura URL:  ([tipoDB]+[tipoConnector]://[nomeUsuário]:[senha]@[localacesso]/[nomeSchema]?[outrasInfo])