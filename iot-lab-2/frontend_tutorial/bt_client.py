import bluetooth

host = "E4:5F:01:AB:68:C9" # The address of Raspberry PI Bluetooth adapter on the server.
port = 0
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))
while 1:
    text = input("Enter your message: ") # Note change to the old (Python 2) raw_input
    if text == "quit":
        break
    sock.send(text)

    data = sock.recv(1024)
    print("from server: ", data)

sock.close()


