# Python Selenium Framework 

Фреймворк для автоматизации UI-тестов на Python с использованием Selenium, Pytest и Allure.

##  Стек технологий
- **Python 3.14**
- **Selenium WebDriver**
- **Pytest** (фикстуры, параметризация)
- **Allure** (отчеты, скриншоты)
- **Page Object Model (POM)**

##  Структура проекта
```text
├── pages/               # Page Object Model (классы страниц)
│   └── login_page.py    # Страница логина
├── tests/               # Автотесты
│   └── test_login.py    # Тесты авторизации
├── conftest.py          # Фикстуры (драйвер, скриншоты)
├── requirements.txt     # Зависимости
└── README.md            # Документация