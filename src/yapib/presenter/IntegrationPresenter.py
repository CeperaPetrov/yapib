from .commands.SendMessageCommand import SendMessageCommand
from .commands.AddSubscriberCommand import AddSubscriberCommand
from .commands.RemoveSubscriberCommand import RemoveSubscriberCommand
from .commands.ViewSubscribersCommand import ViewSubscribersCommand
from .commands.ViewComponentStatusCommand import ViewComponentStatusCommand
from .commands.ExitCommand import ExitCommand
from .commands.SaveStateCommand import SaveStateCommand
from .commands.LoadStateCommand import LoadStateCommand

class IntegrationPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.components = {}
        self.commands = {
            '1': SendMessageCommand(self),
            '2': AddSubscriberCommand(self),
            '3': RemoveSubscriberCommand(self),
            '4': ViewSubscribersCommand(self),
            '5': ViewComponentStatusCommand(self),
            '6': SaveStateCommand(self),
            '7': LoadStateCommand(self),
            '8': ExitCommand(self),
        }

    def handle_user_choice(self, choice):
        command = self.commands.get(choice)
        if command:
            command.execute()
        else:
            self.view.display_message(message="Invalid choice. Please try again.")
            
    def subscribe_component(self, event_type, component):
        self.model.subscribe(event_type, component)

    def send_message(self, event_type, data):
        self.model.publish(event_type, data)
        self.view.display_published_message(event_type, data)