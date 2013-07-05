import os

ABS_PATH = os.path.dirname(os.path.abspath(__file__))

print ABS_PATH + '/db/AuthDB'

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "media")
print MEDIA_ROOT



