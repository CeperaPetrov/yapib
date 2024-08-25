from .Command import Command

class SaveStateCommand(Command):
    def __init__(self, presenter):
        self.presenter = presenter

    def execute(self):
        filename = self.presenter.view.get_user_input("Enter filename to save state [broker_state.pkl]: ")
        if filename == '':
            filename = 'broker_state.pkl'
        self.presenter.model.save_state(filename)
        self.presenter.view.display_message(message="State saved successfully.")
