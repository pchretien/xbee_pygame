
import sys
import serial

ser = serial.Serial('COM8', 19200, timeout=0)

def main():	
	buffer = ''
	while 1:	
		b = ser.read()
		while b:
			sys.stdout.write(b)
			
			if b == '>':
				print
			
			b = ser.read()
	
if __name__ == "__main__":
    main()
    
