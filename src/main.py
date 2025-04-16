"""メインスクリプト - MCP サーバを起動"""
import argparse
import json
import os
from src.server.mcp_server import RandomValueMCPServer


def load_config(config_file="claude_desktop_config.json"):
    """設定ファイルを読み込む"""
    default_host = "0.0.0.0"
    default_port = 8000
    default_name = "Random Value MCP Server"
    default_max_value = 100
    default_instructions = "このサーバは、ランダムな値を生成するAPIを提供します。\n- get_random_value(): 1から設定された上限値までのランダムな整数を返します\n- set_max_value(max_value): ランダム値の上限を設定します\n- get_max_value(): 現在の上限値を取得します"
    
    host = os.environ.get("HOST", default_host)
    port = int(os.environ.get("PORT", default_port))
    name = os.environ.get("SERVER_NAME", default_name)
    max_value = int(os.environ.get("INITIAL_MAX_VALUE", default_max_value))
    
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
                
                if "mcpServers" in config_data and isinstance(config_data["mcpServers"], dict):
                    server_name = next(iter(config_data["mcpServers"]))
                    server_config = config_data["mcpServers"][server_name]
                    
                    if "env" in server_config and isinstance(server_config["env"], dict):
                        if "HOST" in server_config["env"] and "HOST" not in os.environ:
                            host = server_config["env"]["HOST"]
                        if "PORT" in server_config["env"] and "PORT" not in os.environ:
                            port = int(server_config["env"]["PORT"])
                        if "SERVER_NAME" in server_config["env"] and "SERVER_NAME" not in os.environ:
                            name = server_config["env"]["SERVER_NAME"]
                        if "INITIAL_MAX_VALUE" in server_config["env"] and "INITIAL_MAX_VALUE" not in os.environ:
                            max_value = int(server_config["env"]["INITIAL_MAX_VALUE"])
        except (json.JSONDecodeError, IOError) as e:
            print(f"設定ファイルの読み込みに失敗しました: {e}")
    
    return {
        "host": host,
        "port": port,
        "name": name,
        "instructions": default_instructions,
        "random_value": {
            "initial_max_value": max_value
        }
    }


def main():
    """MCPサーバを起動するメイン関数"""
    config = load_config()
    
    parser = argparse.ArgumentParser(description="Random Value MCP Server")
    parser.add_argument("--host", type=str, default=config["host"], 
                        help=f"サーバのホスト名 (デフォルト: {config['host']})")
    parser.add_argument("--port", type=int, default=config["port"], 
                        help=f"サーバのポート番号 (デフォルト: {config['port']})")
    parser.add_argument("--max-value", type=int, default=config["random_value"]["initial_max_value"], 
                        help=f"ランダム値の初期上限値 (デフォルト: {config['random_value']['initial_max_value']})")
    parser.add_argument("--name", type=str, default=config["name"], 
                        help=f"サーバ名 (デフォルト: '{config['name']}')")
    parser.add_argument("--config", type=str, default="claude_desktop_config.json",
                        help="設定ファイルのパス (デフォルト: 'claude_desktop_config.json')")
    args = parser.parse_args()
    
    if args.config != "claude_desktop_config.json":
        config = load_config(args.config)
    
    server = RandomValueMCPServer(
        initial_max_value=args.max_value,
        server_name=args.name,
        server_instructions=config.get("instructions")
    )
    
    print(f"{args.name} を起動しています（{args.host}:{args.port}、上限値: {args.max_value}）...")
    server.run(host=args.host, port=args.port)


if __name__ == "__main__":
    main()
