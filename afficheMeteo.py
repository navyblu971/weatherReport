#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import subprocess

class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):

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
