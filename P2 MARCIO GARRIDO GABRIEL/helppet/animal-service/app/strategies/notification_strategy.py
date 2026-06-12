class NotificationStrategy:

    def send(self, animal_name):
        pass


class ConsoleNotificationStrategy(NotificationStrategy):

    def send(self, animal_name):
        return f"Notificação enviada: o animal {animal_name} foi encontrado!"