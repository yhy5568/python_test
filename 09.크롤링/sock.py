import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
google_ip = socket.gethostbyname("google.com")
sock.connect((google_ip, 80))

sock.send("GET / HTTP/1.1\n".encode())
sock.send("\n".encode())

buffer = sock.recv(4096)
buffer = buffer.decode().replace("\r\n", "\n")
sock.close()

print(buffer)
'''
HTTP/1.1 200 OK
Date: Wed, 14 Sep 2022 05:01:20 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2022-09-14-05; expires=Fri, 14-Oct-2022 05:01:20 GMT; path=/; domain=.google.com; Secure
Set-Cookie: AEC=AakniGP72EM9sNX9H37BstA9oBSJ6OmzlqqQcXJX6jHdsU6g8uC-kR1wzQ; expires=Mon, 13-Mar-2023 05:01:20 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=lax
Set-Cookie: NID=511=bzvo3P3wha5HepOIztLOg9X49Bri8YYzxuIlapYGsiV_8kwVTfOYgooSV3vqh9BVxYC5lpbOJ8JYU5Zv0BEAmtycHWzE-qdQW4etkVtNFnWfCEJfaJeYHLlF8UDDt5_hHWz0691H47cnNFCaQka6kF-58qnOBFsZfLAhezYZ21s; expires=Thu, 16-Mar-2023 05:01:20 GMT; path=/; domain=.google.com; HttpOnly
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

6383
'''