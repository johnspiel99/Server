Python 3.11.0 (main, Oct 24 2022, 18:13:38) [MSC v.1933 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

======== RESTART: C:\Users\njuej\OneDrive\Desktop\mytest\test_server.py ========
Enter the file path: C:\Users\njuej\OneDrive\Desktop\mytest\200k.txt
Server listening on 127.0.0.1:8082
Client Sockets: [<socket.socket fd=820, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082)>]
New connection from 127.0.0.1:50551
Client Sockets: [<socket.socket fd=820, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082)>, <socket.socket fd=796, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 50551)>]
New connection from 127.0.0.1:50552
DEBUG: Received data from ('127.0.0.1', 50551): GET / HTTP/1.1
Host: 127.0.0.1:8082
Connection: keep-alive
Cache-Control: max-age=0
sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9


DEBUG: Query: GET / HTTP/1.1
Host: 127.0.0.1:8082
Connection: keep-alive
Cache-Control: max-age=0
sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9

, IP: ('127.0.0.1', 50551), Execution Time: 0.000962s, Timestamp: 2023-06-20 07:35:17Client Sockets:
 [<socket.socket fd=820, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082)>, <socket.socket fd=796, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 50551)>, <socket.socket fd=732, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 50552)>]
Client Sockets:Client ('127.0.0.1', 50551) disconnected 
[<socket.socket fd=820, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082)>, <socket.socket fd=796, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 50551)>, <socket.socket fd=732, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 50552)>]
Client ('127.0.0.1', 50552) disconnectedClient Sockets:
 [<socket.socket fd=820, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082)>]
New connection from 127.0.0.1:50556
Client Sockets: [<socket.socket fd=820, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082)>, <socket.socket fd=776, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 50556)>]
New connection from 127.0.0.1:50557
Client Sockets: [<socket.socket fd=820, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082)>, <socket.socket fd=776, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 50556)>, <socket.socket fd=804, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 50557)>]DEBUG: Received data from ('127.0.0.1', 50557): GET / HTTP/1.1
Host: 127.0.0.1:8082
Connection: keep-alive
Cache-Control: max-age=0
sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9



DEBUG: Query: GET / HTTP/1.1
Host: 127.0.0.1:8082
Connection: keep-alive
Cache-Control: max-age=0
sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9

, IP: ('127.0.0.1', 50557), Execution Time: 0.001982s, Timestamp: 2023-06-20 07:35:47Client Sockets:
 Client ('127.0.0.1', 50557) disconnected[<socket.socket fd=820, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082)>, <socket.socket fd=776, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 50556)>, <socket.socket fd=804, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 50557)>]

Client ('127.0.0.1', 50556) disconnectedClient Sockets:
 [<socket.socket fd=820, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082)>]
New connection from 127.0.0.1:50563
Client Sockets: [<socket.socket fd=820, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082)>, <socket.socket fd=784, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 50563)>]
New connection from 127.0.0.1:50564
Client Sockets: DEBUG: Received data from ('127.0.0.1', 50564): GET / HTTP/1.1
Host: 127.0.0.1:8082
Connection: keep-alive
Cache-Control: max-age=0
sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9

[<socket.socket fd=820, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082)>, <socket.socket fd=784, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 50563)>, <socket.socket fd=748, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 50564)>]

DEBUG: Query: GET / HTTP/1.1
Host: 127.0.0.1:8082
Connection: keep-alive
Cache-Control: max-age=0
sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9

, IP: ('127.0.0.1', 50564), Execution Time: 0.001014s, Timestamp: 2023-06-20 07:36:47Client Sockets:
 Client ('127.0.0.1', 50564) disconnected[<socket.socket fd=820, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082)>, <socket.socket fd=784, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 50563)>, <socket.socket fd=748, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082), raddr=('127.0.0.1', 50564)>]

Client ('127.0.0.1', 50563) disconnectedClient Sockets:
 [<socket.socket fd=820, family=2, type=1, proto=0, laddr=('127.0.0.1', 8082)>]
