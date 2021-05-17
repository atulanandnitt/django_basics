import os
import sys
#from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from .movie_config import mysql_creds
#import movie_config

_MYSQL_DRIVER = 'mysql+pymysql'
_CHARSET = 'utf8'
_SESSION = None

_movie_db_url = "{}://{}:{}@{}/{}?charset={}".format(
    _MYSQL_DRIVER,
    mysql_creds['user'],
    mysql_creds['password'],
    mysql_creds['host'],
    mysql_creds['db'],
    mysql_creds['charset']
)

_movie_engine = create_engine(_movie_db_url, encoding='utf8', echo=False)
Base = automap_base()

Base.prepare(_movie_engine, reflect=True)

#Get all the tables here
Movie = Base.classes.movie #movie_atul_4  #movie: is table name from DB
#Actors= Base.classes.actors
Theaters = Base.classes.theaters

def get_movie_db_session():
    """
    Get movie db session
    :return: session
    """
    global _SESSION
    if _SESSION is None:
        session = sessionmaker(bind=_movie_engine)
        _SESSION = session()

    return _SESSION

def close_movie_db_session():
    """
    Close DB session
    :return: None
    """
    global _SESSION

    if _SESSION is not None:
        _SESSION.close()
        _SESSION = None
