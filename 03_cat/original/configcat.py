import configcatclient


class ConfigCat:

    def __init__(self, sdk_key: str) -> None:
        self.configcat_client = configcatclient.get(sdk_key=sdk_key)

    def get_flag(self, key: str) -> bool:
        return self.configcat_client.get_value(key=key, default_value=False)


if __name__ == "__main__":
    # arguments
    key = "GitBypass"
    path_sdk_key = "sdk.key"
    with open(path_sdk_key, "r") as sdk_key_open:
        sdk_key = sdk_key_open.read()

    # get and print flag from configcat
    configcat = ConfigCat(sdk_key=sdk_key)
    flag = configcat.get_flag(key=key)
    print(flag)
