from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.
class BlogTests(TestCase):

    def setUp(self):
        #getting user model and creting temp user and Post for database to test
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title = 'a good title',
            author = self.user,
            body = 'Nice Body content'
        )

    # testing data in title is string or not
    def test_string_representation(self):
        post = Post(title= 'a sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','a good title')
        self.assertEqual(f'{self.post.author}','testuser')
        self.assertEqual(f'{self.post.body}','Nice Body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'Nice Body content')
        self.assertTemplateUsed(response,'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/10000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response, 'a good title')
        self.assertTemplateUsed(response,'post_detail.html')
