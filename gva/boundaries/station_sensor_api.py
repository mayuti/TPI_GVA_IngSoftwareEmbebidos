class StationSensorAPI:
    """
    Representa un boundary con los sensores de estación.
    Esta HU recibe un evento de llegada desde esta pieza.
    """

    def notify_arrival(self, mission_controller):
        return mission_controller.notify_station_arrival()
