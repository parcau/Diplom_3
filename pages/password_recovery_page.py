import allure
from pages.base_page import BasePage
import locators.password_recovery_page_locators
import data


class PasswordRecovery(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @allure.step("Вводим почту")
    def set_email_field(self):
        email_input = self.find_element(
            locators.password_recovery_page_locators.EMAIL_FIELD
        )
        email_input.send_keys(data.RecoveryPassword.CLIENT_EMAIL)

    @allure.step("Нажимаем кнопку Восстановить")
    def click_recovery_button(self):
        button = self.find_element(
            locators.password_recovery_page_locators.RECOVERY_BUTTON
        )
        button.click()

    @allure.step("Получаем URL текущей страницы")
    def get_current_url(self):
        return self.get_current_url()

    @allure.step("Ожидаем наличия кнопки Сохранить")
    def wait_visibility_save_button(self):
        return self.wait_visibility_element(
            locators.password_recovery_page_locators.SAVE_BUTTON
        )

    @allure.step("Ожидаем наличия кнопки Восстановить")
    def wait_visibility_recovery_button(self):
        return self.wait_visibility_element(
            locators.password_recovery_page_locators.RECOVERY_BUTTON
        )

    @allure.step("Нажимаем кнопку Показать/спрятать пароль")
    def click_show_hide_pass_button(self):
        button = self.find_element(
            locators.password_recovery_page_locators.SHOW_HIDE_PASS_BUTTON
        )
        button.click()

    @allure.step("Вводим новый пароль в форме воссстановления пароля")
    def set_new_password(self):
        password_input = self.find_element(
            locators.password_recovery_page_locators.PASSWORD_FIELD
        )
        password_input.send_keys(data.RecoveryPassword.CLIENT_PASSWORD)

    @allure.step("Получаем родительский класс поля с паролем")
    def get_parent_class_password_field(self):
        return self.find_element(
            locators.password_recovery_page_locators.PASSWORD_FIELD_PARENT
        )

    @allure.step("Присваиваем переменной родительский класс поля Пароль")
    def assign_parent_class_password_by_variable(self):
        return self.find_element(
            locators.password_recovery_page_locators.HIGHLIGHTED_PASSWORD_FIELD
        )
