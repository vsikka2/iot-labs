import socket

HOST = "192.168.3.113" # IP address of your Raspberry PI
PORT = 8080          # Port to listen on (non-privileged ports are > 1023)
import picar_4wd
from gpiozero import CPUTemperature
def move(s):
    power = 20
    print(s)
    if("87" in s):
        picar_4wd.forward(power)
    elif("83" in s):
        picar_4wd.backward(power)
    elif("65" in s):
        picar_4wd.turn_left(power)
    elif("68" in s):
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
                move(st)
                temp = CPUTemperature()
                to_ret = bin(temp)
                client.sendall(to_ret) 
                # temp = CPUTemperature()
                # dist = picar_4wd.get_distance_at(90)
                # list_data=[]
                # list_data.append(st)
                # list_data.append(temp.temperature)
                # list_data.append(dist)
                # to_ret = ",".join(list_data)
                # to_ret = bin(to_ret)
                # client.sendall(to_ret) # Echo back to client
    except: 
        print("Closing socket")
        client.close()
        s.close()    