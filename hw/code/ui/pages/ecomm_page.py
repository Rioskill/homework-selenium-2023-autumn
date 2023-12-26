import time
from ui.pages.base_page import BasePage
from ui.locators.basic_locators import EcommPageLocators
from selenium.webdriver.support import expected_conditions as EC


class CreateCatalogModal:
    CATALOG_PATH = 'files/catalog_products.csv'

    def __init__(self, page):
        self.page = page
        self.locators = page.locators

    def click_feed_btn(self):
        self.page.click(self.locators.create_catalog_modal.FEED_BTN)

    def click_marketplace_btn(self):
        self.page.click(self.locators.create_catalog_modal.MARKETPLACE_BTN)

    def click_manual_btn(self):
        self.page.click(self.locators.create_catalog_modal.MANUAL_BTN)

    def is_feed_visible(self):
        return self.page.is_visible(self.locators.create_catalog_modal.FEED_LABEL)

    def is_marketplace_visible(self):
        return self.page.is_visible(
            self.locators.create_catalog_modal.MARKETPLACE_LABEL)

    def is_manual_visible(self):
        return self.page.is_visible(self.locators.create_catalog_modal.MANUAL_LABEL)

    def create_catalog_from_file(self):
        self.page.upload_file(
            self.locators.create_catalog_modal.MANUAL_FILE_SELECTOR, self.CATALOG_PATH)

        self.page.click(self.locators.create_catalog_modal.SUBMIT_CATALOG_BTN)

    def has_loading_started(self):
        self.page.wait(30).until(
            EC.visibility_of_element_located(self.locators.FEED_LOADING))
        return True

    def has_loading_finished(self):
        self.page.wait(600).until(
            EC.invisibility_of_element_located(self.locators.FEED_LOADING))
        return True


class EcommPage(BasePage):
    url = 'https://ads.vk.com/hq/ecomm/catalogs'
    locators = EcommPageLocators()

    def __init__(self, driver):
        super().__init__(driver)
        self.create_catalog_modal = CreateCatalogModal(self)

    def click_create_catalog_btn(self):
        self.click(self.locators.CREATE_CATALOG_BTN)

    def is_catalog_btn_visible(self):
        return self.is_visible(self.locators.CREATE_CATALOG_MODAL)

    def click_catalog(self):
        self.click(self.locators.CATALOG)

    def open_catalog_options(self):
        self.click(self.locators.SETTINGS_BTN)

    def is_catalog_options_modal_open(self):
        return self.is_visible(self.locators.SETTINGS_MODAL)

    def click_tab(self, tab_name):
        self.click(self.locators.SPAN_BY_TEXT(tab_name))

    def click_add_goods_btn(self):
        self.click(self.locators.ADD_GOODS_BTN)

    def click_promote_btn(self):
        self.click(self.locators.PROMOTE_BTN)
