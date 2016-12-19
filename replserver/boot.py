try:
    import usocket as socket
except:
    import socket
    
import os
    
import webrepl
webrepl.start(password='shrimping')
    
replpath = "webrepl-inlined.html.gz"

s = socket.socket()
ai = socket.getaddrinfo("0.0.0.0", 80)
addr = ai[0][-1]

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(5)

def accept_handler(sock):
	res = sock.accept()
	print("Handling")
	client_s = res[0]
	string_request = client_s.recv(2048).decode('utf-8')
	print("Request:" + string_request)
	try:
		request_line = string_request.split("\r\n")[0]    # only consider first line
		request_line = request_line.split()     # separate by whitespace 
		(request_method, path, request_version) = request_line
		header = ''
		content = ''
		if request_method == "GET" and "favicon" not in path:
			print("GET "+ path)
			header += 'HTTP/1.1 200 OK\r\n'
			header += 'Content-Type: text/html; charset=UTF-8\r\n'
			header += 'Content-Encoding: gzip\r\n'

			replsize = os.stat(replpath)[6]
			header += 'Content-Length: ' + str(replsize) + '\r\n'
			header += '\r\n'

			client_s.send(header)
			print("Sent "+ header)
			
			with open(replpath, 'r') as f:
				chunkCount = 0
				while True:
					chunk = f.read(1024)
					if chunk != '':
						client_s.write(chunk)
						print("Sent chunk " + str(chunkCount) + ":" + str(len(chunk)))
						chunkCount = chunkCount + 1
					else:
						print("Last chunk sent")
						break							
	except Exception as e:
		print("Exception", e)
	finally:
		client_s.close()

s.setsockopt(socket.SOL_SOCKET, 20, accept_handler)
