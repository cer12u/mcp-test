"""MCPサーバの結合テスト"""
import unittest
import asyncio
from unittest.mock import patch, MagicMock
from src.server.mcp_server import RandomValueMCPServer


class TestMCPServer(unittest.IsolatedAsyncioTestCase):
    """MCPサーバの結合テスト"""

    def setUp(self):
        """各テスト実行前のセットアップ"""
        self.server = RandomValueMCPServer()

    async def test_get_random_value(self):
        """get_random_value APIが正しく機能することを確認"""
        with patch.object(self.server.random_generator, 'get_random_value', return_value=42):
            result = await self.server.server.call_tool("get_random_value", {})
            self.assertEqual(result[0].text, "42")

    async def test_set_max_value(self):
        """set_max_value APIが正しく機能することを確認"""
        with patch.object(self.server.random_generator, 'set_max_value') as mock_set_max:
            result = await self.server.server.call_tool("set_max_value", {"max_value": 200})
            mock_set_max.assert_called_once_with(200)
            self.assertEqual(result[0].text, "上限値が200に設定されました")

    async def test_get_max_value(self):
        """get_max_value APIが正しく機能することを確認"""
        with patch.object(self.server.random_generator, 'get_max_value', return_value=150):
            result = await self.server.server.call_tool("get_max_value", {})
            self.assertEqual(result[0].text, "150")

    async def test_set_invalid_max_value(self):
        """無効な上限値を設定した場合にエラーが発生することを確認"""
        with patch.object(self.server.random_generator, 'set_max_value', 
                          side_effect=ValueError("上限値は1以上の整数である必要があります")):
            with self.assertRaises(Exception) as context:
                await self.server.server.call_tool("set_max_value", {"max_value": 0})
            
            self.assertIn("上限値は1以上の整数である必要があります", str(context.exception))


if __name__ == "__main__":
    unittest.main()
