from presenter.IntegrationPresenter import IntegrationPresenter
from model.MessageBroker import MessageBroker
from model.Component import Component
from view.ConsoleView import ConsoleView
from Application import Application

def main():
    broker = MessageBroker()
    view = ConsoleView()
    presenter = IntegrationPresenter(broker, view)
    app = Application(presenter, view)
    app.run()


if __name__ == "__main__":
    main()