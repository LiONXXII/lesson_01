from selenium import webdriver
from selenium.webdriver.common.by import By


BASE_URL = "https://httpbin.qa-territory.online/forms/post"


def test_form_submission():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(30)  # Ждать загрузку до 30 секунд
    driver.get(BASE_URL)

    driver.find_element(By.NAME, "custname").send_keys("Test User")
    driver.find_element(By.XPATH, "//*[contains(text(),'Submit')]").click()

    assert driver.current_url != BASE_URL

    driver.quit()
