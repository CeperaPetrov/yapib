class Component:
    def __init__(self, broker, name):
        self.broker = broker
        self.name = name
        self.received_messages = 0

    def send_message(self, event_type, data):
        self.broker.publish(event_type, data)

    def receive(self, event_type, data):
        self.received_messages += 1
        print(f"Component '{self.name}' received {event_type}: {data}")

    def get_status(self):
        return {
            "name": self.name,
            "received_messages": self.received_messages
        }
        
    # Сериализации и десериализация
    # У нас есть поле broker со сылкой на MessageBroker.
    # Для предотвращения циклических зависимостий переопределим __getstate__ и __setstate__
    # где будем удалять и добавлять данные в поле broker при сериализации и десериализации 
    
    def __getstate__(self):
        # Сохраняем состояние без ссылки на брокера
        state = self.__dict__.copy()
        del state['broker']
        return state

    def __setstate__(self, state):
        # Восстанавливаем состояние и добавляем broker как None
        self.__dict__.update(state)
        # сами ссылки на объект восстанавливаются в MessageBroker
        self.broker = None  