class Station:
    def __init__(self, station_id: str, sensor_status: str = "UNKNOWN"):
        self.station_id = station_id
        self.sensor_status = sensor_status  # OK, ERROR, UNKNOWN

    def update_sensor_status(self, new_status: str):
        self.sensor_status = new_status

    def __repr__(self):
        return f"<Station id={self.station_id} sensor_status={self.sensor_status}>"
