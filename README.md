# SQL DAG Analyzer

A tool to analyze SQL files and create a Directed Acyclic Graph (DAG) of table and Common Table Expression (CTE) dependencies.

## Features

- Extracts tables and CTEs from SQL files using sqlglot
- Creates a DAG representation of dependencies
- Visualizes the DAG using matplotlib
- Analyzes DAG properties (root nodes, leaf nodes, longest path, etc.)
- Handles complex SQL with multiple CTEs and nested queries
- Supports multiple SQL dialects (Spark, BigQuery, Hive, etc.)
- Provides multiple parsing strategies with fallbacks for robust analysis

## Installation

```bash
pip install sql-dag-analyzer
```

Or install from source:

```bash
git clone https://github.com/jianhuanggo/sql-dag-analyzer.git
cd sql-dag-analyzer
pip install -e .
```

## Usage

### Command Line

```bash
python -m sql_dag_analyzer path/to/your/sql_file.sql
```

### Python API

```python
from sql_dag_analyzer import SQLDAGAnalyzer

# Initialize with SQL content
with open('path/to/your/sql_file.sql', 'r') as f:
    sql_content = f.read()

analyzer = SQLDAGAnalyzer(sql_content)
analyzer.analyze()

# Get tables and CTEs
tables = analyzer.get_tables()
ctes = analyzer.get_ctes()

# Analyze DAG properties
properties = analyzer.analyze_dag_properties()

# Visualize the DAG
analyzer.visualize_dag('output.png')
```

## Requirements

- Python 3.6+
- sqlglot
- networkx
- matplotlib
- pygraphviz (optional, for better visualization)

## How It Works

The analyzer uses a multi-layered approach to extract information from SQL:

1. First, it attempts to parse the SQL using sqlglot with multiple dialect attempts
2. If full parsing succeeds, it extracts tables and CTEs from the parsed expression tree
3. If full parsing fails, it falls back to tokenizer-based analysis
4. As a last resort, it uses regex-based extraction for maximum compatibility

## License

MIT
