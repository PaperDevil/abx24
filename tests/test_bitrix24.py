import unittest
import os
from bitrix24 import Bitrix24, BitrixError
import aiohttp


class Bitrix24Test(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.b24 = Bitrix24('https://example.bitrix24.com/rest/1/123456789')

    async def test_init_with_empty_domain(self):
        with self.assertRaises(Exception):
            Bitrix24('')

    async def test_call_with_empty_method(self):
        with self.assertRaises(BitrixError):
            await self.b24.call_method('', aiohttp.ClientSession())

    async def test_call_non_exists_method(self):
        with self.assertRaises(BitrixError):
            await self.b24.call_method('hello.world', aiohttp.ClientSession())

    async def test_call_wrong_method(self):
        with self.assertRaises(BitrixError):
            await self.b24.call_method('helloworld', aiohttp.ClientSession())

    async def test_without_session_passed(self):
        with self.assertRaises(BitrixError):
            await self.b24.call_method('helloworld')


class ParamsPreparationTest(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.b24 = Bitrix24('https://example.bitrix24.com/rest/1/123456789')

    async def test_one_level(self):
        params = {"fruit": "apple"}
        param_string = await self.b24._prepare_params(params)
        self.assertEqual(param_string, "fruit=apple&")

    async def test_one_level_several_items(self):
        params = {"fruit": "apple", "vegetable": "broccoli"}
        param_string = await self.b24._prepare_params(params)
        self.assertEqual(param_string, "fruit=apple&vegetable=broccoli&")

    async def test_multi_level(self):
        params = {"fruit": {"citrus": "lemon"}}
        param_string = await self.b24._prepare_params(params)
        self.assertEqual(param_string, "fruit[citrus]=lemon&")

    async def test_multi_level_deep(self):
        params = {"root": {"level 1": {"level 2": {"level 3": "value"}}}}
        param_string = await self.b24._prepare_params(params)
        self.assertEqual(
            param_string, "root[level 1][level 2][level 3]=value&")

    async def test_list_dict_mixed(self):
        params = {"root": {"level 1": [
            {"list_dict 1": "value 1"}, {"list_dict 2": "value 2"}]}}
        param_string = await self.b24._prepare_params(params)
        self.assertEqual(
            param_string, "root[level 1][0][list_dict 1]=value 1&root[level 1][1][list_dict 2]=value 2&")

    async def test_multi_level_several_items(self):
        params = {"fruit": {"citrus": "lemon", "sweet": "apple"}}
        param_string = await self.b24._prepare_params(params)
        self.assertEqual(
            param_string, "fruit[citrus]=lemon&fruit[sweet]=apple&")

    async def test_list(self):
        params = {"fruit": ["lemon", "apple"]}
        param_string = await self.b24._prepare_params(params)
        self.assertEqual(param_string, "fruit[0]=lemon&fruit[1]=apple&")

    async def test_tuple(self):
        params = {"fruit": ("lemon", "apple")}
        param_string = await self.b24._prepare_params(params)
        self.assertEqual(param_string, "fruit[0]=lemon&fruit[1]=apple&")

    async def test_string(self):
        param_string = await self.b24._prepare_params('')
        self.assertEqual(param_string, "")


if __name__ == '__main__':
    unittest.main()
