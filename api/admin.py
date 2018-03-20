# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from api.models import *


class LinkInline(admin.TabularInline):
    model = Link
    extra = 3

class ImageInline(admin.TabularInline):
    model = Image
    extra = 10


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = (
        LinkInline,
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (
        LinkInline,
        ImageInline,
    )

    filter_horizontal = (
        'skill',
        'category',
        'organization'
    )

    list_filter = (
        'category',
        'organization',
        'location',
    )

    list_display = (
        'name',
        'headline',
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        # 'rating'
    )
