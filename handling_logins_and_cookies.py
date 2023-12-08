import requests

# params = {'username': 'Ryan', 'passworsd': 'password'}
# r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', params)
# print('Coookie is set to:')
# print(r.cookies.get_dict())
# print('Going to profile page...')
# r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', 
#                  cookies=r.cookies)
# print(r.text)


"""For more complicated sites that frequently modify cookies"""

# session object keeps track of session information,
# cookies, headers, protocol information.
session = requests.Session()

params = {'username': 'username', 'password':'password'}
s = session.post('http://pythonscraping.com/pages/cookies/welcome.php', params)
print('Cookie is set to:')
print(s.cookies.get_dict())
print('Going to profile page...')
s = session.get('http://pythonscraping.com/pages/cookies/profile.php')
print(s.text)

