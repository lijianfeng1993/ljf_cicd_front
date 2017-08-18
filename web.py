#!/usr/bin/env python
# -*- :utf-8 -*-
import bottle
from bottle import route, run, request
from bottle import template, view
import urllib
import urllib2
import json

app = bottle.Bottle()

def getalljobs():
	requesturl = 'http://10.132.47.15:8888/v1/getalljobs'
	req = urllib2.Request(requesturl)
	res_data = urllib2.urlopen(req)
	#res = res_data.read()
	res = json.load(res_data)["info"]
	joblist = res.split(" ")
	return set(joblist)

@app.route('/home')
def home():
	return template('home')

@app.route('/createjob')
def createjob():
	return template('createjobselect')

@app.route('/create_cicdjob')
def create_cicdjob():
	return template('create_cicdjob')

@app.route('/do_create_cicdjob',method='POST')
def do_create_cicdjob():
	jobname = request.forms.get('jobname')
	language = request.forms.get('language')
	url = request.forms.get('url')

	requesturl = "http://10.132.47.15:8888/v2/createjenkinsjob"
	post_data = {"Jobname":jobname,"Language":language,"Url":url}
	headers = {'Content-Type': 'application/json'} 
	#post_data_urlencode = urllib.urlencode(post_data)
	req = urllib2.Request(url = requesturl,data =json.dumps(post_data), headers=headers)
	res_data = urllib2.urlopen(req)
	res = res_data.read()
	return template('create_cicdjobresult',tjobname = jobname, tresult = res)

@app.route('/create_enginejob')
def create_enginejob():
	return template('create_enginejob')

@app.route('/do_create_enginejob',method  = 'POST')
def do_create_enginejob():
	jobname = request.forms.get('jobname')
	language = request.forms.get('language')
	path = request.forms.get('path')
	requesturl = "http://10.132.47.15:8888/v1/createjenkinsjob"
	post_data = {"Jobname":jobname,"Language":language,"Path":path}
	headers = {'Content-Type': 'application/json'}
	req = urllib2.Request(url = requesturl,data =json.dumps(post_data), headers=headers)
	res_data = urllib2.urlopen(req)
	res = res_data.read()
	return template('create_enginejobresult',tjobname = jobname, tresult = res)

@app.route('/create_sonarjob')
def create_sonarjob():
	return template('create_sonarjob')

@app.route('/do_create_sonarjob',method  = 'POST')
def do_create_sonarjob():
	jobname = request.forms.get('jobname')
	language = request.forms.get('language')
	url = request.forms.get('url')
	requesturl = "http://10.132.47.15:8888/v3/createjenkinsjob"
	post_data = {"Jobname":jobname,"Language":language,"Url":url}
	headers = {'Content-Type': 'application/json'}
	req = urllib2.Request(url = requesturl,data =json.dumps(post_data), headers=headers)
	res_data = urllib2.urlopen(req)
	res = res_data.read()
	return template('create_sonarjobresult',tjobname = jobname, tresult = res)

@app.route('/buildjob')
def buildjob():
	alljobnames = getalljobs()
	return template('buildjob',talljobnames = alljobnames)

@app.route('/do_buildjob',method='POST')
def do_buildjob():
	jobname = request.forms.get('jobname')
	requesturl = 'http://10.132.47.15:8888/v1/buildjenkinsjob/%s' % jobname
	req = urllib2.Request(requesturl)
	res_data = urllib2.urlopen(req)
	res = res_data.read()

	return template('buildjobresult', tresult = res, tjobname = jobname)
	#return template('home')

@app.route('/deletejob')
def deletejob():
	alljobnames = getalljobs()
	return template('deletejob',talljobnames = alljobnames)

@app.route('/do_deletejob',method='POST')
def do_deletejob():
	jobname = request.forms.get('jobname')
	requesturl = 'http://10.132.47.15:8888/v1/deletejenkinsjob/%s' % jobname
	req = urllib2.Request(requesturl)
	req.get_method = lambda: 'DELETE'
	res_data = urllib2.urlopen(req)
	res = res_data.read()
	return template('deletejobresult', tresult = res, tjobname = jobname)

@app.route('/getsonarresult')
def getsonarresult():
	alljobnames = getalljobs()
	return template('getsonarresult',talljobnames = alljobnames)

@app.route('/do_getsonarresult',method='POST')
def do_getsonarresult():
	jobname = request.forms.get('jobname')
	requesturl = 'http://10.132.47.15:8888/v1/sonarresult/%s' % jobname
	req = urllib2.Request(requesturl)
	res_data = urllib2.urlopen(req)
	res = res_data.read()
	result_insonar = "http://10.132.47.15:9001/dashboard?id=%s" % jobname
	return template('sonarresult',tjobname = jobname, tresult = res, tresulturl = result_insonar)

@app.route('/getconsole')
def getconsole():
	alljobnames = getalljobs()
	return template('getconsole',talljobnames = alljobnames)

@app.route('/do_getconsole',method='POST')
def do_getconsole():
	jobname = request.forms.get('jobname')
	requesturl = 'http://10.132.47.15:8888/v1/jenkinsconsole/%s' % jobname
	req = urllib2.Request(requesturl)
	res_data = urllib2.urlopen(req)
	#res = res_data.read()
	#return dict(res).get('Console Output')
	res = json.load(res_data)["Console Output"].replace("\n","<br />")
	result_injenkins = "http://10.132.47.15:9000/job/%s/lastBuild/consoleText" % jobname
	return template('consoleresult',tjobname = jobname,tresult = res, tresulturl= result_injenkins)

app.run(host='0.0.0.0',port=4502,debug=True)


