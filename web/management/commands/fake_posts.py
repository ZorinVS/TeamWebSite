from django.core.management.base import BaseCommand
from web.models import Post
from faker import Faker
import random

fake = Faker("ru_RU")


class Command(BaseCommand):
    help = 'Генерирует случайные тестовые посты'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='Количество постов')

    def handle(self, *args, **options):
        count = options['count']
        for _ in range(count):
            title = fake.sentence(nb_words=6)
            content = "\n\n".join(fake.paragraphs(nb=random.randint(3, 7)))
            Post.objects.create(title=title, content=content)
        self.stdout.write(self.style.SUCCESS(f'✅ Создано {count} постов'))
