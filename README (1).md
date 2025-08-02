# 📰 News Headline Scraper & Analyzer

This Python project scrapes news headlines from various websites and organizes the data into CSV format. It also provides a script to generate pivot tables for quick analysis of the headlines.

---

## 🚀 Features

- Scrapes `<h1>`, `<h2>`, and `<h3>` headlines from multiple websites.
- Saves the extracted data into a structured CSV file.
- Provides a pivot table summary using `pandas`.
- Simple and clean structure for easy reuse or enhancement.

---

## 📁 Project Structure

```
python-automation/
├── news-headline.py         # Main scraper script
├── pivot-table.py           # Pivot table generator from CSV
├── requirements.txt         # Dependencies to run the scripts
├── README.md                # Project documentation
├── .gitignore               # Specifies files/folders to ignore in Git
```

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/python-automation.git
cd python-automation
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install required packages**

```bash
pip install -r requirements.txt
```

---

## ⚙️ How to Use

### 1. Scrape Headlines

Run the main script:

```bash
python news-headline.py
```

- This will create a `headlines.csv` file with all extracted headlines.

### 2. Generate Pivot Table

After scraping, run:

```bash
python pivot-table.py
```

- This will create an `pivot_table_output.xlsx` file summarizing the headlines by tag type.

---

## 📝 Output Files

These files are generated during runtime and are not included in the Git repo:

- `headlines.csv`
- `headlines-headless-mode.csv` (if applicable)
- `pivot_table_output.xlsx`

---

## 📄 Requirements

Listed in `requirements.txt`, but key packages include:

- `requests`
- `beautifulsoup4`
- `pandas`
- `openpyxl`

If you use headless browsing, also install:

- `selenium`

---

## 🚫 Files & Folders Ignored by Git

The following are excluded via `.gitignore`:

- Virtual environment (`automation-venv/`)
- Build folders (`build/`, `dist/`)
- PyInstaller spec files (`*.spec`)
- IDE configs (`.idea/`)
- Output data files (`*.csv`, `*.xlsx`)
- Python bytecode (`__pycache__/`, `*.pyc`)

---

## 📌 Disclaimer

This project is for educational purposes. Always check a website’s `robots.txt` and terms of service before scraping.

---

## 🤝 Contributions

Feel free to fork, enhance, or submit issues or pull requests. Happy scraping!
