from selenium.webdriver.common.by import By

ENTER_ACCOUNT_BUTTON = (
    By.XPATH,
    "//button [@class= 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']",
)
PERSONAL_CABINET_BUTTON = (By.XPATH, "//a[contains(@href,'/account')]")
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(.,'Конструктор')]")
ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(.,'Лента Заказов')]")
FLUORESCENT_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
SAUCE_BUTTON = (By.XPATH, "//span[contains(.,'Соусы')]")
ACTIVE_INGREDIENT = (By.XPATH, "//h2[contains(.,'Детали ингредиента')]")
CLOSE_SUCCESS_ORDER_WINDOW_BUTTON = (
    By.CSS_SELECTOR,
    "[class= 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']",
)
CLOSE_INFO_BUTTON = (
    By.XPATH,
    "//button [@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK' and @type= 'button']",
)
ADD_TO_ORDER_FIELD = (By.XPATH, "//img[contains(@alt,'Перетяните булочку сюда (низ)')]")
COUNTER_FLUORESCENT_BUN = (By.CSS_SELECTOR, "[class= 'counter_counter__num__3nue1']")
CREATE_ORDER_BUTTON = (By.XPATH, "//button[contains(.,'Оформить заказ')]")
SUCCESSFUL_REGISTRATION = (By.XPATH, "//p[contains(.,'Ваш заказ начали готовить')]")
NEW_ORDER_NUMBER = (
    By.XPATH,
    "//h2[contains(@class,'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]",
)
CHECK_MARK = (By.XPATH, "//img [@class= 'Modal_modal__image__2nh17']")
LOADING_IMG_ORDER_FORMATION = (By.CSS_SELECTOR, ".Modal_modal__loading__3534A")
