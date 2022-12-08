# 회원가입 더미 데이터 저장
import requests
import json
import random

def board_api(method, title="", content="", username="", path=""):
    API_HOST = "http://ec2-3-38-141-38.ap-northeast-2.compute.amazonaws.com:8000/api/boards/"
    url = API_HOST + path
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    body = {
        "title": f"{title} - {username}",
        "content": f"{content}"
    }
    
    try:
        if method == 'GET':
            if username:
                jwt = signin_api(username=username)['token']['access']
                headers["Authorization"] = f"Bearer {jwt}"
            response = requests.get(url, headers=headers)

        elif method == 'POST':
            jwt = signin_api(username=username)['token']['access']
            headers["Authorization"] = f"Bearer {jwt}"
            response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))

        elif method == 'PUT':
            body = {
                "title": f"{title}",
                "content": f"{content}"
            }
            jwt = signin_api(username=username)['token']['access']
            headers["Authorization"] = f"Bearer {jwt}"
            response = requests.put(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))

        elif method == 'PATCH':
            body = {
                "title": f"{title}",
                "content": f"{content}"
            }
            jwt = signin_api(username=username)['token']['access']
            headers["Authorization"] = f"Bearer {jwt}"
            response = requests.patch(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))

        elif method == 'DELETE':
            jwt = signin_api(username=username)['token']['access']
            headers["Authorization"] = f"Bearer {jwt}"
            response = requests.delete(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))

        print("response status %r" % response.status_code)
        print("response text %r" % response.text)
    except Exception as ex:
        print(ex)
    
    return response.json()


def signin_api(username, password="test"):
    url = "http://ec2-3-38-141-38.ap-northeast-2.compute.amazonaws.com:8000/api/users/sign-in/"
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    body = {
        "username": f"{username}",
        "password": f"{password}"        
    }
    response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
    return response.json()

def read_list():
    board_api(method='GET')

def read_detail():
    user = "test"+str(random.randint(1,20000))
    board_api(method='GET', username=user)


# board_api(method='GET', username=user, path=f"{random.randint(1,17)}")

def create_article():
    user = "test"+str(random.randint(1,20000))
    title = "Dummy Article"
    content = "This is for making bulk log data"
    board_api(method='POST', title=title, content=content, username=user)

def patch_article():
    board_list = board_api(method='GET')
    last_boardid = board_list[-1]['id']
    path = random.randint(1, last_boardid)
    try:
        res = board_api(method='GET', path=str(path))
        user = "test"+f"{res['user']}"
        if "Updated" not in res['title']:
            title = "Updated " + res['title']
            content = "Updated " + res['content']
            board_api(method='PATCH', title=title, content=content, username=user, path=str(path))
        else:
            title = res['title'].split('Updated ')[-1]
            content = res['content'].split('Updated ')[-1]
            board_api(method='PATCH', title=title, content=content, username=user, path=str(path))
    except:
        pass

def put_article():
    board_list = board_api(method='GET')
    last_boardid = board_list[-1]['id']
    path = random.randint(1, last_boardid)
    try:
        res = board_api(method='GET', path=str(path))
        user = "test"+f"{res['user']}"
        if "Updated" not in res['title']:
            title = "Updated " + res['title']
            content = "Updated " + res['content']
            board_api(method='PATCH', title=title, content=content, username=user, path=str(path))
        else:
            title = res['title'].split('Updated ')[-1]
            content = res['content'].split('Updated ')[-1]
            board_api(method='PUT', title=title, content=content, username=user, path=str(path))
    except:
        pass

def delete_article():
    board_list = board_api(method='GET')
    last_boardid = board_list[-1]['id']
    path = random.randint(1, last_boardid)
    try:
        res = board_api(method='GET', path=str(path))
        user = "test"+f"{res['user']}"
        board_api(method='DELETE', username=user, path=str(path))
    except:
        pass

def random_function(num):
    num %= 6
    if num == 0:
        read_list()
    elif num == 1:
        read_detail()
    elif num == 2:
        create_article()
    elif num == 3:
        patch_article()
    elif num == 4:
        put_article()
    elif num == 5:
        delete_article()

if __name__ == "__main__":
    for i in range(int(10e5)):
        random_function(random.randint(1, 100))
