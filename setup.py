from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sql-dag-analyzer",
    version="0.1.0",
    author="Devin AI",
    author_email="devin-ai-integration[bot]@users.noreply.github.com",
    description="A tool to analyze SQL files and create a DAG of table and CTE dependencies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jianhuanggo/sql-dag-analyzer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "sqlglot>=26.0.0",
        "networkx>=3.0",
        "matplotlib>=3.5.0",
    ],
    extras_require={
        "viz": ["pygraphviz>=1.10"],
    },
    entry_points={
        "console_scripts": [
            "sql-dag-analyzer=sql_dag_analyzer:main",
        ],
    },
)
