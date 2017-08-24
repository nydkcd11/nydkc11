import os
if os.environ.get('DEV') is not None:
	from .settings_dev import *
else:
	from .settings_production import *
