from pages.home_page import HomePage
from utils.base_template import TestTemplate


class TestHomePage(TestTemplate):
    title = 'AngularJS — Superheroic JavaScript MVW Framework'

    def test_page_load(self):
        home_page = HomePage(self.driver)
        home_page.go_to()
        self.assertTrue(home_page.check_page_loaded())
        current_title = home_page.get_title()
        assert self.title == current_title, 'Current title %s, should be equal to %s' % (current_title, self.title)
        home_page.set_name('almeid')
