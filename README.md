# Serviço De Importação ANS 
O serviço consiste em fazer a importação do arquivo de beneficiários ANS

# Começando
O serviço funciona tanto em sistemas Windows, quanto em sistemas Unix.

# Pre-requisitos
Os pacotes necessários para o funcionamento adequado do serviço são:

    python: apt-get install python3 --ubuntu  yum install python3 #Para dist baseadas em red hat 
    pandas: pip install pandas 
    pymssql: pip install pymssql
Caso prefira usar o virtualenv, então: 

    pip3 install virtualenv 
Criar ambiente virtual:

    virtualenv -p python3 venv 

# IMPORTANTE 
 O nome de todos os arquivos .xslx devem está no seguinte formato, exemplo:
 
      ARQ_CONF_ANS_2020_01
      No exexmplo acima, o arquivo é da competência de janeiro, ficando então: ARQ_CONF_ANS_2020_01
      
 Editar o arquivo "config.json" para atender as configurações de autênticação de banco de dados, ftp e e-mail.

Autores
José Valclemir Rodrigues Da Silva 
Gabriel Yan Nobre Ricarte
