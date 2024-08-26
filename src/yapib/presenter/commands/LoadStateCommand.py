from .Command import Command

class LoadStateCommand(Command):
    def __init__(self, presenter):
        self.presenter = presenter

    def execute(self):
        filename = self.presenter.view.get_user_input("Enter filename to load state [broker_state.pkl]: ")
        if filename == '':
            filename = 'broker_state.pkl'

        loaded_broker, loaded_components = self.presenter.model.load_state(filename)

        if loaded_broker is not None:
            self.presenter.model = loaded_broker
            self.presenter.components = loaded_components
            self.presenter.view.display_message(message="State loaded successfully.")
        else:
            self.presenter.view.display_message(message="Error: File not found or failed to load.")
