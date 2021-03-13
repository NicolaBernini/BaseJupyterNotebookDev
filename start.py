#!/usr/bin/env python
import os
import sys

os.environ['EXT_PORT'] = '9001'

os.system('docker-compose run --service-ports dev-win')
os.system('docker-compose rm')

