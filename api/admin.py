# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from api.models import Category, Image, Video, Project, Link, Skill, Tool

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    pass

