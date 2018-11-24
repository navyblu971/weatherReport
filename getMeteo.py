from gpiozero import LED
from time import sleep


import subprocess
ret =subprocess.check_output(['ansiweather','-l' , 'Paris,FR']) 
temp = int(ret.split(" ")[6]) 



red = LED(17)

while temp > 0:
    red.on()
    sleep(1)
    red.off()
    sleep(1)
    temp = temp-1



