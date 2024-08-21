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