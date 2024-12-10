from app import db, form



def get_form(form_data: dict) -> list[dict]:
    '''
    Получает форму, поля и значения полей которой полностью совпадают с полученныйми данными
    '''
    forms = db.search(form.fragment(form_data))
    return [form for form in forms if all([item in form_data for item in form if item != 'name'])]
    # return filter(lambda x: all([item in form_data for item in form if item != 'name']), forms)