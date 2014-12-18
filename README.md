apps-with-migrations-and-initial-data-break-tests
=================================================

It appears that with you run `manage.py test` it attempts to `loaddata` for apps with `initial_data.*` prior to the migrations for those apps being run.
