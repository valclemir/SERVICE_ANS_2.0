FILEPY='/home/suporte/SERVICE_ANS_2.0/service_ans/controlers.py'
LOGDIR='/var/log/ANS.log'
TIMESLEEP=3600

if [[ -e $FILEPY ]]; then 
    while [[ true ]]; do
        python3 $FILEPY >> $LOGDIR;
        sleep $TIMESLEEP;
    done;
else
    echo "File not exists";
fi; 