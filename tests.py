from random import choice
import requests



TEST_URL = 'http://localhost:8000/get_form'


def test_user():
    expected_response = {
        "name": "UserForm", 
        "username": "text", 
        "password": "text", 
        "email": "email", 
        "phone_number": "phone"
    }
    params = {
        'username': 'my_name',
        'password': 'pass123',
        'email': 'example@example.com',
        'phone_number': '+7 000 000 00 00'
    }
    assert make_request(params=params) == expected_response


def test_comment():
    expected_response = {
        "name": "CommentForm", 
        "username": "text", 
        "email": "email", 
        "phone_number": "phone", 
        "date": "date", 
        "body": "text"
    }
    params = {
        'username': 'my_name',
        'email': 'example@example.com',
        'phone_number': '+7 000 000 00 00',
        'date': choice(['20.10.1990', '2000-11-02', '10.07.2001', '1990-03-08']),
        'body': 'Hello world'
    }
    assert make_request(params=params) == expected_response


def test_order():
    expected_response = {
        "name": "OrderForm", 
        "username": "text", 
        "email": "email", 
        "phone_number": "phone", 
        "order_date": "date"
    }
    params = {
        'username': 'my_name',
        'email': 'example@example.com',
        'phone_number': '+7 000 000 00 00',
        'order_date': choice(['20.10.1990', '2000-11-02', '10.07.2001', '1990-03-08']),
    }
    assert make_request(params=params) == expected_response


def test_user_fail():
    expected_response = {
        "usernam": "date", 
        "pasword": "text", 
        "email": "email", 
        "phone_number": "phone"
    }
    params = {
        'usernam': '20.11.1990',
        'pasword': 'pass123',
        'email': 'example@example.com',
        'phone_number': '+7 000 000 00 00'
    }
    assert make_request(params=params) == expected_response


def test_comment_fail():
    expected_response = {
        "my_name": "text", 
        "email": "phone", 
        "phone_number": "email", 
        "date": "text", 
        "body": "text"
    }
    params = {
        'my_name': 'my_',
        'email': '+7 000 000 00 00',
        'phone_number': 'example@example.com',
        'date': '2000-11-34',
        'body': 'Hello world'
    }
    assert make_request(params=params) == expected_response


def test_fail_anything():
    expected_response = {
        "usr": "date", 
        "email": "text", 
        "phone_number": "email", 
        "date": "text", 
        "body": "text"
    }
    params = {
        'usr': '2000-11-21',
        'email': 'i like cookies',
        'phone_number': 'example@example.com',
        'date': '2000-11-34',
        'body': 'Hello world'
    }
    assert make_request(params=params) == expected_response



def make_request(**kwargs):
    with requests.post(TEST_URL, **kwargs) as response:
        return response.json()