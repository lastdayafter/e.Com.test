from fastapi import FastAPI
from tinydb import TinyDB, Query


app = FastAPI()
db = TinyDB('db.json')
form = Query()