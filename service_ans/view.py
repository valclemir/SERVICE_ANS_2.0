from load_data import ProcessingFileANS

PFA = ProcessingFileANS()
def showStartService(path):
    print('Iniciando o serviço....')
    PFA.DoStart(path)
    
def endExecution():
    print('Importação finalizada!')
