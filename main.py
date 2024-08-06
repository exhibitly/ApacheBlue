# In Your Project, do pip install pybluez.
import bluetooth

def scan_devices():
    print("Scanning for devices...")
    devices = bluetooth.discover_devices(lookup_names=True)
    print("Devices found:")
    for addr, name in devices:
        print(f"{addr} - {name}")

def connect_device(addr):
    print(f"Connecting to {addr}...")
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((addr, 1))
    print("Connected!")
    return sock

def send_message(sock, message):
    print(f"Sending message: {message}")
    sock.send(message.encode())
    print("Message sent!")

def main():
    scan_devices()
    addr = input("Enter the address of the device you want to connect to: ")
    sock = connect_device(addr)
    message = input("Enter the message you want to send: ")
    send_message(sock, message)
    sock.close()

if __name__ == "__main__":
    main()
