from presenter.IntegrationPresenter import IntegrationPresenter
from model.MessageBroker import MessageBroker
from model.Component import Component
from view.ConsoleView import ConsoleView

if __name__ == "__main__":
    # Создание компонентов MVP
    broker = MessageBroker()
    view = ConsoleView()
    presenter = IntegrationPresenter(broker, view)

    # Создание компонентов системы
    component_a = Component(broker)
    component_b = Component(broker)

    # Подписка компонентов на события
    presenter.subscribe_component("event_type_1", component_a)
    presenter.subscribe_component("event_type_1", component_b)

    # Отправка сообщения
    presenter.send_message("event_type_1", "Hello, World!")
