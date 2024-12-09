import re



VALIDATORS = {
    'date': r'(\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01]))|((0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[012])\.\d{4})',
    'phone': r'\+7?\s*\d{3}?\s*\d{3}?\s*\d{2}\s*\d{2}',
    'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    'text': r'[\S|\s*]+'
}


def fields_types(form_data: dict) -> dict:
    '''
    Проверяет соответствие типов всех полей формы,
    возвращает словврь формата "имя_поля": "тип_данных"
    '''
    return {field: check_type(value) for field, value in form_data.items()}


def check_type(value: str) -> str:
    '''
    Ищет соответсвующий значений тип данных, возвращает строку "тип_данных"
    '''
    for value_type, validator in VALIDATORS.items():
        if re.match(validator, value):
            return value_type
    return