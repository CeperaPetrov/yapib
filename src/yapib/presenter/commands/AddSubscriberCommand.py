from model.Component import Component
from .Command import Command

class AddSubscriberCommand(Command):
    def __init__(self, presenter):
        self.presenter = presenter

    def execute(self):
        event_type = self.presenter.view.get_user_input("Enter event type to subscribe: ")
        component_name = self.presenter.view.get_user_input("Enter component name: ")
        component = Component(self.presenter.model, component_name)
        self.presenter.subscribe_component(event_type, component)
        self.presenter.components[component_name] = component
        print(f"Component '{component_name}' subscribed to '{event_type}'")
