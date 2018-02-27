from django.db import models


# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     link = models.ManyToManyField("Link", blank=True)
#     image = models.OneToOneField("Image", blank=True, null=True)
#
#     def __unicode__(self):
#          return self.name


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


# class Image(models.Model):
#     name = models.CharField(max_length=200)
#     src = models.ImageField(blank=True, null=True)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, related_name="image")
#
#     def __unicode__(self):
#          return self.name

class Project(models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.ManyToManyField("Category", blank=True)
    organization = models.ManyToManyField("Organization", blank=True)
    headline = models.TextField(blank=True, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    skill = models.ManyToManyField("Skill", blank=True)
    location = models.ManyToManyField("Location", blank=True)
    # video = models.ManyToManyField("Video", blank=True)

    def __unicode__(self):
        return self.name



class Link(models.Model):
    name = models.CharField(max_length=200)
    src = models.URLField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, related_name='link')
    # image = models.OneToOneField(
    #     Image,
    #     blank=True,
    #     null=True,
    #     on_delete=models.CASCADE
    # )

    def __unicode__(self):
         return self.name


class Organization(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Skill(models.Model):
    # choices = [
    #     ("novice", "Novice"),
    #     ("intermediate", "Intermediate"),
    #     ("advanced", "Advanced"),
    #     ("expert", "Expert")
    # ]

    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    # rating = models.CharField(max_length=50, choices=choices, blank=True, null=True)

    def __unicode__(self):
        return self.name


# class Video(models.Model):
#     name = models.CharField(max_length=200)
#     src = models.URLField()
#
#     def __unicode__(self):
#         return self.name



