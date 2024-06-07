import allure
import locators.personal_cabinet_page_locators
from pages.base_page import BasePage


class PersonalCabinet(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @allure.step("Кликаем по кнопке История заказов")
    def click_orders_history_buttons(self):
        button = self.find_element(
            locators.personal_cabinet_page_locators.ORDERS_HISTORY_BUTTON
        )
        button.click()

    @allure.step("Ожидаем наличие кнопки История заказов")
    def wait_visibility_orders_history_button(self):
        return self.wait_visibility_element(
            locators.personal_cabinet_page_locators.ORDERS_HISTORY_BUTTON
        )

    @allure.step("Получаем текущий url страницы")
    def get_current_url(self):
        return self.current_url()

    @allure.step("Кликаем по кнопке Выход")
    def click_quit_button(self):
        button = self.find_element(locators.personal_cabinet_page_locators.QUIT_BUTTON)
        button.click()

    @allure.step("Получаем номер последнего заказа в Истории заказов")
    def get_number_last_order(self):
        last_order_number = self.find_elements(
            locators.personal_cabinet_page_locators.LAST_ORDER_NUMBER
        )[0]
        return last_order_number.text

    @allure.step("Ожидаем, когда прогрузbтся cписок заказов")
    def wait_load_orders_list(self):
        return self.wait_visibility_element(
            locators.personal_cabinet_page_locators.LAST_ORDER_NUMBER
        )
