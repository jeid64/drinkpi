import socket

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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(OPCODE_SERVER_LOGIN + ' ' + PASSWD + '\n')
data = s.recv(1024)
s.close()
print 'Recieved ', repr(data)
