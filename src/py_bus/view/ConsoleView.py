class ConsoleView:
    def display_message(self, event_type, data):
        print(f"\nMessage Published - {event_type}: {data}")

    def show_menu(self):
        print("\nMenu:")
        print("1. Send Message")
        print("2. Add Subscriber")
        print("3. Remove Subscriber")
        print("4. View Subscribers")
        print("5. View Component Status")
        print("6. Exit")

    def get_user_input(self, prompt):
        return input(prompt)

    def display_subscribers(self, subscribers):
        print("\nCurrent Subscribers:")
        for event_type, subs in subscribers.items():
            print(f"Event Type: {event_type}")
            for sub in subs:
                print(f"  - {sub.name}")

    def display_component_status(self, component):
        status = component.get_status()
        print(f"\nComponent '{status['name']}' Status:")
        print(f"  - Received Messages: {status['received_messages']}")

    def show_goodbye(self):
        print("Exiting the program. Goodbye!")