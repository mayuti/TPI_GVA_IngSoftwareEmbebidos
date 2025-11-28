class MotorController:
    """
    Controlador responsable de enviar comandos al subsistema de movimiento.
    La implementación interna no es requerida.
    """

    def move_to(self, station_id: str):
        # Simulación / placeholder
        print(f"[MotorController] Moviendo al vehículo hacia estación {station_id}")

    def stop(self):
        print("[MotorController] Vehículo detenido")
