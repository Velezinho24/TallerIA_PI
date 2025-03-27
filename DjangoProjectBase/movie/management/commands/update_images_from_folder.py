import os
from django.core.management.base import BaseCommand
from django.conf import settings
from movie.models import Movie

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        image_folder = os.path.join(settings.MEDIA_ROOT, 'movie', 'images')

        if not os.path.exists(image_folder):
            self.stderr.write(self.style.ERROR(f"Image folder '{image_folder}' not found."))
            return

        updated_count = 0

        for movie in Movie.objects.all():
            image_filename = f"m_{movie.title}.png"
            image_path = os.path.join(image_folder, image_filename)

            if os.path.exists(image_path):
                movie.image = f"movie/images/{image_filename}"  
                movie.save()
                updated_count += 1
                self.stdout.write(self.style.SUCCESS(f"Updated image for: {movie.title}"))
            else:
                self.stderr.write(self.style.WARNING(f"Image not found for: {movie.title}"))

        self.stdout.write(self.style.SUCCESS(f"Finished updating {updated_count} movie images."))
