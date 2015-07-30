
import httplib

host_name = '52.27.141.129'
host_port = 80
video_file = '<video_name>' #the api curruntly support .mp4 files only

def get_test(host_name, host_port):
	#get test:
	conn = httplib.HTTPConnection(host_name, host_port)
	conn.request("GET","/api")
	res = conn.getresponse()
	print res.status, res.reason
	print res.read()
	conn.close()


def run_api (video_file, host_name, host_port):
	#post test
	conn = httplib.HTTPConnection(host_name, host_port)
	headers = {"Content-type": "application/octet-stream", "Accept": "text/plain"}
	params = open(video_file, "rb")
	conn.request("POST","/api", params, headers)
	res = conn.getresponse()
	print res.status, res.reason
	print res.read()


	
run_api (video_file, host_name, host_port)

# get_test(host_name, host_port)