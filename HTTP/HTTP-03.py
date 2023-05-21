import socket
import ssl

hostname = 'www.its.ac.id'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())

        request_header = 'GET / HTTP/1.0\r\nHost: ' + hostname + '\r\n' +  '\r\n\r\n'
        request_header = request_header.encode()

        ssock.send(request_header)

        response = b'' 
        while True:
            received = ssock.recv(1024)
            if not received:
                break
            response += received
           
        header, content = response.split(bytes('\r\n\r\n', 'utf-8'), 1)
        header = header.decode()

        print(header)