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

def level(request):
	'''
	@insert one record for DeviceInfo
	'''
	conn = pymongo.Connection()
	db = conn.DeviceInfo	
	if request.method == 'POST':
		data = {
			'name'				: request.POST.get('name', None),
			'uuid'				: request.POST.get('uuid', None),
			'batteryLevel'		: request.POST.get('batteryLevel', 0),
			'timestamp'			: datetime.datetime.now(),
			# 'model'				: request.POST.get('model', None),
			# 'localizedModel'	: request.POST.get('localizedModel', None),
			# 'systemName'		: request.POST.get('systemName', None),
			# 'systemVersion'		: request.POST.get('systemVersion', 0),
		}
		if data['uuid']:
			db.BatteryLevel.insert(data)
			return HttpResponse(json.dumps({"status": 0, "data": 0}),
					content_type='application/json')
		else:
			return HttpResponse(json.dumps({"status": -1,
					"errMsg": "The uuid is not specified."}),
					content_type='application/json')
	else:
		rs = db.BatteryLevel.find()
		for r in rs:
			print r
		return HttpResponse(json.dumps({"status": 0, "data": 0}),
				content_type='application/json')


if __name__ == '__main__':
	conn = pymongo.Connection()
	db = conn.DeviceInfo
	data = dict(uuid='ghi123', name='name123', batteryLevel=60.0)
	db.BatteryLevel.insert(data)
	rs = db.BatteryLevel.find()
	for r in rs:
		print r

	