import pytest
import allure
from pages.login_page import LoginPage

# 1. ПОЗИТИВНЫЙ ТЕСТ (только для тех, кто ДОЛЖЕН войти)
@allure.feature("Логин")
@allure.story("Успешный вход")
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),  # locked_out_user мы убрали отсюда!
])
def test_successful_login(driver, username, password):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login(username, password)
    
    assert "inventory" in driver.current_url, f"Пользователь {username} не смог войти"

# 2. НЕГАТИВНЫЙ ТЕСТ (проверяем, что заблокированного НЕ пускает и показывает ошибку)
@allure.feature("Логин")
@allure.story("Блокировка пользователя")
def test_locked_out_user(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    
    login_page.login("locked_out_user", "secret_sauce")
    
    error_text = login_page.get_error_message() 
    
    assert "Sorry, this user has been locked out" in error_text