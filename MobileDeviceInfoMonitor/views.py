# -*- coding: utf8 -*-
'''
@auther: chris.hu
@views for battery

'''

import os
import sys
import json
import datetime
import pymongo

sys.path.append(os.path.abspath(
	os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
))

os.environ['DJANGO_SETTINGS_MODULE'] = 'MobileDeviceInfoMonitor.settings'


from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def battery(request):
	print 'battery'
	return render(request, 'battery.html')


if __name__ == '__main__':
	pass

	