from controllers.command_processor import CommandProcessor
from controllers.mission_controller import MissionController
from boundaries.supervision_system_api import SupervisionSystemAPI
from boundaries.station_sensor_api import StationSensorAPI

def main():
    mission_controller = MissionController()
    command_processor = CommandProcessor()
    supervision_api = SupervisionSystemAPI(command_processor)
    station_sensor = StationSensorAPI()

    print("=== INICIO DE MISION ===")
    result = supervision_api.iniciar_mision(
        mission_controller,
        mission_id="M001",
        target_station="ST-15"
    )
    print(result)

    print("\n=== LLEGADA A ESTACION ===")
    result = station_sensor.notify_arrival(mission_controller)
    print(result)

if __name__ == "__main__":
    main()
