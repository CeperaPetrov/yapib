class Application:
    def __init__(self, presenter, view):
        self.presenter = presenter
        self.view = view

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_user_input("Choose an option: ")
            self.presenter.handle_user_choice(choice)