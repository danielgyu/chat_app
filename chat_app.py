import datetime, socket

TIME = datetime.datetime.now().strftime("%H:%M:%S")


def create_socket():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return my_socket

def choose():
    decision = input('Server or Client? ')
    return decision

def input_questions():
    ip = input('Enter IP Address: ')
    port = int(input('Enter port num: '))
    return ip, port

def bind(ip, port, my_socket):
    return my_socket.bind((ip, port))

def connect(ip, port, my_socket):
    return my_socket.connect((ip, port))

def send_message(sending_socket, msg):
    msg = msg + '\n'
    data = msg.encode()
    sending_socket.send(data)

if __name__ == '__main__':
    decision  = choose()
    ip, port  = input_questions()
    my_socket = create_socket()
    if decision == 'Server':
        my_socket.bind((ip, port))
    else:
        my_socket.connect((ip, port))
        print(f'connection success, {my_socket}')

    socket_open = True

    if decision == 'Server':
        my_socket.listen()
        print('waiting for connection')
        connection_socket, address = my_socket.accept()
        print(f'connection accepted: {connection_socket}, {address}')

        while socket_open:
            message = input(f'{TIME}, {address}: ')
            if message == 'quit':
                socket_open = False
            send_message(connection_socket, message)

            data = connection_socket.recv(514)
            print(data.decode())

    elif decision == 'Client':
        while socket_open:
            data = my_socket.recv(514)
            print(data.decode())

            message = input(f'{TIME}, {my_socket.getsockname}: ')
            if message == 'quit':
                socket_open = False
            my_socket.send(message.encode())

        connection_socket.close()
        my_socket.close()
        my_socket.close()
