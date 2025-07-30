import yaml
from django.core.management.base import BaseCommand
from web.models import Post
from pathlib import Path

class Command(BaseCommand):
    help = "Загружает посты из .md файлов в папке content/posts (YAML frontmatter поддерживается)"

    def handle(self, *args, **options):
        base_path = Path("content/posts")
        for md_file in base_path.glob("*.md"):
            with open(md_file, encoding='utf-8') as f:
                raw = f.read()

            if raw.startswith("---"):
                _, frontmatter, body = raw.split("---", 2)
                metadata = yaml.safe_load(frontmatter)
                title = metadata.get("title", "Без названия").strip()
                content = body.strip()
            else:
                lines = raw.splitlines()
                title = lines[0].lstrip("# ").strip()
                content = "\n".join(lines[1:]).strip()

            post, created = Post.objects.get_or_create(
                title=title,
                defaults={"content": content}
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ Добавлен: {title}"))
            else:
                self.stdout.write(self.style.WARNING(f"⚠️ Пропущен (уже существует): {title}"))
