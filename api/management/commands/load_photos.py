import os

from django.core.files import File
from django.core.management.base import BaseCommand
from api.models import Project, Image
from eng40.settings import BASE_DIR

INPUT_DIR = 'media/inputs'


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--mkdirs',
            action='store_true',
            dest='mkdirs',
            help='Create dirs which share the same name as the project to load photos for uploading.',
        )
        parser.add_argument(
            '--upload',
            action='store_true',
            dest='upload',
            help='Upload photos to corresponding project name',
        )

    def handle(self, *args, **options):
        if options['mkdirs']:
            projects = Project.objects.all()
            print('[>] Making dirs')
            for p in projects:
                try:
                    os.mkdir(os.path.join(root_photos_dir, p.name))
                    print('[+]     {}'.format(p.name))
                except OSError:
                    print('[-]     {}'.format(p.name))
            return

        if options['upload']:
            root_photos_dir = os.path.join(BASE_DIR, INPUT_DIR)
            projects = Project.objects.all()
            p = projects[0]
            project_dir = os.path.join(root_photos_dir, p.name)
            for img_name in os.listdir(project_dir):
                file_name = os.path.join(project_dir, img_name)
                f = File(open(file_name, 'rb'))
                i = Image(name=img_name, src=f)
                i.save()
                p.image.add(i)
            p.save()
