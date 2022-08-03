from dronelib.server import gcs


class CommandDacc:

    @staticmethod
    def command(cmd):
        gcs.send_commands(cmd)
        return 'command sent'


