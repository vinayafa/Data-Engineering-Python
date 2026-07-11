# 🚀 My Data Engineering Python Learning Journey

Welcome to your learning dashboard! This file is your personal log to track your progress, summarize your key takeaways, and document your growth as a Data Engineer.

---

## 📊 Challenge Tracker

Run `python run_tests.py` in your terminal to see which tests are passing!

| Module | Challenge Name | Focus Areas | Status |
| :--- | :--- | :--- | :---: |
| **01. Basics** | 🛠️ [Database Config Loader](file:///home/fighter/Desktop/Python%20for%20DE/challenges/challenge_1_basics.py) | Input parsing, Type conversions, String formatting | ⬜ Pending |
| **02. Strings** | 📝 [Web Server Log Parser](file:///home/fighter/Desktop/Python%20for%20DE/challenges/challenge_2_strings.py) | Strip, slicing, lower/upper, split, search | ⬜ Pending |
| **03. Numbers** | 🧮 [Metric Calculator](file:///home/fighter/Desktop/Python%20for%20DE/challenges/challenge_3_numbers.py) | Operators, precision rounding, validation | ⬜ Pending |
| **04. Logic** | 🚦 [ETL Data Quality Gate](file:///home/fighter/Desktop/Python%20for%20DE/challenges/challenge_4_logic.py) | Comparisons, logic gates, `any()`, `all()` | ⬜ Pending |

> *Tip: Change the Status emoji to ⚙️ In Progress or ✅ Completed as you pass the tests!*

---

## 🗺️ Learning Milestones & Notes

### 📂 Phase 1: Python Basics & Clean Inputs
- **Concepts Learned**: Print statement, escaping, variable assignment, dynamic typing, user input with `input()`.
- **Data Engineering Context**: Reading raw command line parameters or environment variables. All raw external inputs start as strings.
- **Key Takeaways**:
  - `input()` returns a string; must cast with `int()` or `float()` for numbers.
  - Semicolons are not needed; Python uses whitespace/newlines to separate statements.

### 🧵 Phase 2: String Manipulations (The Parser's Bread & Butter)
- **Concepts Learned**: Length `len()`, string indexing/slicing, strip whitespace, split by separator, search using `in`/`startswith`/`endswith`.
- **Data Engineering Context**: Parsing text logs, CSV records, URL extraction, database query construction.
- **Key Takeaways**:
  - Slicing `string[start:end]` is inclusive of `start` and exclusive of `end`.
  - Always clean data by using `.strip()` and `.lower()` before doing any comparisons.
  - `split(",")` returns a list of items; extra spacing around delimiters stays unless we clean them.

### 🔢 Phase 3: Working with Numbers & Math
- **Concepts Learned**: Types (`int`, `float`), standard math operators, floor division `//`, modulo `%`, absolute value `abs()`, rounding `round()`, checking float integer values via `is_integer()`.
- **Data Engineering Context**: Calculating metrics (throughput, records per second, size bytes), checking boundary thresholds.
- **Key Takeaways**:
  - Modulo `%` is extremely useful for batching (e.g. logging progress every N rows).
  - Floating point numbers can sometimes cause rounding issues; standard precision functions like `round(val, 2)` or integer validation are crucial.

### 🔀 Phase 4: Control flow, logic and list checkers
- **Concepts Learned**: Comparison operators, logical chaining (`and`, `or`, `not`), `any()`, `all()`, checking types using `isinstance()`.
- **Data Engineering Context**: Writing data validation schemas, monitoring dashboards, and error warning flags.
- **Key Takeaways**:
  - `any([a, b, c])` checks if at least one value is truthy (ideal for error alarm systems).
  - `all([a, b, c])` checks if every value is truthy (ideal for confirming all data quality checks passed).

---

## 📝 My Personal Reflections & Notes
*(Use this space to write down your own notes, common errors you faced, and things you want to remember.)*

- **Example Note**: *I noticed that when splitting strings, it's very easy to leave trailing spaces. Always remember to use `.strip()` when parsing CSVs!*
