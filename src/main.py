"""メインスクリプト - MCP サーバを起動"""
import argparse
from src.server.mcp_server import RandomValueMCPServer


def main():
    """MCPサーバを起動するメイン関数"""
    parser = argparse.ArgumentParser(description="Random Value MCP Server")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="サーバのホスト名 (デフォルト: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=8000, help="サーバのポート番号 (デフォルト: 8000)")
    parser.add_argument("--max-value", type=int, default=100, help="ランダム値の初期上限値 (デフォルト: 100)")
    parser.add_argument("--name", type=str, default="Random Value MCP Server", help="サーバ名 (デフォルト: 'Random Value MCP Server')")
    args = parser.parse_args()
    
    server = RandomValueMCPServer(
        initial_max_value=args.max_value,
        server_name=args.name
    )
    print(f"{args.name} を起動しています（{args.host}:{args.port}、上限値: {args.max_value}）...")
    server.run(host=args.host, port=args.port)


if __name__ == "__main__":
    main()
