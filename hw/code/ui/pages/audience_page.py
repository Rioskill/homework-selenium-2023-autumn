import time
from ui.pages.hq_page import HqPage
from ui.locators import basic_locators
from ui.wait_conditions import element_stops_moving


def keywords_payload(name='Название', keywords='образование', days='15'):
    return {
        'name': name,
        'keywords': keywords,
        'days': days
    }


class AudiencePage(HqPage):
    url = 'https://ads.vk.com/hq/audience'
    locators = basic_locators.AudiencePageLocators

    KEYWORDS = 'Ключевые фразы'

    def create_audience(self, name, source=KEYWORDS, data={}):
        self.set_audience_name(name)
        self.add_source(source, data)
        self.save_audience()

    def save_audience(self):
        self.click(self.locators.SAVE_AUDIENCE, cond=element_stops_moving)

    def add_source(self, source=KEYWORDS, data={}):
        self.click(self.locators.BY_TEXT('Добавить источник'),
                   cond=element_stops_moving)
        self.click(self.locators.BY_TEXT(source))

        if (source == self.KEYWORDS):
            self.add_keywords(data)

    def delete_audience(self, name):
        menu = self.locators.AUDIENCE_DETAILS(name)
        self.hover(menu)
        self.click(menu)
        self.click(self.locators.BY_TEXT('Удалить'))
        self.click(self.locators.BY_TEXT('Удалить'))

    def open_edit_modal(self, name):
        menu = self.locators.AUDIENCE_DETAILS(name)
        self.hover(menu)
        self.click(menu)
        self.click(self.locators.BY_TEXT('Редактировать'))

    def set_audience_name(self, name):
        self.click(self.locators.CREATE_AUDIENCE)
        self.fill_in(self.locators.AUDIENCE_NAME, name)

    def add_keywords(self, data):
        self.fill_in(self.locators.SOURCE_NAME, data['name'])
        self.fill_in(self.locators.KEYWORDS, data['keywords'])

        self.clear(self.locators.DAYS_INPUT)
        self.fill_in(self.locators.DAYS_INPUT, data['days'])

        self.click(self.locators.SAVE_SOURCE)

    def has_long_name_error(self):
        self.has_error(self.locators.AUDIENCE_NAME,
                       'Максимальная длина 255 символов')

    def get_source(self, id, type='keyword'):
        source = self.find(self.locators.AUDIENCE_SOURCE(id))
        name = self.find_from(source, self.locators.AUDIENCE_SOURCE_NAME)
        items = self.find_multiple_from(
            source, self.locators.AUDIENCE_SOURCE_ITEM)
        if type == 'keyword':
            return keywords_payload(name=name.text, keywords=items[0].text, days=items[1].text.split(' ')[0])

    def get_rule(self):
        return self.find(self.locators.RULE).text.lower()

    def set_rule(self, rule):
        self.click(self.locators.RULE_SELECTOR, cond=element_stops_moving)
        if rule == 'или':
            self.click(self.locators.BY_TEXT('хотя бы одному из условий'))
        elif rule == 'и':
            self.click(self.locators.BY_TEXT('всем условиям'))
        elif rule == 'не':
            self.click(self.locators.BY_TEXT('ни одному из условий'))
