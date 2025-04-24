import csv
from django.core.management.base import BaseCommand
from models import Quote

class Command(BaseCommand):
    help = 'Upload quotes from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header if present
            for row in reader:
                quote_text, author, categories = row
                Quote.objects.create(
                    quote_text=quote_text.strip(),
                    author=author.strip(),
                    categories=categories.strip()
                )

        self.stdout.write(self.style.SUCCESS(f'Successfully uploaded quotes from {csv_file}'))
