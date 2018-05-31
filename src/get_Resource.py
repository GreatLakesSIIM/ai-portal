import requests


function get_Resource(url):

	# url = "http://hackathon.siim.org/fhir/" + url_commands

	headers = {
		'apikey': "eee630b7-2669-4a56-843b-eb88b4dff02f",
		'Cache-Control': "no-cache",
		'Postman-Token': "1423e88c-7bc8-4f53-8069-d4deb7254c90"
		}

	print("GET request: ")
	print(url)

	response = requests.request("GET", url, headers=headers)

	if (response.status_code != requests.codes.ok):
		raise AssertionError('Something went wrong with GET request', response.status_code)

	print(response.text)
	
	return response