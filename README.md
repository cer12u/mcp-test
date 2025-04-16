# MCP-TEST

Claude Desktop向けのランダム値生成MCPサーバ

## 機能

- ランダムな値を取得するAPI
- ランダムな値の上限を設定するAPI

## インストール

```bash
# リポジトリをクローン
git clone https://github.com/cer12u/mcp-test.git
cd mcp-test

# 依存関係をインストール
pip install -e .
```

## 使用方法

### 設定ファイル

サーバの設定は `claude_desktop_config` ファイルで管理できます。以下は設定ファイルの例です：

```yaml
host: 0.0.0.0
port: 8000
name: Random Value MCP Server
instructions: |
  このサーバは、ランダムな値を生成するAPIを提供します。
  - get_random_value(): 1から設定された上限値までのランダムな整数を返します
  - set_max_value(max_value): ランダム値の上限を設定します
  - get_max_value(): 現在の上限値を取得します
random_value:
  initial_max_value: 100
```

設定項目の説明：

| 項目 | 説明 | デフォルト値 |
|------|------|------------|
| host | サーバのホスト名 | `0.0.0.0` |
| port | サーバのポート番号 | `8000` |
| name | サーバ名 | `Random Value MCP Server` |
| instructions | サーバの説明文 | (上記の説明文) |
| random_value.initial_max_value | ランダム値の初期上限値 | `100` |

### サーバの起動

```bash
python src/main.py
```

デフォルトでは `0.0.0.0:8000` でサーバが起動します。

#### コマンドライン引数

以下のコマンドライン引数を使用して、サーバの設定をカスタマイズできます：

| 引数 | 説明 | デフォルト値 |
|------|------|------------|
| `--host` | サーバのホスト名 | `0.0.0.0` |
| `--port` | サーバのポート番号 | `8000` |
| `--max-value` | ランダム値の初期上限値 | `100` |
| `--name` | サーバ名 | `Random Value MCP Server` |

#### 使用例

ホスト名やポート番号を変更する場合:

```bash
python src/main.py --host localhost --port 8080
```

ランダム値の初期上限値とサーバ名を変更する場合:

```bash
python src/main.py --max-value 500 --name "カスタムMCPサーバ"
```

すべての設定を変更する場合:

```bash
python src/main.py --host localhost --port 8080 --max-value 500 --name "カスタムMCPサーバ"
```

### API一覧

1. `get_random_value()` - ランダムな値を取得
2. `set_max_value(max_value)` - ランダム値の上限を設定
3. `get_max_value()` - 現在の上限値を取得

## テスト実行

単体テスト:

```bash
python -m unittest tests/logic/test_random_value.py
```

結合テスト:

```bash
python -m unittest tests/server/test_mcp_server.py
```

すべてのテスト:

```bash
python -m unittest discover
```
