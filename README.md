TheHerk Module
==============

TheHerk Module is a very simple django CMS plugin for posting a module for use in a sidebar.

Usage
-----

1. Add "module" to your INSTALLED_APPS

        INSTALLED_APPS = (
            ...
            'module',
        )

2. Run `python manage.py migrate module`.

   Alternately, you could `syncdb` and `migrate --fake`
