import pytest
from selenium import webdriver
from pages.sbis_page import SbisPage
from pages.tensor_page import TensorPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_tensor(driver):
    sbis_page = SbisPage(driver)
    tensor_page = TensorPage(driver)

    # Шаг 1: Перейти на https://sbis.ru/ в раздел "Контакты"
    sbis_page.open()
    sbis_page.go_to_contacts()

    # Шаг 2: Найти баннер Тензор, кликнуть по нему
    sbis_page.click_tensor_banner()

    # Шаг 3: Перейти на https://tensor.ru/
    print(f"URL after clicking tensor banner: {driver.current_url}")
    assert "tensor.ru" in driver.current_url, f"Expected URL to contain 'tensor.ru' but got {driver.current_url}"
