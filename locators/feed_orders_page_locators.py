from selenium.webdriver.common.by import By

LAST_ORDER = (By.XPATH, "//p [@class= 'text text_type_digits-default']")
ORDERS_LIST = (By.XPATH, "//ul [@class= 'OrderFeed_list__OLh59']")
COUNTER_COMPLETED_FOR_TODAY = (
    By.XPATH,
    "//p [@class= 'OrderFeed_number__2MbrQ text text_type_digits-large']",
)
COUNTER_COMPLETED_FOR_ALL_TIME = (
    By.XPATH,
    "//p [@class= 'OrderFeed_number__2MbrQ text text_type_digits-large']",
)
CLOSE_ORDER_INFO_BUTTON = (
    By.XPATH,
    "//button [@class= 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK' and @type= 'button']",
)
ORDER_NUMBER_IN_INFO_WINDOW = (
    By.XPATH,
    "//p [@class= 'text text_type_digits-default mb-10 mt-5']",
)
IN_WORK_CHAPTER = (
    By.XPATH,
    "//ul [@class= 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']",
)
ORDER_IN_WORK = (
    By.XPATH,
    "(//li[contains(@class, 'text text_type_digits-default mb-2')])[6][1]",
)
