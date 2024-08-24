# Интеграционная шина YAPIB
Проект YAPIB - yet another python integration bus.
## Установка и запуск

```python src/yapib/main.py```


## Описание функций меню пользовательского интерфейса

1. Send Message: Пользователь может отправить сообщение, указав тип события и данные сообщения.

2. Add Subscriber: Пользователь может добавить новый компонент, подписав его на определённый тип события.

3. Remove Subscriber: Пользователь может удалить ранее добавленный компонент.

4. View Subscribers: Отображение всех текущих подписчиков для различных типов событий.

5. View Component Status: Позволяет пользователю запросить состояние компонента по имени. Отобразит количество полученных сообщений.

6. Exit: Выход из программы.


## Описание архитектуры проекта
Проект интеграционной шины с использование шаблона MVP (Model-View-Presenter).
Для реализации проекта, также применяются шаблоны проектирования:

1. Observer

    Применение: Взаимодействие между MessageBroker и подписчиками (Component) организовано по паттерну Observer.
   
    Описание: Паттерн Observer описывает отношение "один ко многим", где один объект (в данном случае MessageBroker) уведомляет множество подписчиков (Component) о наступлении определённого события. В нашем случае подписчики регистрируются на определённый тип событий, и при публикации сообщения всем подписанным компонентам отправляется уведомление.

2. Publisher-Subscriber

    Применение: Весь механизм подписки на события и отправки сообщений можно рассматривать как реализацию паттерна Publisher-Subscriber.
   
    Описание: Этот паттерн обеспечивает асинхронную передачу сообщений от издателя (в нашем случае, компонента, отправляющего сообщение) к подписчикам (другим компонентам, которые на это событие подписаны) через промежуточный объект (MessageBroker). Это позволяет издателям и подписчикам оставаться независимыми друг от друга.

3. Facade

    Применение: IntegrationPresenter может рассматриваться как Facade, предоставляющий упрощённый интерфейс для взаимодействия с моделью и представлением.
   
    Описание: Паттерн Facade предоставляет унифицированный интерфейс для взаимодействия с подсистемой, скрывая её сложность. В данном случае IntegrationPresenter скрывает внутреннюю логику подписки и отправки сообщений, предоставляя простой интерфейс для пользователя (через меню).

4. Command

    Применение: Для реализации меню и возможности выполнения сложных действий, применен паттерн Command.
    
    Описание: Паттерн Command инкапсулирует запрос как объект, позволяя параметризовать объекты различными запросами, выполнять отложенные операции и поддерживать отмену операций. Например, команды для добавления/удаления подписчиков.