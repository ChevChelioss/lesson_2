
import pytest
from selene.support.shared import browser


@pytest.fixture(scope='package')
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture()
def browser_open(browser_size):
    browser.open('https://google.com/ncr')