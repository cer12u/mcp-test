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

### サーバの起動

```bash
python src/main.py
```

デフォルトでは `0.0.0.0:8000` でサーバが起動します。

ホスト名やポート番号を変更する場合:

```bash
python src/main.py --host localhost --port 8080
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
