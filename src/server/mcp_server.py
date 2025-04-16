"""fastmcpを使用したMCPサーバの実装"""
from fastmcp import FastMCP
from src.logic.random_value import RandomValueGenerator


class RandomValueMCPServer:
    """ランダム値生成機能を持つMCPサーバ"""

    def __init__(self):
        """コンストラクタ"""
        self.random_generator = RandomValueGenerator()
        
        self.server = FastMCP(name="Random Value MCP Server")
        
        self.register_tools()

    def register_tools(self):
        """ツール（API）をサーバに登録"""
        
        @self.server.tool()
        def get_random_value() -> int:
            """
            ランダムな整数値を取得します。
            
            Returns:
                int: 1から設定された上限値までのランダムな整数
            """
            return self.random_generator.get_random_value()
        
        @self.server.tool()
        def set_max_value(max_value: int) -> str:
            """
            ランダム値の上限を設定します。
            
            Args:
                max_value: 新しい上限値（1以上の整数）
                
            Returns:
                str: 設定完了メッセージ
                
            Raises:
                ValueError: max_valueが1未満の場合
            """
            try:
                self.random_generator.set_max_value(max_value)
                return f"上限値が{max_value}に設定されました"
            except ValueError as e:
                raise ValueError(str(e))
        
        @self.server.tool()
        def get_max_value() -> int:
            """
            現在設定されているランダム値の上限を取得します。
            
            Returns:
                int: 現在の上限値
            """
            return self.random_generator.get_max_value()

    def run(self, host: str = "0.0.0.0", port: int = 8000):
        """
        サーバを起動
        
        Args:
            host: ホスト名（デフォルト: "0.0.0.0"）
            port: ポート番号（デフォルト: 8000）
        """
        import uvicorn
        app = self.server.sse_app
        uvicorn.run(app, host=host, port=port)
