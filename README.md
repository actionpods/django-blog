=====
Action Blog
=====

Action Blog is a django app that creates and encourages new leaders in activism both to start their own movements and coordinate with others to make real change.

Quick start
-----------

1. Add "action-blog" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'action-blog',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^action-blog/', include('action-blog.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Visit http://127.0.0.1:8000/action-blog/
