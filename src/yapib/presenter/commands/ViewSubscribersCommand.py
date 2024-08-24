from .Command import Command

class ViewSubscribersCommand(Command):
    def __init__(self, presenter):
        self.presenter = presenter

    def execute(self):
        self.presenter.view.display_subscribers(self.presenter.model.subscribers)
