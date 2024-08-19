from complementizer.types import TypeField

class FieldComplementizer:
    
    def __init__(self, name: str, type: TypeField, **agrs):
        if type == TypeField.NAME:
            pass
        self.function = type