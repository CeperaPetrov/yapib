from model.Component import Component


class IntegrationPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.components = {}

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
                component = Component(self.model, component_name)
                self.subscribe_component(event_type, component)
                self.components[component_name] = component
                print(f"Component '{component_name}' subscribed to '{event_type}'")
            elif choice == '3':
                event_type = self.view.get_user_input("Enter event type to unsubscribe: ")
                component_name = self.view.get_user_input("Enter component name: ")
                if component_name in self.components:
                    component = self.components[component_name]
                    if self.model.unsubscribe(event_type, component):
                        print(f"Component '{component_name}' unsubscribed from '{event_type}'")
                    else:
                        print(f"Component '{component_name}' was not subscribed to '{event_type}'")
                else:
                    print(f"Component '{component_name}' does not exist.")
            elif choice == '4':
                self.view.display_subscribers(self.model.subscribers)
            elif choice == '5':
                component_name = self.view.get_user_input("Enter component name to view status: ")
                if component_name in self.components:
                    component = self.components[component_name]
                    self.view.display_component_status(component)
                else:
                    print(f"Component '{component_name}' does not exist.")
            elif choice == '6':
                self.view.show_goodbye()
                break
            else:
                print("Invalid choice. Please try again.")

    def subscribe_component(self, event_type, component):
        self.model.subscribe(event_type, component)

    def send_message(self, event_type, data):
        self.model.publish(event_type, data)
        self.view.display_message(event_type, data)