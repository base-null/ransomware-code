import socket

def check():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect(('sock.io',80))
        s.close()
    except:
        print("No Hay conexion")
        exit()

if __name__ == '__main__':
    check()