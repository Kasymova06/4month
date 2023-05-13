from django.test import TestCase, Client
from django.urls import reverse



class BlogViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        response = self.client.get(reverse("index-page"))
        self.assertTemplateUsed(response,"posts/index.html")
        self.assertEqual(200, response.status_code)
        

    def test_about(self):
        response = self.client.get(reverse("about-page"))
        self.assertTemplateUsed(response,"posts/about.html")
        self.assertEqual(200, response.status_code)

    def test_contacts(self):
        response = self.client.get(reverse("contacts-page"))
        self.assertTemplateUsed(response,"posts/contacts.html")
        self.assertEqual(200, response.status_code)


    def test_test_page(self):
        response = self.client.get(reverse("test-page"))
        self.assertTemplateUsed(response,"posts/includes/include_text.html")
        self.assertEqual(response.status_code, 200)
        # print(response)
