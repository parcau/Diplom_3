import data
import allure
import stellar_burgers_api
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_cabinet_page import PersonalCabinet
from helper import UserFactory


class TestPersonalCabinet:
    @allure.title("Проверяем переход в Личный кабинет")
    @allure.description(
        "Нажимаем кнопку Личный кабинет, проверяем, что открылась страница с авторизацией"
    )
    def test_personal_cabinet_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_personal_cabinet_button()
        login_page = LoginPage(driver)
        login_page.wait_visibility_enter_button()

        assert login_page.get_current_url() == data.Urls.LOGIN_PAGE

    @allure.title("Проверяем переход в раздел История заказов")
    @allure.description(
        "Создаем нового пользователя, авторизируемся, переходим в Личный кабинет, проверяем что переход в Историю заказов работает"
    )
    def test_step_to_orders_history(self, driver):
        new_user = UserFactory.generate_new_user()
        auth_user = stellar_burgers_api.CreateUserApi.create_user(new_user)
        email = new_user["email"]
        password = new_user["password"]
        main_page = MainPage(driver)
        main_page.click_enter_account_button()
        login_page = LoginPage(driver)
        login_page.set_email(email)
        login_page.set_password(password)
        login_page.click_enter_button()
        main_page.click_personal_cabinet_button()
        personal_cabinet = PersonalCabinet(driver)
        personal_cabinet.wait_visibility_orders_history_button()
        personal_cabinet.click_orders_history_buttons()
        token = auth_user.json()["accessToken"]
        stellar_burgers_api.DeleteUserApi.delete_user(token)

        assert personal_cabinet.get_current_url() == data.Urls.ORDERS_HISTORY_PAGE

    @allure.title("Проверяем выход из личного кабинета")
    @allure.description(
        "Создаем нового пользователя, авторизуемся, переходим в Личный кабинете, проверяем при нажаьии на кнопку Выход попадем на страницу авторизации"
    )
    def test_quit_from_account(self, driver):
        new_user = UserFactory.generate_new_user()
        auth_user = stellar_burgers_api.CreateUserApi.create_user(new_user)
        email = new_user["email"]
        password = new_user["password"]
        main_page = MainPage(driver)
        main_page.click_enter_account_button()
        login_page = LoginPage(driver)
        login_page.set_email(email)
        login_page.set_password(password)
        login_page.click_enter_button()
        main_page.click_personal_cabinet_button()
        personal_cabinet = PersonalCabinet(driver)
        personal_cabinet.wait_visibility_orders_history_button()
        personal_cabinet.click_quit_button()
        token = auth_user.json()["accessToken"]
        stellar_burgers_api.DeleteUserApi.delete_user(token)

        assert login_page.get_current_url() == data.Urls.LOGIN_PAGE
