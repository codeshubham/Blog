from unicodedata import category
from django.test import TestCase
from django.contrib.auth.models import User 
from blog.models import Post, Category 

class Test_Create_Post(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789'
        )
        test_post = Post.objects.create(category_id=1,title='Post title',excerpt='Post Excerpt',content='Post Content',slug='post-title',author_id=1,status='published')
        
    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = post.author 
        excerpt = post.excerpt
        title = post.title 
        content = post.content 
        status = post.status
        self.assertEqual(author,'test_user1')
        self.assertEqual(title,'Post title')
        self.assertEqual(content,'Post Content')
        self.assertEqual(status,'published')
        self.assertEqual(str(post),'Post Title')
        self.assertEqual(str(cat),'django')