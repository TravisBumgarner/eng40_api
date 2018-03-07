from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from .serializers import *
from models import *

class AuthorViewSet(ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = None


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


# class ImageViewSet(ReadOnlyModelViewSet):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#     pagination_class = None


class LinkViewSet(ReadOnlyModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    pagination_class = None


class ProjectViewSet(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        response_data = {}
        for project in self.queryset:
            serializer = self.get_serializer(project)
            response_data[project.id] = serializer.data
        return Response(response_data)



        serializer = UserSerializer(user)
        return Response(serializer.data)


class SkillViewSet(ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    pagination_class = None


# class VideoViewSet(ReadOnlyModelViewSet):
#     queryset = Video.objects.all()
#     serializer_class = VideoSerializer
#     pagination_class = None
