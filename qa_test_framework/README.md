# Framework. Selenium WebDriver. Tools QA
## Проект по автоматизации тестирования сайта [https://demoqa.com/](https://demoqa.com/).
Использованный стек технологий: 
[Python](https://www.python.org/), 
[Selenium](https://www.selenium.dev/), 
[Pytest](https://docs.pytest.org/),
[Dynaconf](https://www.dynaconf.com/).

В проекте реализовано:
Автоматизированы тесткейсы, для проверки базовой логики на страницах:
- https://demoqa.com/alerts;
- https://demoqa.com/frames;
- https://demoqa.com/webtables;
- https://demoqa.com/browser-windows.


## Запуск тестов (команды для терминала OS Linux)
Скопировать папку с удалённого репозитория: `git clone https://github.com/tquality-education-lvl1/a.navickas.git`
Перейти в папку с проектом task3: `cd task3`
Установить зависимости: `pip install -r requirements.txt`
Запустить тесты в браузере Chrome: `pytest`
Запустить тесты в браузере Firefox: `pytest --browser_name firefox`
Журнал хода выполнения тестов доступен в папке [log](log)

## Описание проекта
Простейший фреймворк по автоматизации тестирования, который включает в себя:
1. BaseForm класс
2. BaseElement класс и его классы-наследники
3. Singleton и BrowserFactory (Factory method) для организации получения экземпляра драйвера
4. Класс для работы с браузером 
5. ConfigManager класс

