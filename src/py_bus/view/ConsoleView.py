class ConsoleView:
    def display_message(self, event_type, data):
        print(f"Message Published - {event_type}: {data}")