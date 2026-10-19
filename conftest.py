import pytest
import allure
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    
    # Этот код выполнится ПОСЛЕ теста (даже если он упал)
    # Проверяем, упал ли тест (ищем ошибку в результатах)
    if hasattr(driver, "current_url"):  # проверка, что браузер ещё жив
        # Делаем скриншот в памяти
        screenshot = driver.get_screenshot_as_png()
        
        # Прикрепляем его к отчёту Allure
        allure.attach(
            screenshot, 
            name="screenshot_on_failure", 
            attachment_type=allure.attachment_type.PNG
        )
    
    driver.quit()