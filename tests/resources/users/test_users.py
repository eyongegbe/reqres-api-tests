import requests
from pytest import mark


@mark.user
class UsersTests():

    def test_calling_user_request(self, user_uri):
        uri = f"{user_uri}/2"
        result = requests.get(uri)
        data = result.json()
        assert data["data"]["email"] == "janet.weaver@reqres.in"
        assert data["data"]["last_name"] == "Weaver"
        assert result.status_code == 200

    def test_create_a_user(self, user_uri, random_string):
        name = f"ola-{random_string}"
        user = {"name": name, "title": "Director"}
        result = requests.post(user_uri, json=user)
        data = result.json()
        assert result.status_code == 201
        assert data["name"] == user["name"]
        assert data["title"] == user["title"]

    @mark.chain
    def test_update_user(self, user_uri, random_string):
        # build JSON for creating user
        name = f"{random_string}"
        user = {"name": name, "title": "Director"}

        #send request to create user
        result = requests.post(user_uri, json=user)
        data = result.json()
        assert data["name"] == name
        assert data["title"] == "Director"

        #get created user id
        user_id = data["id"]

        #build JSON payload for updating user
        user_update = {"name": name, "title": "CEO"}
        update_uri = f"{user_uri}/{user_id}"

        #send request to update user
        new_result = requests.put(update_uri, json=user_update)

        #verify response after update
        new_data = new_result.json()
        print(new_result.text)
        assert new_data["title"] == "CEO"

    @mark.chain
    def test_delete_user(self, user_uri, random_string):
        #build JSON to create user
        name = f"Jean-Claude {random_string}"
        user = {"name": name, "title": "Actor"}
        #create user and check http status code
        result = requests.post(user_uri, json=user)
        assert result.status_code == 201

        #get user id
        data = result.json()
        user_id = data["id"]
        delete_uri = f"{user_uri}/{user_id}"

        #send delete user request
        new_result = requests.delete(delete_uri)
        assert new_result.status_code == 204

    @mark.chain
    def test_patch_user_information(self, user_uri, random_string):
        # build JSON for creating user
        name = f"{random_string}"
        user = {"name": name, "title": "Director"}

        #send request to create user
        result = requests.post(user_uri, json=user)
        data = result.json()
        assert data["name"] == name
        assert data["title"] == "Director"

        #get created user id
        user_id = data["id"]

        #build JSON payload for updating user
        user_update = {"name": name, "title": "CEO"}
        update_uri = f"{user_uri}/{user_id}"

        #send request to update user
        new_result = requests.patch(update_uri, json=user_update)

        #verify response after update
        new_data = new_result.json()
        print(new_result.text)
        assert new_data["title"] == "CEO"