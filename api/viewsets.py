from rest_framework.viewsets import ModelViewSet

from .serializers import SkillSerializer
from models import Skill

class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    pagination_class = None