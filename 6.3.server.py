import socket
import os
import sys
import shutil
import math

host=''
port=5000

s=socket.socket()
s.bind((host,port))
s.listen(2)

def multiply(x,y):
	return x*y

def divide(x,y):
	return x/y

def add(x,y):
	return x+y

def subs(x,y):
	return x-y

print('Waiting a connection . . . ')
while True:
	conn,addr = s.accept()
	print('Connection from: '+str(addr))
	client_req = conn.recv(1024)
	req_str = client_req.decode('utf-8')
	if req_str == 'multiply':
		#fill code
		no1_req = conn.recv(1024)
		number1 = no1_req.decode('utf-8')
		converted_num1 = float(number1)
		no2_req = conn.recv(1024)
		number2 = no2_req.decode('utf-8')
		converted_num2 = float(number2)

		operation = multiply(converted_num1,converted_num2)
		#print('Total: '+ str(operation))
		#total = str(operation)
		conn.send(str.encode(str(operation)))

	elif req_str == 'divide':
		#fill code
		no1_req = conn.recv(1024)
		number1 = no1_req.decode('utf-8')
		converted_num1 = float(number1)
		no2_req = conn.recv(1024)
		number2 = no2_req.decode('utf-8')
		converted_num2 = float(number2)

		operation = divide(converted_num1,converted_num2)
		conn.send(str.encode(str(operation)))

	elif req_str == 'addition':
		#fill code
		no1_req = conn.recv(1024)
		number1 = no1_req.decode('utf-8')
		converted_num1 = float(number1)
		no2_req = conn.recv(1024)
		number2 = no2_req.decode('utf-8')
		converted_num2 = float(number2)

		operation = add(converted_num1,converted_num2)
		conn.send(str.encode(str(operation)))

	elif req_str == 'substract':
		#fill code
		no1_req = conn.recv(1024)
		number1 = no1_req.decode('utf-8')
		converted_num1 = float(number1)
		no2_req = conn.recv(1024)
		number2 = no2_req.decode('utf-8')
		converted_num2 = float(number2)

		operation = subs(converted_num2,converted_num2)
		conn.send(str.encode(str(operation)))

	elif req_str == 'log':
		no1_req = conn.recv(1024)
		number1 = no1_req.decode('utf-8')
		converted_num1 = float(number1)

		operation = math.log(converted_num1)
		conn.send(str.encode(str(operation)))
	elif req_str == 'sqrt':
		no1_req = conn.recv(1024)
		number1 = no1_req.decode('utf-8')
		converted_num1 = float(number1)

		operation = math.sqrt(converted_num1)
		conn.send(str.encode(str(operation)))
	elif req_str == 'expo':
		no1_req = conn.recv(1024)
		number1 = no1_req.decode('utf-8')
		converted_num1 = float(number1)

		operation = math.exp(converted_num1)
		conn.send(str.encode(str(operation)))

	#conn.send(str.encode(str(operation)))


