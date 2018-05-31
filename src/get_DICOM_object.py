import requests

url = "http://hackathon.siim.org/dicom-web/studies/1.3.6.1.4.1.14519.5.2.1.8421.4009.308092408045167711117671108231/series/1.3.6.1.4.1.14519.5.2.1.8421.4009.148721140606055021653661934276/instances/1.3.6.1.4.1.14519.5.2.1.8421.4009.445297343480625496511480948334"

headers = {
    'apikey': "eee630b7-2669-4a56-843b-eb88b4dff02f",
    'Cache-Control': "no-cache",
    'Postman-Token': "1423e88c-7bc8-4f53-8069-d4deb7254c90"
    }

print("GET request")

response = requests.request("GET", url, headers=headers)

if (response.status_code != requests.codes.ok):
	raise AssertionError('Something went wrong with GET request', response.status_code)


	
print(response.text)