"""RandomValueGeneratorクラスの単体テスト"""
import unittest
from src.logic.random_value import RandomValueGenerator


class TestRandomValueGenerator(unittest.TestCase):
    """RandomValueGeneratorクラスのテストケース"""

    def setUp(self):
        """各テスト実行前のセットアップ"""
        self.generator = RandomValueGenerator()

    def test_default_max_value(self):
        """デフォルトの上限値が100であることを確認"""
        self.assertEqual(self.generator.get_max_value(), 100)

    def test_custom_max_value(self):
        """カスタム上限値でオブジェクトを初期化できることを確認"""
        generator = RandomValueGenerator(max_value=50)
        self.assertEqual(generator.get_max_value(), 50)

    def test_set_max_value(self):
        """上限値を設定できることを確認"""
        self.generator.set_max_value(200)
        self.assertEqual(self.generator.get_max_value(), 200)

    def test_set_invalid_max_value(self):
        """無効な上限値の場合に例外が発生することを確認"""
        with self.assertRaises(ValueError):
            self.generator.set_max_value(0)
        with self.assertRaises(ValueError):
            self.generator.set_max_value(-10)

    def test_get_random_value_range(self):
        """生成されるランダム値が有効な範囲内であることを確認"""
        self.generator.set_max_value(50)
        
        for _ in range(100):
            value = self.generator.get_random_value()
            self.assertGreaterEqual(value, 1)
            self.assertLessEqual(value, 50)


if __name__ == "__main__":
    unittest.main()
