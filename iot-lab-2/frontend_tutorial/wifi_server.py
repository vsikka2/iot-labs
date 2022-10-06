import socket

HOST = "192.168.3.113" # IP address of your Raspberry PI
PORT = 8080          # Port to listen on (non-privileged ports are > 1023)
import picar_4wd
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    try:
        while 1:
            client, clientInfo = s.accept()
            print("server recv from: ", clientInfo)
            data = client.recv(1024)      # receive 1024 Bytes of message in binary format
            if data != b"":
                if(data == "b'87\r\n"):
                    print("hi")
                    picar_4wd.forward(30)
                    sleep(2)
                    picar_4wd.stop()
                print(data)
                client.sendall(data) # Echo back to client
    except: 
        print("Closing socket")
        client.close()
        s.close()    