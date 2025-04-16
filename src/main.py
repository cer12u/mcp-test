"""メインスクリプト - MCP サーバを起動"""
import argparse
from src.server.mcp_server import RandomValueMCPServer


def main():
    """MCPサーバを起動するメイン関数"""
    parser = argparse.ArgumentParser(description="Random Value MCP Server")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="サーバのホスト名 (デフォルト: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8000, help="サーバのポート番号 (デフォルト: 8000)")
    args = parser.parse_args()
    
    server = RandomValueMCPServer()
    print(f"Random Value MCP Server を起動しています（{args.host}:{args.port}）...")
    server.run(host=args.host, port=args.port)


if __name__ == "__main__":
    main()
