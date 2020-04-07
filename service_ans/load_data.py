from connection import Database
from pandas import read_excel, read_sql, DataFrame
import os 
from config_db import Config
import datetime 
from send_mail import SendMail
from ftplib import FTP
from log_error import logError
import pymssql

db = Database(Config)
log = logError()
class ProcessingFileANS:

    def downloadFile(self):       
        try:  
            ftp = FTP(Config.ftp_host)
            ftp.login(user=Config.ftp_user, passwd=Config.ftp_password)
            
            listing = []
            ftp.retrlines("LIST", listing.append)
            if len(listing) != 0: #File existing to download 
                words = listing[0].split(None, 8)
                filename = words[-1].lstrip()
                # download the file to folder repository
                local_filename = os.path.join(Config.ftp_folder, filename)
                lf = open(local_filename, "wb")
                ftp.retrbinary("RETR " + filename, lf.write, 8*1024)
                ftp.delete(filename) #delete file
                lf.close()
        except Exception as e:
            log.insert_log_error(str(e), 'downloadFile')


    
    def remove_file_xlsx(self, path):
        try: 
            if os.name == 'nt':
                bar = '\\'
            elif os.name == 'posix':
                bar = '/'
            listdir = os.listdir(path)
            path = path+bar+listdir[-1]
            for root, dirs, files in os.walk(path):
                path = root+bar+''.join(files)
            os.remove(path)
        except Exception as e:
            log.insert_log_error(str(e), 'remove_file_xlsx')


    def check_competencia(self, path): 
        DF = None 
        listdir = os.listdir(path)
        datesDir = None 
        if len(listdir) != 0:
            i = listdir[-1]
            datesDir = i[13:20]+'-01'
            datesDir = datesDir.replace('_', '-')
            SQL = (f'''SELECT * FROM BENEFICIARIOANS WHERE COMPETENCIA = '{datesDir}' ''')
            DF = read_sql(SQL, db.open_connection())

        return DF, datesDir


    def read_data_excel(self, path):
        try: 
            if os.name == 'nt':
                bar = '\\'
            elif os.name == 'posix':
                bar = '/'
            listdir = os.listdir(path)
            path = path+bar+listdir[-1]
            for root, dirs, files in os.walk(path):
                path = root+bar+''.join(files)
            return read_excel(path)
        except Exception as e:
            log.insert_log_error(str(e), 'read_data_excel')
        

    def insert_table_beneficiarioans(self, DF, path):
        competencia = None 
        status = None 
        try:
            status = 2  #File processing completed
            competencia = self.check_competencia(path)[1]
            
            DF['COMPETENCIA'] = competencia
            DF['BENEFICIARIO_ID'] = DF.index
            DF['CONFERENCIA_ID'] = DF.index


            DF['CD_MUNICIPIO'].fillna(0, inplace=True)
            DF['NUMERO'].fillna(0, inplace=True)
            DF['LOGRADOURO'].fillna('nan', inplace=True)
            DF['BAIRRO'].fillna('nan', inplace=True)
            DF['COMPLEMENTO'].fillna('nan', inplace=True)
            DF['CD_MUNICIPIO_RESIDENCIA'].fillna(0, inplace=True)
            DF['CCO_BENEFICIARIO_TITULAR'].fillna(0, inplace=True)
            DF['CNPJ_EMPRESA_CONTRATANTE'].fillna(0, inplace=True)
            DF['CPF'].fillna(0, inplace=True)
            DF['CNS'].fillna(0, inplace=True)
            DF['CEP'].fillna(0, inplace=True)
            DF['RESIDE_EXTERIOR'].fillna(0, inplace=True)
            DF['NR_PLANO_ANS'].fillna(0 , inplace=True)
            DF['REL_DEPEND'].fillna(0 , inplace=True)
            DF['MTV_CANCELAMENTO'].fillna(0, inplace=True)





            DF['DT_ATUALIZACAO'] = '20'+DF['DT_ATUALIZACAO'].str[6:9]+'-'+DF['DT_ATUALIZACAO'].str[3:5]+'-'+DF['DT_ATUALIZACAO'].str[0:2]
            DF['DT_NASCIMENTO'] = '20'+DF['DT_NASCIMENTO'].str[6:9]+'-'+DF['DT_NASCIMENTO'].str[3:5]+'-'+DF['DT_NASCIMENTO'].str[0:2]
            DF['DT_CANCELAMENTO'] = '20'+DF['DT_CANCELAMENTO'].str[6:9]+'-'+DF['DT_CANCELAMENTO'].str[3:5]+'-'+DF['DT_CANCELAMENTO'].str[0:2]
            DF['DT_CONTRATACAO'] = '20'+DF['DT_CONTRATACAO'].str[6:9]+'-'+DF['DT_CONTRATACAO'].str[3:5]+'-'+DF['DT_CONTRATACAO'].str[0:2]
            for i in range(len(DF)):
                BAIRRO = str(DF.BAIRRO[i].replace("'", ''))
                LOGRADOURO = str(DF.LOGRADOURO[i].replace("'", ''))
                COMPLEMENTO = str(DF.COMPLEMENTO[i].replace("'", ''))
                
                SQL = (f'''EXEC SP_INSERT_BENEFICIARIOANS @p_BENEFICIARIO_ID= '{DF.BENEFICIARIO_ID[i]}',
                                                    @p_CCO= '{DF.CCO[i]}',
                                                    @p_SITUACAO= '{DF.SITUACAO[i]}' ,
                                                    @p_dataAtualizacao= '{DF.DT_ATUALIZACAO[i]}',
                                                    @p_CONFERENCIA_ID= '{DF.CONFERENCIA_ID[i]}',
                                                    @p_LOGRADOURO= '{LOGRADOURO}',
                                                    @p_NUMERO= '{DF.NUMERO[i]}',
                                                    @p_COMPLEMENTO= '{COMPLEMENTO}',
                                                    @p_BAIRRO= '{BAIRRO}',
                                                    @p_codigoMunicipio= {DF.CD_MUNICIPIO[i]},
                                                    @p_codigoMunicipioResidencia= {DF.CD_MUNICIPIO_RESIDENCIA[i]},
                                                    @p_CEP= {DF.CEP[i]},
                                                    @p_resideExterior= {DF.RESIDE_EXTERIOR[i]},
                                                    @p_tipoEndereco= '{DF.TP_ENDERECO[i]}',
                                                    @p_CPF= {DF.CPF[i]},
                                                    @p_CNS= {DF.CNS[i]},
                                                    @p_NOME= '{DF.NOME[i]}',
                                                    @p_SEXO= '{DF.SEXO[i]}',
                                                    @p_dataNascimento= '{DF.DT_NASCIMENTO[i]}',
                                                    @p_nomeMae= '{DF.NOME_MAE[i]}',
                                                    @p_ccoBeneficiarioTitular= {DF.CCO_BENEFICIARIO_TITULAR[i]},
                                                    @p_cnpjEmpresaContratante= {DF.CNPJ_EMPRESA_CONTRATANTE[i]},
                                                    @p_codigoBeneficiario= '{DF.CD_BENEFICIARIO[i]}',
                                                    @p_dataCancelamento= '{DF.DT_CANCELAMENTO[i]}',
                                                    @p_datacontratacao= '{DF.DT_CONTRATACAO[i]}',
                                                    @p_itensExcluidosCobertura= '{DF.ITENS_EXCLUIDOS_COBERTURA[i]}',
                                                    @p_motivoCancelamento= {DF.MTV_CANCELAMENTO[i]},
                                                    @p_numeroPlanoANS= {DF.NR_PLANO_ANS[i]},
                                                    @p_relacaoDependencia= {DF.REL_DEPEND[i]},
                                                    @p_COMPETENCIA= '{DF.COMPETENCIA[i]}' ''')
                
                db.execute(SQL)
            SendMail().sendMail(DF) #Send mail
        except Exception as e:
            competencia = self.check_competencia(path)[1]
            status = 3 #error processing the file ANS 
            log.insert_log_error(str(e), 'insert_table_beneficiarioans')
            db.rollback()
        finally:    
            self.update_status_processing(status, competencia)
            db.commit()
            db.__disconnect__()


    def update_status_processing(self, status, competencia):
        SQL = (f'''UPDATE BASICUS_TESTE.DBO.Processar_Arquivo_Importacao_ANS
                    SET situacao = {status}
                WHERE COMPETENCIA =  RIGHT(CONVERT(VARCHAR(10), CONVERT(DATE, '{competencia}'), 103), 7) ''')
        db.execute(SQL)


    def DoStart(self, path):
        try:
            self.downloadFile()
            if self.check_competencia(path)[0] is not None:
                if self.check_competencia(path)[0].empty:                    
                    self.insert_table_beneficiarioans(self.read_data_excel(path), path)
                    self.remove_file_xlsx(path)
                else:
                    print('Competência já existe!')
                    self.remove_file_xlsx(path) #Delete if existis competência in directory 
            else:
                print('Não tem arquivo para processamento!')
            
            
        except Exception as e:
            log.insert_log_error(str(e), 'DoStart')



