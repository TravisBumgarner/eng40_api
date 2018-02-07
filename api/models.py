from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)


class EngineeringProject(models.Model):
    category = models.ManyToManyField("Category")
    date = models.DateTimeField()
    description = models.TextField()
    image = models.ManyToManyField("EngineeringImage")
    name = models.CharField(max_length=200)
    skill = models.ManyToManyField("Skill")
    tool = models.ManyToManyField("Tool")
    video = models.ManyToManyField("Video")


class EngineeringImage(models.Model):
    name = models.CharField(max_length=200)
    src = models.URLField()


class Link(models.Model):
    name = models.CharField(max_length=200)
    src = models.URLField()
    image = models.ManyToManyField("PhotoImage")


class PhotoProject(models.Model):
    category = models.ManyToManyField("Category")
    date = models.DateTimeField()
    description = models.TextField()
    image = models.ManyToManyField("PhotoImage")
    name = models.CharField(max_length=200)
    skill = models.ManyToManyField("Skill")
    tool = models.ManyToManyField("Tool")
    video = models.ManyToManyField("Video")


class PhotoImage(models.Model):
    name = models.CharField(max_length=200)
    src = models.URLField()
    camera = models.CharField(max_length=200)
    exposure = models.CharField(max_length=200)


class Skill(models.Model):
    category = models.ManyToManyField("Category")
    name = models.CharField(max_length=200)
    rating = models.CharField(max_length=50)


class Tool(models.Model):
    name = models.CharField(max_length=200)


class Video(models.Model):
    name = models.CharField(max_length=200)
    src = models.URLField()