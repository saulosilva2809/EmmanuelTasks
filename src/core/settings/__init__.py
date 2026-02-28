import os

env = os.getenv('DJANGO_ENV')

if env == 'dev':
    from .dev import *
else:
    from .prod import *
