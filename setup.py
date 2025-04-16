"""セットアップファイル"""
from setuptools import setup, find_packages

setup(
    name="random-value-mcp-server",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastmcp>=2.1.2",
    ],
    python_requires=">=3.8",
    description="Claude Desktop向けのランダム値生成MCPサーバ",
)
