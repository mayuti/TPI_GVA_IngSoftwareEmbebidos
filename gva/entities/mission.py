class Mission:
    def __init__(self, mission_id: str, target_station: str, status: str = "PENDING"):
        self.mission_id = mission_id
        self.target_station = target_station
        self.status = status  # PENDING, IN_PROGRESS, COMPLETED, FAILED

    def start(self):
        self.status = "IN_PROGRESS"

    def complete(self):
        self.status = "COMPLETED"

    def fail(self):
        self.status = "FAILED"

    def __repr__(self):
        return f"<Mission id={self.mission_id} target={self.target_station} status={self.status}>"
