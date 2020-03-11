import requests
from pytest import mark

@mark.register
class RegisterTests():
    def test_register_request(self, register_uri):
        #build JSON payload for registration
        data = {"email": "eve.holt@reqres.in","password": "pistol"}
        result = requests.post(register_uri, json=data)
        assert result.status_code == 200
        result_data = result.json()
        assert result_data["id"] != None
        assert result_data["token"] != None


    def test_unsuccesful_registration(self, register_uri, random_string):
        some_email = f"{random_string}@gmail.com"
        data = {"email": some_email}
        result = requests.post(register_uri, json=data)
        assert result.status_code == 400



