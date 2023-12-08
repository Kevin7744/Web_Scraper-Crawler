import requests

# on the form the key take aways are the name and value.
params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
r = requests.post('http://pythonscraping.com/pages/processing.php', data=params)
print(r.text)


