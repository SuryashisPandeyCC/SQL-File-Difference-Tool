# SQL-File-Difference-Tool

# sqldiff.py

A simple command-line tool to compare two SQL files and display their differences with color highlighting. Optionally, it can generate an AI-powered explanation of the changes.

---

## 🚀 Features

- Compare two `.sql` files line by line  
- Colorized diff output:
  - 🟢 Additions in green  
  - 🔴 Deletions in red  
- Optional AI explanation using Claude (Anthropic API)  
- Lightweight and easy to use  

---

## 📦 Requirements

- Python 3.x  
- Libraries:
  - `colorama`
  - `anthropic` (only required for `--explain` feature)

Install dependencies:

```bash
pip install colorama anthropic
