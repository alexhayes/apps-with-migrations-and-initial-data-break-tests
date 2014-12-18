# apps-with-migrations-and-initial-data-break-tests

It appears that with you run `manage.py test` it attempts to `loaddata` for apps with `initial_data.*` prior to the migrations for those apps being run.

According to [the docs](https://docs.djangoproject.com/en/dev/howto/initial-data/#automatically-loading-initial-data-fixtures) the loading of `initial_data.*` files has been deprecated in 1.7 and it states that you should "consider doing it in a data migration.".

To me, this implies that it should work and at the very least not break the running of tests. 

## Install


  