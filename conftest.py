import pytest
import data
from selenium import webdriver
from faker import Faker


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefpx":
        driver = webdriver.Firefox()

    driver.get(data.Urls.STELLAR_BURGERS)
    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def new_user():
    fake = Faker()
    email = fake.email()
    password = fake.password()
    name = fake.name()
    payload = {"email": email, "password": password, "name": name}
    return payload
