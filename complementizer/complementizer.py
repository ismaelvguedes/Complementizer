import requests
from faker import Faker

class Complementizer:
    
    def __init__(self, url_base: str, username: str, password: str, has_token: bool = False, path_auth: str = ''):
        self.url_base: str = url_base
        self.username: str = username
        self.password: str = password
        self.has_token: bool = has_token
        self.faker = Faker(locale = 'pt_br')
        
        if self.has_token:
            response = requests.post(url_base + path_auth, data = {
                'username': username,
                'password': password,
            })
            self.token = response.json()['token']
            
    def generate(self, endpoint, fields: list[dict]):
        pass
    
    def typeField(self, type: str) -> callable:
        if type == 'name':
            return self.faker.name
        elif type == 'address':
            return self.faker.address
        elif type.split('_')[0] == 'date_of_birth':
            return self.faker.date_of_birth
