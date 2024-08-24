from .Command import Command


class RemoveSubscriberCommand(Command):
    def __init__(self, presenter):
        self.presenter = presenter

    def execute(self):
        event_type = self.presenter.view.get_user_input("Enter event type to unsubscribe: ")
        component_name = self.presenter.view.get_user_input("Enter component name: ")
        if component_name in self.presenter.components:
            component = self.presenter.components[component_name]
            if self.presenter.model.unsubscribe(event_type, component):
                print(f"Component '{component_name}' unsubscribed from '{event_type}'")
            else:
                print(f"Component '{component_name}' was not subscribed to '{event_type}'")
        else:
            print(f"Component '{component_name}' does not exist.")
