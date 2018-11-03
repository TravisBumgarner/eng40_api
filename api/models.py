from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ManyToManyField("Category", blank=True)
    organization = models.ManyToManyField("Organization", blank=True)
    preview_img = models.OneToOneField("Image", blank=True, on_delete=models.CASCADE, null=True, related_name="preview_img")
    headline = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    skill = models.ManyToManyField("Skill", blank=True)
    location = models.ManyToManyField("Location", blank=True)

    def __unicode__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=200)
    src = models.ImageField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, related_name='image')

    def __unicode__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.OneToOneField("Image", on_delete=models.CASCADE, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    email = models.EmailField()
    message = models.TextField(max_length=2500)


class Keyword(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Keyword'


class Link(models.Model):
    name = models.CharField(max_length=200)
    src = models.URLField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, related_name='link')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True, related_name='link')

    def __unicode__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=200, unique=True)
    keyword = models.ManyToManyField("Keyword", blank=True)
    preview_img = models.OneToOneField("Image", on_delete=models.CASCADE, blank=True, null=True)
    headline = models.TextField(blank=True, null=True)
    created_date = models.DateField(null=True)

    def __unicode__(self):
        return self.name


