"""ランダム値を生成するロジックモジュール"""
import random
from typing import Optional


class RandomValueGenerator:
    """ランダムな値を生成・管理するクラス"""

    def __init__(self, max_value: int = 100):
        """
        コンストラクタ
        
        Args:
            max_value: ランダム値の上限（デフォルト: 100）
        """
        self._max_value = max_value

    def get_random_value(self) -> int:
        """
        ランダム値を取得する
        
        Returns:
            1からmax_valueまでのランダムな整数
        """
        return random.randint(1, self._max_value)

    def set_max_value(self, max_value: int) -> None:
        """
        ランダム値の上限を設定する
        
        Args:
            max_value: 新しい上限値（1以上の整数）
            
        Raises:
            ValueError: max_valueが1未満の場合
        """
        if max_value < 1:
            raise ValueError("上限値は1以上の整数である必要があります")
        self._max_value = max_value

    def get_max_value(self) -> int:
        """
        現在設定されているランダム値の上限を取得する
        
        Returns:
            現在の上限値
        """
        return self._max_value
