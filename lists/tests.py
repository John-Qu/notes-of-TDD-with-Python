from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string
from lists.models import Item


# class SmokeTest(TestCase):
#
#     def test_bad_math(self):
#         self.assertEqual(1+1,3)

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = "Item the second"
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, "The first (ever) list item")
        self.assertEqual(second_saved_item.text, "Item the second")

class HomePageTest(TestCase):

    # These two test method were replaced by one with two lines.
    #
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)
    #
    # def test_home_page_returns_correct_html(self):
    #     # Replace these two lines with one line.
    #     # request = HttpRequest()
    #     # response = home_page(request)
    #     response = self.client.get('/')
    #     #
    #     html = response.content.decode('utf8')
    #     # print(repr(html)) # to check what charactors are actual in it.
    #     self.assertTrue(html.startswith('<!DOCTYPE html>\n<html'))
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.strip().endswith('</html>'))
    #     #
    #     # Replace these two lines with one line.
    #     # expected_html = render_to_string('home.html')
    #     # self.assertEqual(html, expected_html)
    #     self.assertTemplateUsed(response, 'home.html')
    #     # self.assertTemplateUsed(response, 'wrong.html') # for error messages

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

        # self.assertIn('A new list item', response.content.decode())
        # self.assertTemplateUsed(response, 'home.html')

    def test_only_saved_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


