from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TensorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tensor.ru/"
        self.sila_v_lyudyakh = (By.XPATH, "//div[contains(text(), 'Сила в людях')]")
        self.more_details = (By.LINK_TEXT, "Подробнее")
        self.about_page_header = (By.XPATH, "//h1[text()='О компании']")
        self.works_section_images = (By.CSS_SELECTOR, ".works-section img")

    def is_sila_v_lyudyakh_present(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.sila_v_lyudyakh)
        )

    def click_more_details(self):
        self.driver.find_element(*self.more_details).click()

    def is_about_page_opened(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.about_page_header)
        )

    def get_works_section_images(self):
        return self.driver.find_elements(*self.works_section_images)
