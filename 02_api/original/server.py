import requests


def server_set_up(url: str, item: dict):
    requests.post(
        url=f"{url}",
        json = item
    )


def bypass(url: str, name: str):
    response = requests.get(url=f"{url}/{name}")
    if response.status_code == 200:
        data = response.json()
        if data[name]["flag"]:
            return data[name]["path"]
    return


if __name__ == "__main__":
    # arguments
    url = "http://127.0.0.1:8000"
    item = {
        "name": "bypass",
        "flag": True,
        "path": "../server/original"
    }

    # set up server
    server_set_up(url=url, item=item)

    # run bypass
    path = bypass(url=url, name=item["name"])
    print(path)
