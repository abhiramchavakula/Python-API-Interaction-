import requests

#getting all 200 TODOs

URL = 'https://jsonplaceholder.typicode.com/todos'
r = requests.get(url = URL, params = PARAMS)        # To execute get request
PARAMS = {'id':1-200}
response = requests.get(url = URL, params = PARAMS)
data = response.json()
print(response.status_code)     # To print http response code
print(response.text)            # To print formatted JSON response


#create a TODO

API_ENDPOINT = 'https://jsonplaceholder.typicode.com/todos'
# data to being sent to our API endpoint
data = {
    "userId": 1,
    "id": 201,
    "title": "creating new TODO",
    "completed": true
  }
  response = requests.post(url = API_ENDPOINT, data = data) # sending post request and saving the response as response object
  jsonplaceholder_URL = response.text
  print("New TODO has been created succesfully!")


 #delete a TODO

 API_ENDPOINT = 'https://jsonplaceholder.typicode.com/todos'
 # data being deleted from our API endpoint
 data = {
     "userId": 1,
     "id": 23,
     "title": "deleting a TODO",
     "completed": true
   }
   response = requests.delete(url = API_ENDPOINT, data = data) # executing delete request
   jsonplaceholder_URL = response.text
   print("TODO with ID 23 has been deleted succesfully!")
