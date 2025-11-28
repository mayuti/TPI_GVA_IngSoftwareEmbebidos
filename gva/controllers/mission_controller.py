from entities.mission import Mission
from entities.vehicle_state import VehicleState
from controllers.motor_controller import MotorController

class MissionController:
    """
    Orquestador principal de la HU GVA-U02.
    Maneja creación, inicio y monitoreo de una misión.
    """

    def __init__(self):
        self.vehicle_state = VehicleState()
        self.motor_controller = MotorController()
        self.current_mission = None

    def start_mission(self, mission_id: str, target_station: str):
        self.current_mission = Mission(mission_id, target_station)
        self.current_mission.start()
        self.vehicle_state.set_mode("MOVING")

        # Ordena movimiento
        self.motor_controller.move_to(target_station)

        return {
            "mission": self.current_mission,
            "vehicle_state": self.vehicle_state
        }

    def notify_station_arrival(self):
        self.vehicle_state.set_mode("ARRIVED")

        if self.current_mission:
            self.current_mission.complete()

        return {
            "mission": self.current_mission,
            "vehicle_state": self.vehicle_state
        }
