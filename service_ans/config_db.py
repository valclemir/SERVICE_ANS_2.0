import json 

class Config:

    
    with open(r'C:\Users\valclemir\Documents\Azure-estudos\ANS\service_ans\config.json', 'r') as read_json:
        config = json.load(read_json)

    # Database config
    db_host = config['db_config']['host']
    db_domain = config['db_config']['domain']
    db_user = config['db_config']['user']
    db_password = config['db_config']['password']
    db_name = config['db_config']['database']

    # Mail config 
    host_mail = config['mail_config']['host']
    port_mail = config['mail_config']['port']
    ME = config['mail_config']['ME']
    TO = config['mail_config']['TO']

    #FTP config 
    ftp_host = config['ftp_config']['host']
    ftp_user = config['ftp_config']['user']
    ftp_password = config['ftp_config']['password']
    ftp_folder = config['ftp_config']['local_folder_download']
    

    path = 'repository'



    
    
    

