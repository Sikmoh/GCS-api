from dronelib.server import gcs


class SelectDacc:

    @staticmethod
    def select(drone_id, cmd):
        gcs.get_target(drone_id, cmd)
        return 'command sent'


