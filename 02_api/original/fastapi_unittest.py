import requests
import unittest


"""
Before start testing run:
uvicorn main:app --reload
"""


class TestFastAPI(unittest.TestCase):
    """
    Test FastAPI
    Prevent sorting using numbering
    """

    path = "http://127.0.0.1:8000"
    item_00 = {
        "name": "aaa-111",
        "flag": True,
        "path": "../server/original"
    }
    item_01 = {
        "name": "bbb-222",
        "flag": True,
        "path": "../server/original"
    }
    name_00 = "ABC-123"

    def test_aaa_get_content_status(self):
        """get content - empty"""
        self.assertEqual(
            requests.get(url=f"{self.path}/").status_code,
            200
        )

    def test_aab_get_content_json(self):
        """get content - empty"""
        self.assertEqual(
            requests.get(url=f"{self.path}/").json(),
            {"content": {}}
        )

    def test_aac_get_item_status(self):
        """get item - empty"""
        self.assertEqual(
            requests.get(url=f"{self.path}/{self.name_00}").status_code,
            404
        )

    def test_aad_get_item_json(self):
        """get item - empty"""
        self.assertEqual(
            requests.get(url=f"{self.path}/{self.name_00}").json(),
            {"detail": f"{self.name_00} does not exist"}
        )


    def test_aae_add_item_status(self):
        """add item - empty"""
        self.assertEqual(
            requests.post(
                url=f"{self.path}/",
                json=self.item_00
            ).status_code,
            200
        )

    def test_aaf_add_item_status(self):
        """add item - again"""
        self.assertEqual(
            requests.post(
                url=f"{self.path}/",
                json=self.item_00
            ).status_code,
            400
        )

    def test_aag_add_item_json(self):
        """add item - not empty"""
        self.assertEqual(
            requests.post(
                url=f"{self.path}/",
                json=self.item_01
            ).json(),
            {"added": self.item_01}
        )

    def test_aah_get_item_status(self):
        """get item - not empty"""
        self.assertEqual(
            requests.get(url=f"{self.path}/{self.item_00["name"]}").status_code,
            200
        )

    def test_aai_get_item_json(self):
        """get item - not empty"""
        self.assertEqual(
            requests.get(url=f"{self.path}/{self.item_00["name"]}").json(),
            {self.item_00["name"]: self.item_00}
        )

    def test_aaj_get_item_status(self):
        """get item - not empty"""
        self.assertEqual(
            requests.get(url=f"{self.path}/{self.name_00}").status_code,
            404
        )

    def test_aak_get_item_json(self):
        """get item - not empty"""
        self.assertEqual(
            requests.get(url=f"{self.path}/{self.name_00}").json(),
            {"detail": f"{self.name_00} does not exist"}
        )

    def test_aal_change_item_status(self):
        """change item - not empty"""
        self.item_00["flag"] = False
        self.assertEqual(
            requests.put(url=f"{self.path}/{self.item_00["name"]}?flag=False").status_code,
            200
        )

    def test_aam_get_item_json(self):
        """get item - not empty"""
        self.assertEqual(
            requests.get(url=f"{self.path}/{self.item_00["name"]}").status_code,
            200
        )

    def test_aan_get_item_json(self):
        """get item - not empty"""
        self.assertEqual(
            requests.get(url=f"{self.path}/{self.item_00["name"]}").json(),
            {self.item_00["name"]: self.item_00}
        )

    def test_aao_change_item_json(self):
        """change item - not empty"""
        self.item_00["flag"] = True
        self.assertEqual(
            requests.put(url=f"{self.path}/{self.item_00["name"]}?flag=True").json(),
            {"changed": self.item_00}
        )

    def test_aap_change_item_status(self):
        """change item - not empty"""
        self.assertEqual(
            requests.put(url=f"{self.path}/{self.name_00}").status_code,
            404
        )

    def test_aaq_change_item_json(self):
        """change item - not empty"""
        self.assertEqual(
            requests.put(url=f"{self.path}/{self.name_00}").json(),
            {"detail": f"{self.name_00} does not exist"}
        )

    def test_aar_delete_item_status(self):
        """delete item - not empty"""
        self.assertEqual(
            requests.delete(url=f"{self.path}/delete/{self.item_00["name"]}").status_code,
            200
        )

    def test_aas_delete_item_status(self):
        """delete item - not empty"""
        self.assertEqual(
            requests.delete(url=f"{self.path}/delete/{self.name_00}").status_code,
            404
        )

    def test_aat_delete_item_json(self):
        """delete item - not empty"""
        self.assertEqual(
            requests.delete(url=f"{self.path}/delete/{self.name_00}").json(),
            {"detail": f"{self.name_00} does not exist"}
        )

    def test_aau_delete_item_json(self):
        """delete item - not empty"""
        self.assertEqual(
            requests.delete(url=f"{self.path}/delete/{self.item_01["name"]}").json(),
            {"deleted": self.item_01}
        )

    def test_aav_delete_item_status(self):
        """delete item - empty"""
        self.assertEqual(
            requests.delete(url=f"{self.path}/delete/{self.name_00}").status_code,
            404
        )

    def test_aaw_delete_item_json(self):
        """delete item - empty"""
        self.assertEqual(
            requests.delete(url=f"{self.path}/delete/{self.name_00}").json(),
            {"detail": f"{self.name_00} does not exist"}
        )


if __name__ == "__main__":
    unittest.main()
