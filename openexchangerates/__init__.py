
__version__ = '0.2.2'
__author__ = 'Bomzheg'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020 Bomzheg. Forked from 2013 Metglobal https://github.com/metglobal/openexchangerates'

import asyncio
import os

try:
    import uvloop
except ImportError:
    uvloop = None
else:
    if 'DISABLE_UVLOOP' not in os.environ:
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


