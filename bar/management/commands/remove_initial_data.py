from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = "Remove the initial_data.json file that causes tests to break."

    def handle(self, *args, **options):
        os.unlink(os.path.join(os.path.dirname(__file__), '..', '..', 'fixtures', 'initial_data.json'))
        print "Removed 'bar/fixtures/initial_data.json' - tests should now work."