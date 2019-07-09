#!/usr/bin/python3
import socket

def recv():
    global conn
    return conn.recv(1024**2).decode()

def send(s):
    global conn
    snd = b''
    for i in s:
        snd += i.encode()
    conn.send(snd)

ans = input('1 -- run server, other -- connect')
if ans == '1':
    sock = socket.socket()
    sock.bind(("0.0.0.0", '17000'))
    sock.listen(1)
    conn, addr = sock.accept()
    name2 = recv()
    print(f'New connection from {name2} ({addr[0]})')
    send(name)
    while True:
        send(input(name + ": "))
        print(name2 + ": " + recv())