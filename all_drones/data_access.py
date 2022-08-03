from dronelib.server import gcs


class DroneDacc:

    @staticmethod
    def all_drones():
        drones = (len(gcs.all_connections))
        return drones

    @staticmethod
    def conn_dict():
        gcs.transform_ip()
        conn_dict = str(gcs.new)
        return conn_dict
