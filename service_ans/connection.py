import pymssql 
from config_db import Config
import logging
import sys

class Database:

    def __init__(self, Config):
        self.host = Config.db_host 
        self.domain = Config.db_domain
        self.user = Config.db_user 
        self.password = Config.db_password
        self.database = Config.db_name
        self.conn = None



    def open_connection(self):
        """Connect to SQL SERVER Database."""
        try:
         
            if self.conn is None:
                self.conn = pymssql.connect(server=self.host, 
                                            user=self.user, 
                                            password=self.password, 
                                            database=self.database)
                self.cur = self.conn.cursor()
         
        except Exception as e:
            print(e)
            sys.exit()
        finally:
            logging.info('Connection opened successfully.')
            return self.conn


  
    def execute(self, sql):
        self.open_connection()
        self.cur.execute(sql)
        self.commit()

    #Busca sql 
    def fetch(self, sql):
        self.open_connection()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.__disconnect__()
        return result


    def commit(self):
        if self.conn:
            self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def __disconnect__(self):
        if self.conn:
            self.conn.close()