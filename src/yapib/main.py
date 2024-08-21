from presenter.IntegrationPresenter import IntegrationPresenter
from model.MessageBroker import MessageBroker
from model.Component import Component
from view.ConsoleView import ConsoleView

if __name__ == "__main__":
    broker = MessageBroker()
    view = ConsoleView()
    presenter = IntegrationPresenter(broker, view)

    # Запуск пользовательского интерфейса
    presenter.run()
