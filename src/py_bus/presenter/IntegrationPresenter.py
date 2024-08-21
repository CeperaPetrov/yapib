class IntegrationPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def subscribe_component(self, event_type, component):
        self.model.subscribe(event_type, component)

    def send_message(self, event_type, data):
        self.model.publish(event_type, data)
        self.view.display_message(event_type, data)