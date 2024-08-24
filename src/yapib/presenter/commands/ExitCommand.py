from .Command import Command


class ExitCommand(Command):
    def __init__(self, presenter):
        self.presenter = presenter

    def execute(self):
        self.presenter.view.show_goodbye()
        exit()
