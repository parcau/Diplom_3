import pytest
import data
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()

    driver.get(data.Urls.STELLAR_BURGERS)
    yield driver

    driver.quit()
