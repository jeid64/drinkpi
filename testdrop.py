import time

id = '05-0000000dff61'
file = open('/sys/bus/w1/devices/' + id + '/rw', 'w')
file.write('\\' + 'x' + '55')
file.flush()
time.sleep(1)
file.write('\\' + 'x' + '55')
file.flush()
file.close()
