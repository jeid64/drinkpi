#Op Codes for tini-server communication
OPCODE_SERVER_LOGIN = '0'
OPCODE_SERVER_DROP_ACK = '4'
OPCODE_SERVER_DROP_NACK = '5'
OPCODE_SERVER_SLOT_STATUS = '7'
OPCODE_SERVER_TEMPERATURE = '8'
OPCODE_SERVER_NOOP = '9'

OPCODE_TINI_ERROR = '-1'
OPCODE_TINI_LOGIN_ACK = '1'
OPCODE_TINI_LOGIN_NACK = '2'
OPCODE_TINI_DROP = '3'
OPCODE_TINI_SLOT_STATUS = '6'


HOST = 'drinkjs.csh.rit.edu'
PORT = 4343
PASSWD = 'password'

import asyncore, socket, time
import threading
import drink
class PIClient(asyncore.dispatcher):

	def __init__(self):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect((HOST, PORT))
		self.send(OPCODE_SERVER_LOGIN + ' ' + PASSWD + '\n')
		self.buffer = OPCODE_SERVER_LOGIN + ' ' + PASSWD + '\n'
		#noopThread = self.noopThread(self)
		#noopThread.start()
		self.drinkmachine = drink.drinkMachine()
	def handle_connect(self):
		pass

	def handle_close(self):
		self.close()
	
	def commandSwitch(self,receivedBuffer):	
		if OPCODE_TINI_LOGIN_ACK in receivedBuffer:
			print 'ACK!'
		elif OPCODE_TINI_LOGIN_NACK in receivedBuffer:
			print 'NACK!'
		elif '6' in receivedBuffer:
			print 'Server wants slot info.'
			self.buffer = self.giveSlotInfo()
			self.handle_write()
		elif OPCODE_TINI_DROP in receivedBuffer:
			print 'Server wants to drop a drink.'
			self.buffer = self.dropDrink()
		else:
			print receivedBuffer
	def handle_read(self):
		buffer = self.recv(8192)
		self.commandSwitch(buffer)
        def writable(self):
		return (len(self.buffer) > 0)

	def handle_write(self):
		print 'writing ' + self.buffer
		sent = self.send(self.buffer)
		self.buffer = self.buffer[sent:]
	
	def noop(self):
		return '9\n'

	def dropDrink(self):
		return '4\n'

	def giveSlotInfo(self):
		builderString = '7 '
		statuses = self.drinkmachine.getAllStatus()
		print statuses
		builderString = ''.join([builderString, statuses, ' \n'])
		'''
			for i in range(1, numSlots):
				builderString += " " + str(i) + " " + '1'
			builderString += '\n'
		'''
		#builderString = "7 1 1 ` 2 1 ` 3 1 ` 4 1 ` 5 1 ` 6 1 \n"	
		print builderString
		return builderString

	class noopThread(threading.Thread):
		def __init__(self, piclient):
			threading.Thread.__init__(self)
			self.piclient = piclient
		def run(self):
			while(True):
				self.piclient.buffer = self.piclient.noop()
				self.piclient.handle_write()
				time.sleep(5)
client = PIClient()
asyncore.loop()
