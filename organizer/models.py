from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=31,
                            unique=True,)
    slug = models.SlugField(max_length=31,
                            unique=True,
                            help_text='A label for url config')

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name.title()



class Department(models.Model):
    name = models.CharField(max_length=31,
                            db_index=True)
    slug = models.SlugField(max_length=31,
                            unique=True,
                            help_text='a label for url config')
    description = models.TextField()
    founded_date = models.DateField('date founded')
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag,
                                  blank=True)


    class Meta:
        ordering = ['name']
        get_latest_by = ['founded_date']


    def __str__(self):
        return self.name

class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=255)
    department = models.ForeignKey(Department)



    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'
        unique_together = ('slug','department')


    def __str__(self):
        return '{}: {}'.format(self.department,
                               self.title)


