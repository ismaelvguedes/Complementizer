from complementizer.types import TypeField
from faker import Faker
import random

class FieldComplementizer:
    
    def __init__(self, name: str, type: TypeField, **info):
        self.name = name
        self.type = type
        self.info = info

    def create(self, form):
        if form.male:
            if self.type == TypeField.NAME:
                return form.faker.name_male()
            if self.type == TypeField.NAME_FIRST:
                return form.faker.first_name_male()
            if self.type == TypeField.NAME_LAST:
                return form.faker.last_name_male()
            if self.type == TypeField.SEX:
                return 'man'
        else:
            if self.type == TypeField.NAME:
                return form.faker.name_female()
            if self.type == TypeField.NAME_FIRST:
                return form.faker.first_name_female()
            if self.type == TypeField.NAME_LAST:
                return form.faker.last_name_female()
            if self.type == TypeField.SEX:
                return 'woman'

        if self.type == TypeField.ADDRESS:
            return str(form.faker.address()).replace('\n', ' ')
        if self.type == TypeField.STREET:
            return form.faker.street_name()
        if self.type == TypeField.NUMBER:
            return form.faker.port_number()
        if self.type == TypeField.DISTRICT:
            return form.faker.bairro()
        if self.type == TypeField.POSTAL:
            return form.faker.postcode()
        if self.type == TypeField.CITY:
            return form.faker.city()
        if self.type == TypeField.STATE:
            return form.faker.state_abbr()
        if self.type == TypeField.COUNTRY:
            return form.faker.country()
        if self.type == TypeField.DATE_OF_BIRTH:
            return form.faker.date_of_birth(**self.info)
        if self.type == TypeField.PHONE:
            return form.faker.phone_number()
        if self.type == TypeField.EMAIL:
            return form.faker.email()
        if self.type == TypeField.PASSWORD:
            return form.faker.password(15, True, True, True, True)
        if self.type == TypeField.COMPANY:
            return form.faker.company()
        
class Dependency:
    def __init__(self, name, path) -> None:
        self.name = name
        self.path = path

class FormComplementizer:
    
    def __init__(self, fields: list[FieldComplementizer], dependencies: list[Dependency] = []):
        self.faker = Faker(locale = 'pt_br')
        self.fields = fields
        self.dependencies = dependencies

    def generate(self, deps: list[dict]):
        self.male = self.faker.boolean(50)
        data = {}
        for field in self.fields:
            data[field.name] = str(field.create(self))
        for dep in deps:
            data[dep['name']] = dep['values'][random.randint(0, len(dep['values']) - 1)]
        return data