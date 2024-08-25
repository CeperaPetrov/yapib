from .Command import Command

class LoadStateCommand(Command):
    def __init__(self, presenter):
        self.presenter = presenter

    def execute(self):
        filename = self.presenter.view.get_user_input("Enter filename to load state [broker_state.pkl]: ")        
        if filename == '':
            filename = 'broker_state.pkl'
        self.presenter.model.load_state(filename)
        self.presenter.view.display_message(message="State loaded successfully.")