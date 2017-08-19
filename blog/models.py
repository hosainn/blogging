from django.db import models
from organizer.models import Tag, Department
from django.core.urlresolvers import reverse
# Create your models here.
#################

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63,
                            help_text='A label for url config',
                            unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField('date published',
                                auto_now_add=True)
    tags = models.ManyToManyField(Tag,
                                blank=True,
                                 related_name='blog_posts')
    departments = models.ManyToManyField(Department,
                                         blank=True,
                                         related_name='blog_posts')


    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date','title']
        get_latest_by = 'pub_date'



    def __str__(self):
        return '{} on {}'.format(
            self.title,
            self.pub_date.strftime('%Y-%m-%d'))

    def get_absolute_url(self):
        return reverse('blog_post_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('blog_post_update', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('blog_post_delete',kwargs={'slug':self.slug})
