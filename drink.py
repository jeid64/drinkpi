class drinkMachine():
	def __init__ (self):
		self.slots = []
		self.sensors = []
		for item in open('config/machine.config'):
			if (item[:1] == '05'):
				print 'slot made'
				self.slots.append(item)
			elif (item[:1] == '28'):
				self.sensors.append(item)
			
	def getAllStatus(self):
		outstr = ''
		for x in range(0, len(self.slots)):
			status = 0
			if (self.slots[x].getStatus()):
				status = 1
			outstr += (x + 1) + ' ' + 1
			if (x != len(self.slots) - 1):
				outstr += ' ` '
		return outstr

class slot():
	def __init__ (self, idNumber):
		self.idNumber = idNumber
		self.lock = false

	def getStatus(self):
		try:
			file = open(''.join(['/sys/bus/w1/devices/',self.idNumber,'/name']))
			file.close()
		except IOError:
			return False
		return True 
	
	def getLock(self):
		return self.lock

	def setLock(self):
		self.lock = True
	
	def setUnlock(self):
		self.lock = False
	
	def dropDrink(self):
		if (self.getStatus and not self.getLock):
			self.setLock()
			commands = ['sh', 'drop.sh', self.idNumber]
        		subprocess.call(commands)
			self.setUnlock()
			return True
		else:
			return False

class sensor():
	def __init__ (self, idNumber):
		self.idNumber = idNumber
	
	def getStatus(self):
		try:
			file = open(''.join(['/sys/bus/w1/devices/', self.idNumber, '/name']))
			file.close()
		except IOError:
			return False
		return True
	def getTemp(self):
		try:
			tempFile = open(''.join(['/sys/bus/w1/devices/', self.idNumber, '/w1_slave']))
			text = tempFile.read();
			tempFile.close()
			temperature = float(text.split('\n')[1].split(' ')[9][2:]) / 1000
		except IOError:
			return -1
		return temperature

if __name__ == '__main__':
	drinkmachine = drinkMachine()
	print (drinkmachine.getAllStatus())
	

