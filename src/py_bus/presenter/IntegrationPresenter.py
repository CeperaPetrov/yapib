from model.Component import Component


class IntegrationPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_user_input("Choose an option: ")

            if choice == '1':
                event_type = self.view.get_user_input("Enter event type: ")
                data = self.view.get_user_input("Enter message data: ")
                self.send_message(event_type, data)
            elif choice == '2':
                event_type = self.view.get_user_input("Enter event type to subscribe: ")
                component_name = self.view.get_user_input("Enter component name: ")
                component = Component(self.model)
                self.subscribe_component(event_type, component)
                print(f"Component '{component_name}' subscribed to '{event_type}'")
            elif choice == '3':
                print("Removing subscribers not implemented yet.")
                # Logic to remove subscribers can be added here
            elif choice == '4':
                self.view.display_subscribers(self.model.subscribers)
            elif choice == '5':
                self.view.show_goodbye()
                break
            else:
                print("Invalid choice. Please try again.")

    def subscribe_component(self, event_type, component):
        self.model.subscribe(event_type, component)

    def send_message(self, event_type, data):
        self.model.publish(event_type, data)
        self.view.display_message(event_type, data)
