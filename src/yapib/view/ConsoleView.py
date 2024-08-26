class ConsoleView:
    def show_menu(self):
        self.display_message(message="\nMenu:")
        self.display_message(message="1. Send Message")
        self.display_message(message="2. Add Subscriber")
        self.display_message(message="3. Remove Subscriber")
        self.display_message(message="4. View Subscribers")
        self.display_message(message="5. View Component Status")
        self.display_message(message="6. Save State")
        self.display_message(message="7. Load State")
        self.display_message(message="8. Exit")

    def get_user_input(self, prompt):
        return input(prompt)
   
    def display_message(self, message):
        print(message)

    def display_published_message(self, event_type, message):
        self.display_message(message=f"\nMessage Published - {event_type}: {message}")

    def display_subscribers(self, subscribers):
        self.display_message(message="\nCurrent Subscribers:")
        for event_type, subs in subscribers.items():
            self.display_message(message=f"Event Type: {event_type}")
            for sub in subs:
                self.display_message(message=f"  - {sub.name}")

    def display_component_status(self, component):
        status = component.get_status()
        self.display_message(message=f"\nComponent '{status['name']}' Status:")
        self.display_message(message=f"  - Received Messages: {status['received_messages']}")

    def show_goodbye(self):
        self.display_message(message="Exiting the program. Goodbye!")