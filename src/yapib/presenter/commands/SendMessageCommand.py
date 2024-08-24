from .Command import Command

class SendMessageCommand(Command):
    def __init__(self, presenter):
        self.presenter = presenter

    def execute(self):
        event_type = self.presenter.view.get_user_input("Enter event type: ")
        data = self.presenter.view.get_user_input("Enter message data: ")
        self.presenter.send_message(event_type, data)
