from selenium import webdriver
from selenium.webdriver.common.by import By


def test_links_count():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")
    links = driver.find_elements(By.TAG_NAME, "a")
    assert len(links) == 9
    for link in links:
        assert link.is_displayed()
    assert "1" in links[0].text
    driver.quit() # Коментарий для пул реквеста
