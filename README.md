# manage.py test attempts to apply initial_data for apps that have migrations

It appears that in Django 1.7.1 when you run `manage.py test` it attempts to `loaddata` for apps with `initial_data.*` prior to the migrations for those apps being run.

According to [the docs](https://docs.djangoproject.com/en/dev/howto/initial-data/#automatically-loading-initial-data-fixtures) the loading of `initial_data.*` files has been deprecated in 1.7 and it states that you should "consider doing it in a data migration.".

To me, this implies that it should work and at the very least not break the running of tests. 

## Install

```bash
git clone https://github.com/alexhayes/apps-with-migrations-and-initial-data-break-tests.git
cd apps-with-migrations-and-initial-data-break-tests
pip install -r requirements.txt
```

## Replicate the issue

The following should pass;

```bash
./manage.py test
```

Run the following to create `bar/fixtures/initial_data.json`;

```bash
./manage.py create_initial_data
```

Now, run the tests, which will cause `django.db.utils.OperationalError` to be thrown;

```bash
./manage.py test -v 3
```

Which results in the following;

```
Creating test database for alias 'default' (':memory:')...
Operations to perform:
  Apply all migrations: admin, contenttypes, bar, auth, sessions
Traceback (most recent call last):
  File "./manage.py", line 10, in <module>
    execute_from_command_line(sys.argv)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 385, in execute_from_command_line
    utility.execute()
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 377, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/commands/test.py", line 50, in run_from_argv
    super(Command, self).run_from_argv(argv)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/base.py", line 288, in run_from_argv
    self.execute(*args, **options.__dict__)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/commands/test.py", line 71, in execute
    super(Command, self).execute(*args, **options)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/base.py", line 338, in execute
    output = self.handle(*args, **options)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/commands/test.py", line 88, in handle
    failures = test_runner.run_tests(test_labels)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/test/runner.py", line 147, in run_tests
    old_config = self.setup_databases()
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/test/runner.py", line 109, in setup_databases
    return setup_databases(self.verbosity, self.interactive, **kwargs)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/test/runner.py", line 299, in setup_databases
    serialize=connection.settings_dict.get("TEST", {}).get("SERIALIZE", True),
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/db/backends/creation.py", line 377, in create_test_db
    test_flush=True,
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 115, in call_command
    return klass.execute(*args, **defaults)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/base.py", line 338, in execute
    output = self.handle(*args, **options)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/commands/migrate.py", line 141, in handle
    inhibit_post_migrate=True,
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 115, in call_command
    return klass.execute(*args, **defaults)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/base.py", line 338, in execute
    output = self.handle(*args, **options)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/base.py", line 533, in handle
    return self.handle_noargs(**options)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/commands/flush.py", line 88, in handle_noargs
    call_command('loaddata', 'initial_data', **options)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 115, in call_command
    return klass.execute(*args, **defaults)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/base.py", line 338, in execute
    output = self.handle(*args, **options)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/commands/loaddata.py", line 61, in handle
    self.loaddata(fixture_labels)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/commands/loaddata.py", line 91, in loaddata
    self.load_label(fixture_label)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/management/commands/loaddata.py", line 148, in load_label
    obj.save(using=self.using)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/core/serializers/base.py", line 173, in save
    models.Model.save_base(self.object, using=using, raw=True)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/db/models/base.py", line 619, in save_base
    updated = self._save_table(raw, cls, force_insert, force_update, using, update_fields)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/db/models/base.py", line 681, in _save_table
    forced_update)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/db/models/base.py", line 725, in _do_update
    return filtered._update(values) > 0
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/db/models/query.py", line 600, in _update
    return query.get_compiler(self.db).execute_sql(CURSOR)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/db/models/sql/compiler.py", line 1004, in execute_sql
    cursor = super(SQLUpdateCompiler, self).execute_sql(result_type)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/db/models/sql/compiler.py", line 786, in execute_sql
    cursor.execute(sql, params)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/db/backends/utils.py", line 65, in execute
    return self.cursor.execute(sql, params)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/db/utils.py", line 94, in __exit__
    six.reraise(dj_exc_type, dj_exc_value, traceback)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/db/backends/utils.py", line 65, in execute
    return self.cursor.execute(sql, params)
  File "/path/to/venv/foo/local/lib/python2.7/site-packages/django/db/backends/sqlite3/base.py", line 485, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.OperationalError: Problem installing fixture '/path/to/apps-with-migrations-and-initial-data-break-tests/bar/fixtures/initial_data.json': Could not load bar.Bar(pk=1): no such table: bar_bar
```