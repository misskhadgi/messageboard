from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='a test')

    def test_post_create(self):
        post = Post.objects.get(id=1)
        expected_output = f'{post.text}'
        self.assertEqual(expected_output, 'a test')


class HomePageViewTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
