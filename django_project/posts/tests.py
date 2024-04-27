from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
# Create your tests here.

class BlogTest(TestCase): 
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = "Frank",
            email = "Frank@gmail.com",
            password = "secret",
        )
        
        cls.post = Post.objects.create(
            author = cls.user,
            title = "First post",
            body = "Body of the post", 
        )
        
    def test_post_model(self):
        self.assertEqual(self.post.author.username, "Frank" )
        self.assertEqual(self.post.title, "First post" )
        self.assertEqual(self.post.body, "Body of the post" )
        self.assertEqual(str(self.post), "First post" )