import pytest
import json

from agent.model.Asset import Asset


class TestAssets:

    def test_asset(self):
        asset = Asset("123", 10.0)
        assert asset.id == "123"
        assert asset.price == 10

    def test_toJson(self):
        asset = Asset("123", 10.0)
        _json = asset.toJson()

        content = json.loads(_json)
        assert content["id"] == "123"
        assert content["price"] == 10.0
