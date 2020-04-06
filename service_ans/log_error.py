from connection import Database
from config_db import Config

db = Database(Config)

class logError:
    
    def insert_log_error(self, ds_erro, ds_metodo):
         
        SQL = (f'''SP_INSERE_LOG_ERRO @p_DS_ERRO = '{ds_erro}'
                                    , @p_DS_METODO = '{ds_metodo}' ''')
        db.execute(SQL)
        
