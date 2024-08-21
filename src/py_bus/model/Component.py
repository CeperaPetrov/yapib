class Component:
    def __init__(self, broker):
        self.broker = broker

    def send_message(self, event_type, data):
        self.broker.publish(event_type, data)

    def receive(self, event_type, data):
        print(f"Component received {event_type}: {data}")