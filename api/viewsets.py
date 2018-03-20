from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from api.forms import ContactForm
from api.utils import send
from .serializers import *
from models import *


class AuthorViewSet(ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = None


class LocationViewSet(ReadOnlyModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        response_data = {}
        for location in self.queryset:
            serializer = self.get_serializer(location)
            response_data[location.id] = serializer.data
        return Response(response_data)


class OrganizationViewSet(ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        response_data = {}
        for organization in self.queryset:
            serializer = self.get_serializer(organization)
            response_data[organization.id] = serializer.data
        return Response(response_data)


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        response_data = {}
        for category in self.queryset:
            serializer = self.get_serializer(category)
            response_data[category.id] = serializer.data
        return Response(response_data)


class ImageViewSet(ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        response_data = {}
        for image in self.queryset:
            serializer = self.get_serializer(image)
            response_data[image.id] = serializer.data
        return Response(response_data)


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


class SkillViewSet(ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        response_data = {}
        for skill in self.queryset:
            serializer = self.get_serializer(skill)
            response_data[skill.id] = serializer.data
        return Response(response_data)


class ContactViewSet(GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = None

    def get_throttles(self):
        if self.action in ['create',]:
            self.throttle_scope = 'contact.' + self.action
        return super(ContactViewSet, self).get_throttles()

    def create(self, request):
        r = request.data

        form = ContactForm(r)

        if not form.is_valid():
            is_submit_error = True
            detail = "Sorry, there was an error with your message, please check your inputs and try again."

        else:
            c = Contact(
                name=r['name'],
                email=r['email'],
                website=r['website'],
                message=r['message'],
            )
            c.save()

            send("Name: {}\nEmail: {}\nWebsite: {}\nMessage: {}".format(r['name'], r['email'], r['website'], r['message']))

            is_submit_error = False
            detail = "Thank you for your message, I'll get back to you shortly!"

        return Response({
            'is_submit_error': is_submit_error,
            'detail': detail
        })
