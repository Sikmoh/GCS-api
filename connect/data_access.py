from dronelib.server import gcs


class ConnectDacc:

    @staticmethod
    def connect(connect):
        gcs.create_socket()
        gcs.accept_conn(connect)
        #gcs.transform_ip()
        return 'command sent'


