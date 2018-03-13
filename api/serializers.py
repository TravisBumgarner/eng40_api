from .models import *
from rest_framework import serializers



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = (
            'id',
            'name',
            'src',
        )


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = (
            'id',
            'name',
            'src',
        )


class AuthorSerializer(serializers.ModelSerializer):
    link = LinkSerializer(read_only=True, many=True)
    image = serializers.StringRelatedField()

    class Meta:
        model = Author
        fields = (
            'name',
            'description',
            'link',
            'image'
        )


class ProjectSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=True)
    preview_img = ImageSerializer(read_only=True)
    # video = serializers.StringRelatedField(many=True)
    # skill = serializers.StringRelatedField(many=True)
    link = LinkSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'category',
            # 'description',
            'start_date',
            'end_date',
            'skill',
            # 'image',
            # 'video',
            'link',
            'preview_img',
        )


class SkillSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Skill
        fields = (
            'id',
            'name',
            'category',
            # 'rating'
        )


# class VideoSerializer(serializers.ModelSerializer):
#     category = serializers.StringRelatedField()
#
#     class Meta:
#         model = Video
#         fields = (
#             'id',
#             'name',
#             'src'
#         )


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'website',
            'message',
        )
