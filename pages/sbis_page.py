from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

class SbisPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://sbis.ru/"
        self.contacts_link = (By.LINK_TEXT, "Контакты")
        self.tensor_banner = (By.XPATH, "//a[contains(@href, 'tensor.ru')]")

    def open(self):
        self.driver.get(self.url)

    def go_to_contacts(self):
        attempts = 0
        while attempts < 3:
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.contacts_link)
                ).click()
                print("Clicked on 'Контакты'")
                return
            except StaleElementReferenceException:
                attempts += 1
                print("StaleElementReferenceException: Retry clicking 'Контакты'")

    def click_tensor_banner(self):
        try:
            # Проверка наличия баннера
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.tensor_banner)
            )
            print("Tensor banner found.")
            attempts = 0
            while attempts < 3:
                try:
                    tensor_element = self.driver.find_element(*self.tensor_banner)
                    WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(tensor_element)
                    ).click()
                    print("Clicked on tensor banner.")
                    # Явное ожидание нового URL
                    WebDriverWait(self.driver, 10).until(
                        EC.url_contains("tensor.ru")
                    )
                    return
                except StaleElementReferenceException:
                    attempts += 1
                    print("StaleElementReferenceException: Retry clicking 'Тензор'")
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(self.tensor_banner)
                    )
        except TimeoutException:
            print("TimeoutException: Не удалось найти или кликнуть на баннер 'Тензор'.")
            print(f"Current URL after timeout: {self.driver.current_url}")
            self.driver.save_screenshot('screenshot.png')  # Сохранение скриншота

