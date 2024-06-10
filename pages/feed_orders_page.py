from pages.base_page import BasePage
import locators.feed_orders_page_locators
import allure


class FeedOrders(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @allure.step("Ожидаем кликабельности по номеру последнего заказа")
    def wait_clickable_last_order(self):
        return self.wait_clickable_element(
            locators.feed_orders_page_locators.LAST_ORDER
        )

    @allure.step("Кликаем по последнему заказу")
    def click_last_order(self):
        button = self.find_elements(locators.feed_orders_page_locators.LAST_ORDER)[0]
        button.click()

    @allure.step("Получаем текст заказов, которые в работе и последние готовые")
    def get_orders_list(self):
        order_list = self.find_element(locators.feed_orders_page_locators.ORDERS_LIST)
        return order_list.text

    @allure.step("Получаем кол-во заказов выполненных за сегодня")
    def get_quantity_counter_completed_today(self):
        quantity = self.find_elements(
            locators.feed_orders_page_locators.COUNTER_COMPLETED_FOR_TODAY
        )[1]
        return quantity.text

    @allure.step("Получаем кол-во заказов выполненных за все время")
    def get_quantity_counter_completed_all_time(self):
        quantity = self.find_elements(
            locators.feed_orders_page_locators.COUNTER_COMPLETED_FOR_ALL_TIME
        )[0]
        return quantity.text

    @allure.step("Ожидаем видимости счетчика заказов выполненных за сегодня")
    def wait_visibility_counter_completed_today(self):
        return self.wait_visibility_element(
            locators.feed_orders_page_locators.COUNTER_COMPLETED_FOR_TODAY
        )

    @allure.step("Проверяем наличие открытого окна с инфо о заказе")
    def get_availability_active_info_order_window(self):
        element = self.find_elements(
            locators.feed_orders_page_locators.CLOSE_ORDER_INFO_BUTTON
        )[1]
        if element.is_displayed():
            return True
        else:
            return False

    @allure.step("Ожидаем видимости номера заказа в окне информации о заказе")
    def wait_visibility_order_number_in_info_window(self):
        return self.wait_visibility_element(
            locators.feed_orders_page_locators.ORDER_NUMBER_IN_INFO_WINDOW
        )

    @allure.step("Получаем номер последнего заказа в Работе")
    def get_list_orders_in_work(self):
        list_orders = self.find_element(
            locators.feed_orders_page_locators.IN_WORK_CHAPTER
        )
        return list_orders.text

    @allure.step("Ожидаем появления номера заказа в Работе")
    def wait_visibility_order_number_in_work(self):
        return self.wait_visibility_element(
            locators.feed_orders_page_locators.ORDER_IN_WORK
        )
