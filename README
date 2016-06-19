Kegbot
======

This is a project to build a system for tracking kegerator usage and displaying real time
information about kegs.

Working Features
----------------

(though they may continue to change)

* Flow meter recording
* Pluggable backend for running on different platforms (Raspberry Pi, Cubie, Edison, etc.)
* Support multiple flow meters inputs, limited only by the platform GPIO

In Progress Features
--------------------

* Interface for displaying keg stats (amount in keg, style, ABV, etc) in real time

Planned Features
----------------

* Temperature reading
* Track recipe, batch, style, abv, stats for display
* Web admin interface for easy management of all manual input data
* Pluggable backend for reporting stats to other systems (statsd?)

Running Project
----------------

At least three processes need to be started to be running for everything to work. It's recommended
that these be managed by something like supervisord for anything other than development
environments.

Starting reader: reads input from sensors and passing data to Celery for processing.

```
python manage.py runreader
```

Starting Celery: runs tasks that calculates and stores data sensors recorded.

```
celery -A kegbot worker
```

Starting Webserver: serves REST API and builtin browser interface.

```
python manage.py runserver
```
