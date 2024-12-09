from fastapi import Request
from app import app, validation, utils



@app.post('/get_form')
async def get_form(request: Request):
    params = dict(request.query_params)

    fields_types = validation.fields_types(params)
    suited_form = utils.get_form(fields_types)
    if suited_form:
        return next(iter(suited_form))
    return fields_types