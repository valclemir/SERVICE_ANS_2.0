from view import showStartService, endExecution
import time
from config_db import Config



def start(path):
   try:
      start_time = time.time()
      showStartService(path)
   except Exception as e:
      print(e)
   finally:
      endExecution()
      elapsed_time = time.time() - start_time
      print('Tempo decorrido...: '+str(time.strftime("%H:%M:%S", time.gmtime(elapsed_time))))
   
  
#'Z:\\ARQUIVOS_ANS'
if __name__ == '__main__':
   start(Config.path)