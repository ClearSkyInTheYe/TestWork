import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import pandas as pd
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, create_engine
from sqlalchemy_utils import database_exists, create_database
from datetime import datetime


class Db:
    def __init__(self) -> None:
        self.count = 0
        self.engine = create_engine('postgresql+psycopg2://user1:1234@localhost:5432/test')
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        self.engine.connect()
        # self.cursor = self.engine.cursor()
        self.engine.execute('''CREATE TABLE IF NOT EXISTS List_of_files(
                                file_id  serial primary key,
                                filename VARCHAR,
                                dbname VARCHAR,
                                info VARCHAR);''')
    
    def add_to_list_of_files(self, filename:str,  info:str) ->str:
        self.count += 1
        dbname = 'f' + str(self.count)
        self.engine.execute(f'''INSERT INTO List_of_files(filename, dbname, info) 
                            VALUES('{filename}', '{dbname}', '{str(info).replace("'", '"')}');''')
        return dbname
    
    def get_info(self):
        x = self.engine.execute('select * from list_of_files')
        print(x.fetchall())
