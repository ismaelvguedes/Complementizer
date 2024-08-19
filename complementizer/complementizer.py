import requests
from complementizer.form import FormComplementizer

class Complementizer:
    
    def __init__(self, url_base: str, username: str, password: str, has_token: bool = False, path_auth: str = ''):
        self.url_base: str = url_base
        self.username: str = username
        self.password: str = password
        self.has_token: bool = has_token
        
        if self.has_token:
            response = requests.post(url_base + path_auth, data = {
                'username': username,
                'password': password,
            })
            self.token = response.json()['token']
            
    def populate(self, endpoint, form: FormComplementizer, amount: int):
        for id in range(0, amount):
            deps = []
            for dependency in form.dependencies:
                response = requests.get(self.url_base + dependency.path, headers = { 'Authorization': 'Token ' + self.token }) 
                values = []
                for cargo in response.json():
                    values.append(cargo['id'])
                deps.append({
                    'name': dependency.name,
                    'values': values
                })
                
            datas = form.generate(deps=deps)
            response = requests.post(self.url_base + endpoint, data = datas, headers = { 'Authorization': 'Token ' + self.token }) 
            print(response.json())