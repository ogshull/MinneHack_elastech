#class to convert 3 axis linear accleration into 3 axis position vector



class acc2pos():

	def __init__(self):

		#create empty array
		self.acc = []
		self.vel = []
		self.pos = []
		self.i=0

		#initial values zero
		self.acc.append(0)
		self.vel.append(0)
		self.pos.append(0)
		#self.i.append(0)

		#get linear accleration
		

	def convert(self,linearaccleration):
		acc = linearaccleration
		newvel = self.vel[self.i] + acc
		self.newpos = self.pos[self.i] + newvel

		self.acc.append(linearaccleration)
		self.vel.append(newvel)
		self.pos.append(self.newpos)

		self.i = self.i + 1

	def readardunio(self):
		time.sleep(.001)
		self.ardtalk = arduino.read(arduino.inWaiting())
		print(self.ardtalk)
		xpos = self.ardtalk.find('x') + 1 
		ypos = self.ardtalk.find('y') + 1
		zpos = self.ardtalk.find('z') + 1

		#position = self.ardtalk[xpos]
		print(self.ardtalk.find('x'))
		print xpos
		#print(position)

				

	def callarduino(self):
		sendtext = " givemedata"
		self.ard.flush()
		self.ard.write(sendtext)
		print("Ard sent" + sendtext)
		self.listen()

	def listen(self):
		time.sleep(1)
		dataleft = self.ard.inWaiting()
		print(dataleft)
		self.ardtalk = self.ard.read(dataleft)
		print(len(self.ardtalk))
		print("Ard recieved" + str(self.ardtalk))
		xpos = self.ardtalk.find('x') + 1 
		ypos = self.ardtalk.find('y') + 1
		zpos = self.ardtalk.find('z') + 1
		#position = self.ardtalk[xpos]
		#print xpos


	def readardunio(self):
		time.sleep(.2)
		self.ardtalk = arduino.read(size=1)
		print self.ardtalk
		xpos = self.ardtalk.find('x') + 1 
		ypos = self.ardtalk.find('y') + 1
		zpos = self.ardtalk.find('z') + 1

		#position = self.ardtalk[xpos]
		print(self.ardtalk.find('x'))
		print xpos
		#print(position)


	def getposition(self,arduinoout):
		accleration = [1,2,3]
		x = acc2pos()
		x.convert(accleration[0])
		print(x.newpos)

		y = acc2pos()
		y.convert(accleration[1])
		print(y.newpos)

		z = acc2pos()
		z.convert(accleration[2])
		print(z.newpos)


