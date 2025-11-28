class SupervisionSystemAPI:
    """
    Boundary para recibir comandos externos desde el sistema de supervisión.
    Para esta HU: comando INICIAR_MISION.
    """

    def __init__(self, command_processor):
        self.command_processor = command_processor

    def iniciar_mision(self, mission_controller, mission_id: str, target_station: str):
        return self.command_processor.process_start_mission(
            mission_controller, mission_id, target_station
        )
