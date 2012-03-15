import serial
ser = serial.Serial('COM8', 19200, timeout=0)

def process(buffer):
	if len(buffer) > 0:
		print(buffer)

def main():	
	buffer = ''
	while 1:	
		b = ser.read()
		while b:
			if b == '<':
				buffer = ''
			elif b == '>':
				process(buffer)
			else:
				buffer += b		

			b = ser.read();
	
if __name__ == "__main__":
    main()
    
