#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import subprocess
import paho.mqtt.client as paho
 
def on_connect(client, userdata, flags, rc):
	print("CONNACK received with code %d." % (rc))
 



def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))



class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):

	client = paho.Client()
	client.on_connect = on_connect
	client.username_pw_set("wqberakn", "8zk2BfULr4y2")
	client.connect("m20.cloudmqtt.com", 19737)

	client.on_subscribe = on_subscribe
	client.on_message = on_message

	client.subscribe("curial", qos=1)
	
	client.loop_forever()
	
	ret =subprocess.check_output(['ansiweather','-l' , 'Paris,FR']) 
	temp = ret.split(" ")[6]
	isRaining =0  
	temp = temp + " C"

	if  ret.split(" ")[8] == u"\u2602" : 
		isRaining = 1 
		temp = temp + ",Pluie Prevue"
	else: 
		isRaining = 0

	print isRaining




        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("../../../fonts/6x10.bdf")

        red = graphics.Color(255, 0, 0)
        #graphics.DrawLine(canvas, 5, 5, 22, 13, red)

        green = graphics.Color(0, 255, 0)
        #graphics.DrawCircle(canvas, 15, 15, 10, green)

        blue = graphics.Color(0, 0, 255)
        graphics.DrawText(canvas, font, 0, 8, blue, temp)


	if  ret.split(" ")[8] == u"\u2602" : 
                isRaining = 1 
                temp = temp + ",Pluie Prevue"
		graphics.DrawText(canvas, font, 0, 16, blue, "Pluie")
        else: 
                isRaining = 0
        print isRaining



        time.sleep(10)   # show display for 10 seconds before exit


# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
