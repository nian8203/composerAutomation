# composerAutomation

crontab -e //agrega un cronjob a la lista de tareas a ejecutar
[Minute] [Hour(0-23)] [Day(0-7)] [Month(1-12)] [Day of week (0 =sunday to 6 =saturday)] [Command] //formato para ejecutar tarea
ej = Supongamos que queremos ejecutar un script cada 20 minutos:
*/20 * * * * /path/to/command
*/5 //ej cada 5 minutos

============script===================
tiempo=$(date +"%Y-%m-%d:%H:%M:%S).log
free > $tiempo
=====================================

sudo service cron restart //reiniciar crontab
2-10 //para ejecuutar la instruccion del minuto 2 al 10 
chmod +x script.sh //darle permisos al script para ejecutar
tail script.sh //revisar las ultimas lineas del archivo

ej. console 
    nano script.sh //crear un ejecutable
    chmod +x script.sh //dar permisos execute
    sh script.sh //ejecutar script para ver resultado de prueba
    tail ramlog.txt //mirar ultimas lineas de archivo
    pwd //mirar ruta archivo
    crontab -e //configurar el tiempo de ejecucion
    min hour * * * cd /home/nian/Documentos/composerAutomation && sh script.sh //configurar la tarea

==========================formato ejecucion crontab====================================
36 09 * * * cd  /home/nian/Documentos/composerAutomation/ && python3.11 pruebaLoad.py
