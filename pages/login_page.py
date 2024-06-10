import allure
from pages.base_page import BasePage
import locators.login_page_locators


class LoginPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @allure.step("Кликаем по кнопке Восстановить пароль")
    def click_password_recovery_button(self):
        button = self.find_element(
            locators.login_page_locators.PASSWORD_RECOVERY_BUTTON
        )
        button.click()

    @allure.step("Ожидаем наличия кнопки Войти")
    def wait_visibility_enter_button(self):
        return self.wait_visibility_element(locators.login_page_locators.ENTER_BUTTON)

    @allure.step("Получаем текущий url страницы")
    def get_current_url(self):
        return self.current_url()

    @allure.step("Вводим email")
    def set_email(self, email):
        email_input = self.find_element(locators.login_page_locators.EMAIL_FIELD)
        email_input.send_keys(email)

    @allure.step("Вводим пароль")
    def set_password(self, password):
        password_input = self.find_element(locators.login_page_locators.PASSWORD_FIELD)
        password_input.send_keys(password)

    @allure.step("Кликаем по кнопке Войти")
    def click_enter_button(self):
        button = self.find_element(locators.login_page_locators.ENTER_BUTTON)
        button.click()
