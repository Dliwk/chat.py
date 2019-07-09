#!/usr/bin/python3
import socket

def recv():
    global conn
    return conn.recv(1024).decode()

def send(s):
    global conn
    snd = b''
    for i in s:
        try:
            snd += i.encode()
        except:
            pass
    conn.send(snd)

name = input("Your name is ")
ans = input('1 -- run server, other -- connect: ')
if ans == '1':
    print("Wait a connection...")
    sock = socket.socket()
    sock.bind(("0.0.0.0", 17000))
    sock.listen(1)
    conn, addr = sock.accept()
    name2 = recv()
    print(f'New connection from {name2} ({addr[0]})')
    send(name)
    while True:
        send(' '+input(name + ": "))
        print(name2 + ": ", end='')
        a = recv()
        if a == '':
            print("Diskonnected")
            exit(0)
        print(a)
else:
    print(f"Connecting to {ans}...")
    conn = socket.socket()
    conn.connect((ans, 17000))
    send(name)
    name2 = recv()
    print(f"Successful connect to {name2} ({ans})")
    while True:
        print(name2 + ": ", end='')
        a = recv()
        if a == '':
            print("Diskonnected")
            exit(0)
        print(a)
        send(' '+input(name + ": "))
