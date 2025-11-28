class CommandProcessor:
    """
    Interpreta comandos entrantes desde el sistema de supervisión.
    Para esta HU: procesar comando 'INICIAR_MISION'.
    """

    def process_start_mission(self, mission_controller, mission_id: str, target_station: str):
        return mission_controller.start_mission(mission_id, target_station)
