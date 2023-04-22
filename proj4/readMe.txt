CSDS 425 Networking project 4

Xiao Wang

Environment:
    requests
How to install:
    pip install requests

Running usage:
    python server.py
    python client.py [HTTP URL]
    e.g. python client.py http://engineering.case.edu/eecs

Run the server first, then the client

The data get from the server by proxy is stored in text.txt
The data get directly from the server by wget is stored in eecs.txt (http://engineering.case.edu/eecs)

Using:
    diff eesc.txt text.txt
can compare the output

There maybe errors like address used, if that happens, change the port number in server.py and client.py if possible
