import socket

HOST = "192.168.3.113" # IP address of your Raspberry PI
PORT = 8080          # Port to listen on (non-privileged ports are > 1023)
import picar_4wd

def move(s):
    power = 20
    if(s == "87"):
        picar_4wd.forward(power)
    elif(s == "83"):
        picar_4wd.backward(power)
    elif(s == "65"):
        picar_4wd.turn_left(power)
    elif(s == "68"):
        picar_4wd.turn_right(power)
    else:
        picar_4wd.stop()
            



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    try:
        while 1:
            client, clientInfo = s.accept()
            print("server recv from: ", clientInfo)
            data = client.recv(1024)      # receive 1024 Bytes of message in binary format
            if data != b"":
                st = data.decode('ascii')
                print(st)
                client.sendall(data) # Echo back to client
    except: 
        print("Closing socket")
        client.close()
        s.close()    