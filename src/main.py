"""メインスクリプト - MCP サーバを起動"""
import argparse
import json
import os
from src.server.mcp_server import RandomValueMCPServer


def load_config(config_file="claude_desktop_config.json"):
    """設定ファイルを読み込む"""
    default_config = {
        "server": {
            "host": "0.0.0.0",
            "port": 8000,
            "name": "Random Value MCP Server",
            "instructions": "このサーバは、ランダムな値を生成するAPIを提供します。\n- get_random_value(): 1から設定された上限値までのランダムな整数を返します\n- set_max_value(max_value): ランダム値の上限を設定します\n- get_max_value(): 現在の上限値を取得します"
        },
        "random_value": {
            "initial_max_value": 100
        }
    }
    
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
                if "server" not in config:
                    config["server"] = default_config["server"]
                else:
                    for key, value in default_config["server"].items():
                        if key not in config["server"]:
                            config["server"][key] = value
                
                if "random_value" not in config:
                    config["random_value"] = default_config["random_value"]
                else:
                    for key, value in default_config["random_value"].items():
                        if key not in config["random_value"]:
                            config["random_value"][key] = value
                
                return config
        except (json.JSONDecodeError, IOError) as e:
            print(f"設定ファイルの読み込みに失敗しました: {e}")
            return default_config
    else:
        return default_config


def main():
    """MCPサーバを起動するメイン関数"""
    config = load_config()
    
    parser = argparse.ArgumentParser(description="Random Value MCP Server")
    parser.add_argument("--host", type=str, default=config["server"]["host"], 
                        help=f"サーバのホスト名 (デフォルト: {config['server']['host']})")
    parser.add_argument("--port", type=int, default=config["server"]["port"], 
                        help=f"サーバのポート番号 (デフォルト: {config['server']['port']})")
    parser.add_argument("--max-value", type=int, default=config["random_value"]["initial_max_value"], 
                        help=f"ランダム値の初期上限値 (デフォルト: {config['random_value']['initial_max_value']})")
    parser.add_argument("--name", type=str, default=config["server"]["name"], 
                        help=f"サーバ名 (デフォルト: '{config['server']['name']}')")
    parser.add_argument("--config", type=str, default="claude_desktop_config.json",
                        help="設定ファイルのパス (デフォルト: 'claude_desktop_config.json')")
    args = parser.parse_args()
    
    if args.config != "claude_desktop_config.json":
        config = load_config(args.config)
    
    server = RandomValueMCPServer(
        initial_max_value=args.max_value,
        server_name=args.name,
        server_instructions=config["server"].get("instructions")
    )
    
    print(f"{args.name} を起動しています（{args.host}:{args.port}、上限値: {args.max_value}）...")
    server.run(host=args.host, port=args.port)


if __name__ == "__main__":
    main()
