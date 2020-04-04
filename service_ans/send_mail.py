import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config_db import Config


class SendMail:
    def mountHtmlMail(self, DF):
            TEXT = """
                <!DOCTYPE html>
                        <html>
                        
                        <head>
                        <style>
                        #titulo {
                            font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
                        }
                        #ANS {
                        font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
                        border-collapse: collapse;
                        width: 50%;
                        }

                        #ANS td, #ANS th {
                        border: 1px solid #ddd;
                        padding: 8px;
                        }

                        #ANS tr:nth-child(even){background-color: #f2f2f2;}

                        #ANS tr:hover {background-color: #ddd;}

                        #ANS th {
                        padding-top: 12px;
                        padding-bottom: 12px;
                        text-align: left;
                        background-color: #4CAF50;
                        color: white;
                        }
                        </style>
                        </head>
                        <body>
                        <H1 id="titulo">Processamento Arquivo ANS</H1>
                        <table id="ANS">
                        <tr style="background-color: blue;color: white;">
                            <th>COMPETÊNCIA</th>
                            <th>LINHAS PROCESSADAS</th>
                            
                        </tr>
                        <tr>
                            <td>"""+str(DF['COMPETENCIA'].values[0])+"""</td>
                            <td>"""+str(DF.shape[0])+"""</td>
                            
                        </tr>
                       
                        </table>

                        </body>
                        </html>



            """
            return TEXT


    def sendMail(self, DF):
        try: 
            print('Enviando email...!')
            ME = Config.ME
            TO = Config.TO

            #Cria um container de menssagem
            msg = MIMEMultipart('alternative')
            msg['Subject'] = "PROCESSAMENTO ARQUIVO ANS"
            msg['From'] = ME
            msg['To'] = TO

            header = "PROCESSAMENTO ARQUIVO ANS"
            # Cria o titulo e corpo HTML
            TITLE = MIMEText(header, 'plain')
            BODY = MIMEText(SendMail().mountHtmlMail(DF), 'html')

            msg.attach(TITLE)
            msg.attach(BODY)
            # Servidor de envio de email
            #mail = smtplib.SMTP('172.18.88.33', 25) 
            mail = smtplib.SMTP(Config.host_mail, Config.port_mail)

            mail.ehlo()
            mail.starttls()
            mail.mail(ME)
            mail.login('valclemor@gmail.com', 'heller123')
            mail.sendmail(ME, TO, msg.as_string())
            mail.quit()

        except Exception as e:
            print(e)

