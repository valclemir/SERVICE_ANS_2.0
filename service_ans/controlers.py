from view import showStartService, endExecution
import time
from config_db import Config



def start(path):
      start_time = time.time()
      showStartService(path)
      endExecution()
      elapsed_time = time.time() - start_time
      print('Tempo decorrido...: '+str(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))+'\n')
   
  
#'Z:\\ARQUIVOS_ANS'
if __name__ == '__main__':
   start(Config.path)