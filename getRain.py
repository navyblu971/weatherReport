from gpiozero import LED
from time import sleep


import subprocess
ret =subprocess.check_output(['ansiweather','-l' , 'Paris,FR']) 
temp = int(ret.split(" ")[6])
isRaining =0  

if  ret.split(" ")[8] == u"\u2602" : 
	isRaining = 1 
else: 
	isRaining = 0

print isRaining
red = LED(17)


while temp > 0 & isRaining==1:
    red.on()
    sleep(1)
    red.off()
    sleep(1)
    temp = temp-1



