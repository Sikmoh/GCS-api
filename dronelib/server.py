#  Python Imports
# -------------------------------------------------
import socket
import sys
import os


#  Module Imports
# -------------------------------------------------

class ServerInit:

    def __init__(self, host: str, port: int):
        self.__host = host
        self.__port = port
        self.s = socket.socket()
        self.all_connections = []
        self.all_addresses = []
        self.new = {}

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

    def create_socket(self):
        """socket connection for main server"""
        try:
            print("Binding the port : " + " " + str(self.__port))
            self.s.bind((self.__host, self.__port))
            self.s.listen(5)

        except socket.error as msg:
            print("Socket creation error:" + str(msg))

    def accept_conn(self, drone_number: int):
        """this method creates a connection object for
        each drone that connects to the socket """
        while True:
            try:
                conn, address = self.s.accept()
                self.s.setblocking(True)  # prevents timeout

                self.all_connections.append(conn)
                self.all_addresses.append(address)

                print("Connection has been established :" + address[0])
                if len(self.all_addresses) == drone_number:
                    break

            except socket.error as msg:
                print("Error accepting connections" + str(msg))

    def transform_ip(self):
        for x in self.all_addresses:
            for i in self.all_connections:
                n, a = x
                add = n.partition('192.168.0.')[-1]
                self.new[add] = i


class RunServer(ServerInit):
    """These methods are used to run the server"""

    def send_commands(self, cmd):
        # You can only send a command to a connection
        print(cmd)
        while True:
            if cmd == 'quit':
                gcs.s.close()
            elif cmd[:3] == 'arm':
                for i in self.all_connections:
                    i.send(str.encode(cmd))
            elif cmd == 'test':
                for i in self.all_connections:
                    i.send(str.encode(cmd))
            elif cmd == 'land':
                for i in self.all_connections:
                    i.send(str.encode(cmd))
            elif cmd == 'abort':
                for i in self.all_connections:
                    i.send(str.encode(cmd))
            elif cmd == 'start':
                for i in self.all_connections:
                    i.send(str.encode(cmd))
            elif cmd == 'disarm':
                for i in self.all_connections:
                    i.send(str.encode(cmd))
            elif cmd == 'telemetry':
                for i in self.all_connections:
                    i.send(str.encode(cmd))
            else:
                pass
            break

    def get_target(self, number, cmd):
        # use this to select a target drone
        # Welcome to ALAB firefly show.Start show here: select 0 or 1...
        # Press enter to exit from target command section
        try:
            conn = self.new[f'{number}']
            # conn = self.all_connections[drone_id]
            # print("You are now connected to :" + str(self.all_addresses[drone_id][0]))
            # print(str(self.all_addresses[drone_id][0]) + ">", end="")
            conn.send(str.encode(cmd))
            print(number)
            print('sent')
            print(cmd)

        except:
            print("Selection not valid")


def create_server(host, port):
    gcs_server = RunServer(host, port)
    return gcs_server


gcs = create_server('192.168.0.100', 9999)

# code below is executed in a different script, its just here for reference
# gcs_server = create_server('127.0.0.1', 9999, 1)
# gcs_server.create_socket()
# gcs_server.accept_conn()
# gcs_server.send_commands()
