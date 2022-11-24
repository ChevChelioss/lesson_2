from selene.support.shared import browser
from selene import be, have


def test_search_selene_positive(browser_open):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('#search').should(have.text('Selene - Wikipedia'))
    pass


def test_search_selene_negative(browser_open):
    browser.element('[name="q"]').should(be.blank).type('dckdnvfvfdv').press_enter()
    browser.element('#search').should(have.text('Selene - Wikipedia'))
    pass

