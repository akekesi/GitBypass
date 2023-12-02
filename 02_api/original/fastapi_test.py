import json
import requests

URL = "http://127.0.0.1:8000"
NAME = "bypass"
NAME_ERROR = "bypass_error"
ITEM = {
    "name": "bypass",
    "flag": "True",
    "path": "../server/original"
}

def print_dict_pretty(dictionay: dict, comment: str = "") -> None:
    if comment:
        print(comment)
    print(json.dumps(dictionay, indent=4))

# get main
print_dict_pretty(
    comment=f"get main:",
    dictionay=requests.get(url=f"{URL}/").json()
)

# get item --> error
print_dict_pretty(
    comment=f"get {NAME}:",
    dictionay=requests.get(url=f"{URL}/{NAME}").json()
)

# add item
print_dict_pretty(
    comment=f"add {ITEM['name']}",
    dictionay=requests.post(
        url=f"{URL}/",
        json=ITEM
    ).json()
)

# get item
print_dict_pretty(
    comment=f"get {NAME}:",
    dictionay=requests.get(url=f"{URL}/{NAME}").json()
)

# add item --> error
print_dict_pretty(
    comment=f"add {ITEM['name']}",
    dictionay=requests.post(
        url=f"{URL}/",
        json=ITEM
    ).json()
)

# update flag --> error
flag = "False"
print_dict_pretty(
    comment=f"update flag of {NAME_ERROR} --> {flag}",
    dictionay=requests.put(f"{URL}/{NAME}?flag={flag}").json()
)

# update flag
flag = "False"
print_dict_pretty(
    comment=f"update flag of {NAME} --> {flag}",
    dictionay=requests.put(f"{URL}/{NAME}?flag={flag}").json()
)

# update flag
flag = "True"
print_dict_pretty(
    comment=f"update flag of {NAME} --> {flag}",
    dictionay=requests.put(f"{URL}/{NAME}?flag={flag}").json()
)

# update path
path = "xxx"
print_dict_pretty(
    comment=f"update path of {NAME} --> {path}",
    dictionay=requests.put(f"{URL}/{NAME}?path={path}").json()
)

# update path
path = "../server/original"
print_dict_pretty(
    comment=f"update path of {NAME} --> {path}",
    dictionay=requests.put(f"{URL}/{NAME}?path={path}").json()
)

# delete item --> error
print_dict_pretty(
    comment=f"delete {NAME_ERROR}",
    dictionay=requests.delete(url=f"{URL}/delete/{NAME_ERROR}").json()
)

# delete item
print_dict_pretty(
    comment=f"delete {NAME}",
    dictionay=requests.delete(url=f"{URL}/delete/{NAME}").json()
)

# get main
print_dict_pretty(
    comment=f"get main:",
    dictionay=requests.get(url=f"{URL}/").json()
)
