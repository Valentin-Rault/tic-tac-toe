import socket
import threading

# Choosing a nickname
nickname = input('Choose your nickname: ')

# Connecting to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


# Listening to server and sending nickname
def receive():
    """Listen to server and send nickname or prints message"""
    while True:
        try:
            # Receive message from server
            # If message is NICK send nickname
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            elif message == 'Thank you for playing':
                client.close()
            else:
                print(message)
        except:
            # Close connection when error
            print('An error occurred.')
            client.close()
            break


def write():
    """Sending messages to server"""
    while True:
        message = input('')
        client.send(message.encode('utf-8'))


# Starting thread for listening and writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
