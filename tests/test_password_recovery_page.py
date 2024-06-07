import allure
import data
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecovery


class TestPasswordRecovery:
    @allure.step("Проверяем работоспособность конопки Восстановить пароль")
    @allure.description(
        "Нажимаем кнопку Войти в аккаунт, нажимаем кнопку Восстановить пароль, проверяем, что перешли на странцу восстановления пароля"
    )
    def test_password_recovery_button(self, driver):
        main_page = MainPage(driver)
        main_page.wait_clickable_enter_in_account_button()
        main_page.click_enter_account_button()
        login_page = LoginPage(driver)
        login_page.click_password_recovery_button()
        password_recovery_page = PasswordRecovery(driver)
        password_recovery_page.wait_visibility_recovery_button()

        assert password_recovery_page.current_url() == data.Urls.FORGOT_PASSWORD_PAGE

    @allure.step(
        "Проверяем работоспособность кнопки Восстановить на странице восстановления пароля"
    )
    @allure.description(
        "Нажимаем кнопку Восстановить пароль, вводим email, нажимаем Восстановить, проверяем, что перешли на страницу сброса пароля"
    )
    def test_recovery_button(self, driver):
        main_page = MainPage(driver)
        main_page.wait_clickable_enter_in_account_button()
        main_page.click_enter_account_button()
        login_page = LoginPage(driver)
        login_page.click_password_recovery_button()
        password_recovery_page = PasswordRecovery(driver)
        password_recovery_page.set_email_field()
        password_recovery_page.click_recovery_button()
        password_recovery_page.wait_visibility_save_button()

        assert password_recovery_page.current_url() == data.Urls.RESET_PASSWORD_PAGE

    @allure.step("Проверяем, что клик по кнопке показать/скрыть пароль работает")
    @allure.description(
        "В форме восстановления пароля, нажимаем на кнопку показать/скрыть пароль. Проверяем, что поле становится активным и подсвечиватеся"
    )
    def test_show_hide_password_button(self, driver):
        main_page = MainPage(driver)
        main_page.wait_clickable_enter_in_account_button()
        main_page.click_enter_account_button()
        login_page = LoginPage(driver)
        login_page.click_password_recovery_button()
        password_recovery_page = PasswordRecovery(driver)
        password_recovery_page.set_email_field()
        password_recovery_page.click_recovery_button()
        password_recovery_page.wait_visibility_save_button()
        password_recovery_page.set_new_password()
        password_recovery_page.click_show_hide_pass_button()
        highlighted_field = password_recovery_page.get_parent_class_password_field()
        parent_class = password_recovery_page.assign_parent_class_password_by_variable()

        assert highlighted_field == parent_class
