from django.test import TestCase ,Client
from django.urls import reverse

class PostsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        response = self.client.get(reverse("Hello-view"))
        expected_data = "Hello"
        self.assertEqual(expected_data, response.content.decode())
        self.assertEqual(500, response.status_code)
        self.assertEqual(response['Name'], 'Alex')

    def test_contacts(self):
        response = self.client.get(reverse("Contacts-view"))
        expected_data= "Number"
        self.assertEqual(expected_data,response.content.decode())


    def test_about(self):
        response = self.client.get(reverse("About-view"))
        expected_data= "About"
        self.assertEqual(expected_data,response.content.decode())
    # def test_test_page(self):
    #     response = self.client.get(reverse("test-page"))
    #     expected_data = "Test"
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.content.decode(), expected_data)
    #     print(response)