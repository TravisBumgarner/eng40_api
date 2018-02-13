from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    link = models.ManyToManyField("Link", blank=True)
    def __unicode__(self):
       return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
       return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Image(models.Model):
    name = models.CharField(max_length=200)
    external_src = models.URLField(blank=True)
    local_src = models.ImageField(blank=True)
    camera = models.CharField(max_length=200, blank=True)
    exposure = models.CharField(max_length=200, blank=True)

    # def clean(self):
    # TODO How to handle both types of src?

    def __unicode__(self):
       return self.name


class Link(models.Model):
    name = models.CharField(max_length=200)
    src = models.URLField(blank=True)
    image = models.OneToOneField(
        Image,
        blank=True,
        on_delete=models.CASCADE
    )

    def __unicode__(self):
       return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField("Category", blank=True)
    description = models.TextField(blank=True)
    link = models.ManyToManyField("Link", blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    skill = models.ManyToManyField("Skill", blank=True)
    tool = models.ManyToManyField("Tool", blank=True)
    image = models.ManyToManyField("Image", blank=True)
    video = models.ManyToManyField("Video", blank=True)

    def __unicode__(self):
       return self.name


class Skill(models.Model):
    choices = [
        ("novice", "Novice"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
        ("expert", "Expert")
    ]

    name = models.CharField(max_length=200, )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    rating = models.CharField(max_length=50, choices=choices)

    def __unicode__(self):
       return self.name


class Tool(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField("Category", blank=True)
    
    def __unicode__(self):
       return self.name


class Video(models.Model):
    name = models.CharField(max_length=200)
    src = models.URLField()

    def __unicode__(self):
       return self.name



