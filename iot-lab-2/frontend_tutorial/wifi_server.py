import socket

HOST = "192.168.3.113" # IP address of your Raspberry PI
PORT = 8081         # Port to listen on (non-privileged ports are > 1023)
import picar_4wd
import binascii
from gpiozero import CPUTemperature
def move(s):
    power = 20
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
        return s
    return ""



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
                st = move(st)
                temp = str(CPUTemperature().temperature)
                dist = str(picar_4wd.get_distance_at(90))
                list_data=[]
                list_data.append(st)
                list_data.append(temp)
                list_data.append(dist)
                to_ret = ",".join(list_data)
                data = bytes(to_ret,'UTF-8')
                client.sendall(data)
    except: 
        print("Closing socket")
        client.close()
        s.close()    