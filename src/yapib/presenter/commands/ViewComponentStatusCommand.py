from .Command import Command

class ViewComponentStatusCommand(Command):
    def __init__(self, presenter):
        self.presenter = presenter

    def execute(self):
        component_name = self.presenter.view.get_user_input("Enter component name to view status: ")
        if component_name in self.presenter.components:
            component = self.presenter.components[component_name]
            self.presenter.view.display_component_status(component)
        else:
            self.presenter.view.display_message(message=f"Component '{component_name}' does not exist.")
