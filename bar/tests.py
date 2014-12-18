from django.test import TestCase
from bar.models import Bar


# Create your tests here.
class FooTestCase(TestCase):

    def test_initial_data(self):
        """
        This test will never pass, in the case where an initial_data.yaml has been
        create it won't run because an attempt to load the initial_data.json is performed
        before the migrations are actually run. 
        """
        try:
            Bar.objects.get(name='initial-data')
            self.fail("If you're seeing this, my assumption that there is a bug is wrong...")
        except Bar.DoesNotExist:
            pass

    def test_data_migration(self):
        Bar.objects.get(name='data-migration')
