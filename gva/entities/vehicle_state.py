class VehicleState:
    def __init__(self, mode: str = "IDLE", battery_level: float = 100.0):
        self.mode = mode           # IDLE, MOVING, ARRIVED, ERROR
        self.battery_level = battery_level

    def set_mode(self, mode: str):
        self.mode = mode

    def __repr__(self):
        return f"<VehicleState mode={self.mode} battery={self.battery_level}>"
