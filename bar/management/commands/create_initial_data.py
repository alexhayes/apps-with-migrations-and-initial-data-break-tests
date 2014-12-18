from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = "Create the initial_data.json file that causes tests to break."

    def handle(self, *args, **options):
        with open(os.path.join(os.path.dirname(__file__), '..', '..', 'fixtures', 'initial_data.json'), 'w') as f:
            f.write("""[
    {
        "pk": "1",
        "model": "bar.Bar",
        "fields": {
            "name": "initial-data"
        }
    }
]""")

        print "Wrote 'bar/fixtures/initial_data.json' - tests should now fail."