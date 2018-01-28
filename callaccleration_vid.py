from acclerationtoposition import acc2pos
import serial
import time
import sys
from visual import *
import numpy as np
import matplotlib.pyplot as plt


class runacc():

	def __init__(self):

		arduino = serial.Serial('com3', 9600,timeout=5)
		self.ard = arduino
		self.ball = sphere(pos=(0,0,0), color=color.red,radius=2)
		self.i=0
		#plt.axis([0,200,-7,15])
		#plt.ion()

		#floor = box(length=2, height=0.5, width=2, color=color.blue)

		while 1:
			#self.i = self.i +1
			self.readardunio()
			#plt.pause(0.05)

	def readardunio(self):
		time.sleep(.1)
		self.ardtalk = self.ard.readline()
		print(self.ardtalk)
		xpos = self.ardtalk.find('x') + 1 
		ypos = self.ardtalk.find('y') + 1
		zpos = self.ardtalk.find('z') + 1
		tpos = self.ardtalk.find('t') + 1
		apos = self.ardtalk.find('a') + 1 
		bpos = self.ardtalk.find('b') + 1
		cpos = self.ardtalk.find('c') + 1
		kpos = self.ardtalk.find('k') + 1

		try:
			xvalue2 = self.ardtalk[xpos:ypos-1]
			yvalue2= self.ardtalk[ypos:zpos-1]
			zvalue2 = self.ardtalk[zpos:apos-1]
			print(xvalue2)
			print(yvalue2)
			print(zvalue2)
			#plt.scatter(self.i,xvalue2)
			self.visualizedata(float(xvalue2),float(yvalue2),float(zvalue2))
		except:
			print('didntwork')


	def visualizedata(self,x,y,z):
		rate(1000)
		self.ball.pos = (x,y,z)
		print(str(self.ball.pos))


if __name__ == '__main__':
	main = runacc()
	main.ard.close()
