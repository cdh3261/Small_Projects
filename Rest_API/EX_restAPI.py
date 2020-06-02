import requests

r = requests.post('http://13.125.222.176/quiz/jordan', json={'nickname': "광주1반최동호", 'yourAnswer': "kubernetes"})
r.status_code
print(r.status_code)
r.headers
print(r.headers)
r.encoding
print(r.encoding)
r.text
print(r.text)
r.json()
print(r.json())