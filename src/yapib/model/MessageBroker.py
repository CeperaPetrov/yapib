import pickle

class MessageBroker:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, subscriber):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(subscriber)

    def publish(self, event_type, data):
        if event_type in self.subscribers:
            for subscriber in self.subscribers[event_type]:
                subscriber.receive(event_type, data)

    def unsubscribe(self, event_type, subscriber):
        if event_type in self.subscribers:
            if subscriber in self.subscribers[event_type]:
                self.subscribers[event_type].remove(subscriber)
                return True
        return False

    def save_state(self, filename, components):
        state = {
            'broker': self,
            'components': components
        }
        with open(filename, 'wb') as f:
            pickle.dump(state, f)

    @staticmethod
    def load_state(filename):
        try:
            with open(filename, 'rb') as f:
                state = pickle.load(f)
                broker = state['broker']
                components = state['components']
            # Восстановим ссылки на брокера в компонентах
            for event_type, comps in broker.subscribers.items():
                for component in comps:
                    component.broker = broker
            return broker, components
        except FileNotFoundError:
            return None, None