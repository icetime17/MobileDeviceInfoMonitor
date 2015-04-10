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
			'timestamp'			: _nowTimestamp(),
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
		percentages = db.BatteryLevel.find()
		ret = _parse_raw_percentage(percentages)
		return HttpResponse(json.dumps({"status": 0, "data": ret}),
				content_type='application/json')


def _nowTimestamp():
	# 2015-4-8 18:3:0
	timestamp = ''
	rawTime = map(_timeFormat, datetime.datetime.now().utctimetuple()[0:6])
	timestamp = '%s-%s-%s %s:%s:%s' % (rawTime[0], rawTime[1], rawTime[2], rawTime[3], rawTime[4], rawTime[5])
	return timestamp


def _timeFormat(x):
	if x<10:
		return '0%d' % x
	else:
		return str(x)


def _parse_raw_percentage(percentages):
	ret = {}
	for p in percentages:
		name 		 	= p['name']
		uuid 			= p['uuid']
		timestamp 		= p['timestamp']
		batteryLevel 	= p['batteryLevel']
		if not ret.get(name):
			ret[name] = {
				'name'		: name,
				'uuid'		: uuid,
				'battery'	: {},
			}
		ret[name]['battery'][timestamp] = batteryLevel
	for name in ret:
		ret[name]['battery'] = sorted(ret[name]['battery'].iteritems(), 
									  key=lambda d:d[0])
	return ret


if __name__ == '__main__':
	# conn = pymongo.Connection()
	# db = conn.DeviceInfo
	# percentages = db.BatteryLevel.find({'name':'TA iPhone 5'})
	# ret = _parse_raw_percentage(percentages)
	# print ret
	print _nowTimestamp()