# Python for DE Notes

This note file summarizes your code lessons from the `Python for DE` folder.
It is written in the same order as your files and includes the important concepts you should remember.

---

## 1. Basics of Python

### 1_Hello.py
- This file is the first example of Python code execution.
- Use `print()` to display text on the screen.
- Strings must be wrapped in quotes: single `'...'` or double `"..."`.
- Comments start with `#` and are ignored by Python.

Things to remember:
- `print()` is the basic output function.
- Python is case-sensitive, so `print` is not the same as `Print`.
- Every statement ends at the end of the line, not with a semicolon.

---

### 2_Escapes.py
- This file demonstrates escape sequences inside strings.
- `\"` is used to print a double quote inside a string.
- `\'` is used to print a single quote inside a string.
- `\\` prints a literal backslash.
- `\n` creates a new line.
- `\t` inserts a tab space.
- Triple quotes `"""..."""` allow multiline strings with one `print()` call.

Things to remember:
- Escape sequences let you include special characters in strings.
- Use raw strings only when you want literal backslashes, but in this file the examples show standard escaping.
- Multiline strings are helpful for long text blocks.

---

### 3_Print_usecase.py
- This script uses variables and basic arithmetic to calculate totals.
- Variables hold values that can be used in expressions.
- The `print()` function can display values separated by commas.
- Comments explain why `print()` is useful.

Things to remember:
- Use variables for values that may change later.
- `*` is multiplication and `+` is addition.
- `print()` can show the result of expressions directly.
- `print()` is useful for communicating, debugging, and testing.

---

### 4_Variables.py
- This file shows how variables store text values.
- Variables are assigned using `=`.
- You can reuse the same variable name with a different value.
- This demonstrates dynamic typing in Python.

Things to remember:
- Variables make your code easier to update.
- Strings can be combined in a `print()` call using commas.
- Changing `name` or `language` in one place updates all uses of that variable.
- Avoid using variable names that shadow built-in Python functions.

---

### 5_Input.py
- This file introduces `input()` to get user data.
- `input()` always returns a string.
- The prompt text inside `input()` is shown to the user.

Things to remember:
- `input()` does not convert types automatically.
- If you need a number, convert the result with `int()` or `float()`.
- Always store input values in variables before using them.

---

### 6_DataTypes.py
- This file lists the most common Python data types:
  - `int` for whole numbers
  - `float` for decimal numbers
  - `str` for text
  - `bool` for `True` or `False`
  - `None` for no value
- It also shows the difference between an empty string `""` and a string with a single space `" "`.

Things to remember:
- Python is dynamically typed: the same code can use different types.
- Strings are values in quotes, even if they only contain digits.
- `None` means “nothing” or “no value.”
- `True` and `False` are special boolean values.

---

### 7_Functions&Methods.py
- This file checks the type of variables with `type()`.
- It gets string length with `len()`.
- It shows a string method `upper()` that converts text to uppercase.
- There is a bug: calling `upper()` on a number is not valid.

Things to remember:
- `type(value)` tells you the data type.
- `len(value)` works on strings, lists, and other sequence types.
- Methods like `.upper()` only work on string values.
- Numbers do not support string methods such as `.upper()`.

---

## 2. Working With Strings

### Type Function/1_type().py
- This file demonstrates the `type()` built-in function.
- It shows string concatenation and type conversion with `str()`.
- It also shows a common mistake: after converting an integer to a string, you cannot add an integer to it.

Things to remember:
- `str(number)` converts a number to text.
- Once a value is converted to a string, arithmetic operations with integers are invalid.
- Python does not automatically convert between strings and numbers.
- Always check the data type before mixing strings and numbers.

---

### Math Function/len.py
- This file currently defines a string variable named `password`.
- The file name suggests using `len()` to measure string length.

Things to remember:
- `len(password)` returns the number of characters in the password string.
- You can use `len()` on any string to check its size.
- `password` is a text value and should be in quotes.

---

### Transformations/app.py
- This file shows string transformation by combining a first name and a last name.
- It also shows how to join a folder path and file name into one full file path.
- The examples use `+` to concatenate strings.

Things to remember:
- String concatenation joins two text values together.
- Use `+` carefully when combining variables that are already strings.
- This pattern is useful for building full names, file paths, and other text output.
- Keep the comments short and clear so the code is easy to revise later.

---

### Transformations/f-string.py
- This file compares long string concatenation with f-strings.
- The old style is harder to read because it needs many `+` signs and `str()` conversions.
- The f-string version is easier to read because variables are placed directly inside `{}`.
- It also shows that f-strings can evaluate expressions like `{2+3}`.
- Double braces `{{` and `}}` are used when you want literal curly braces in the output.

Things to remember:
- Put `f` before the opening quote to create an f-string.
- Use `{variable}` inside the string to insert values.
- Use `{expression}` when you want Python to calculate something inside the string.
- Use double braces when you need actual curly braces printed on screen.

---

### Transformations/split_function.py
- This file shows how `split()` breaks one string into a list of smaller parts.
- The first example splits a date and time string by spaces.
- The second example splits a comma-separated value string into fields.
- Spaces around values stay if the separator is only a comma.

Things to remember:
- `split(" ")` divides text wherever there is a space.
- `split(",")` divides text wherever there is a comma.
- `split()` returns a list.
- Extra spaces may remain in the pieces unless you clean them separately.

---

### Transformations/multipleFunction.py
- This file shows string repetition with the `*` operator.
- The first example repeats `ha` three times.
- The other examples repeat `#` and `$` to make simple output patterns.

Things to remember:
- `"text" * number` repeats the text that many times.
- This works with any string value.
- String repetition is useful for separators, headings, and repeated patterns.

---

### Transformations/IndexAndSlicing.py
- This file shows string indexing with positive and negative positions.
- `text[0]` gets the first character.
- `text[-1]` gets the last character.
- `text[3]` gets the fourth character, which is `h` in `Python`.
- It also shows string slicing with `date[0:4]`, `date[:4]`, `date[5:7]`, and `date[8:]`.

Things to remember:
- Indexing starts at `0` in Python.
- Negative indexes count from the end of the string.
- You can use positive or negative indexes to get the same character.
- Make sure the index is inside the string length, or Python will raise an error.
- Slicing includes the start index but excludes the end index.
- Leaving out the start index means "start from the beginning."
- Leaving out the end index means "go until the end."
- Slicing is useful for pulling out parts of text such as year, month, and day.

---

### Cleaning/strip.py
- This file shows how to remove extra spaces or characters from the sides of a string.
- `lstrip()` removes characters from the left side.
- `rstrip()` removes characters from the right side.
- `strip()` removes characters from both sides.
- The file also checks whether a string has extra spaces by comparing the original length with the stripped length.

Things to remember:
- `strip()` is useful for cleaning user input or messy text data.
- `strip()` without arguments removes whitespace.
- `strip("#")` removes `#` symbols from both ends.
- Comparing `len(text)` and `len(text.strip())` helps detect unwanted spaces.
- Clean data before saving or processing it further.

---

### Cleaning/caseConversion.py
- This file shows how `lower()` and `upper()` change the letter case of a string.
- It also shows how to clean strings with `lower().strip()` before comparing them.
- The comparison returns `True` when both cleaned strings match.

Things to remember:
- `lower()` is useful when you want case-insensitive comparison.
- `upper()` is useful when you want everything in uppercase.
- Use `strip()` together with case conversion to remove extra spaces before comparing text.
- Clean and normalize data before checking equality.

---

### Searching/search.py
- This file shows how to check whether a string starts with, ends with, or contains a value.
- `startswith()` is used for things like country codes in phone numbers.
- `endswith()` is used for domains and file extensions.
- `in` is used to search for text inside strings.

Things to remember:
- Use `startswith()` when you want to verify the beginning of a string.
- Use `endswith()` when you want to verify the ending of a string.
- Use `in` when you only need to know whether a value appears anywhere inside the string.
- These checks are useful for validating emails, URLs, file names, and phone numbers.

---

### Working with Numbers/Numeric/Rounding.py
- This file shows how to use `abs()`, `round()`, and several math rounding helpers on numbers.
- `abs()` gives the distance from zero.
- `round()` shortens a number to a chosen number of decimal places.
- `math.floor()` rounds down.
- `math.ceil()` rounds up.
- `math.trunc()` removes the decimal part without rounding.
- `int()` also removes the decimal part by converting the value to a whole number.
- The example shows rounding a price value to different decimal places and comparing several rounding behaviors.

Things to remember:
- Use `abs()` when you want a positive distance, even if the original number is negative.
- Use `round(number, 2)` when you want two decimal places, such as for money.
- Use `round(number)` when you want the nearest whole number.
- Use `math.floor()` when you need to always round down.
- Use `math.ceil()` when you need to always round up.
- Use `math.trunc()` or `int()` when you want to drop the decimal part.
- `round()` is useful when you want cleaner output for display or reporting.

<span style="color:#c7254e">Definition: `abs()` returns the absolute value, `round()` changes decimal precision, `floor()` rounds down, `ceil()` rounds up, `trunc()` removes decimals, and `int()` converts to a whole number.</span>

---

## General Python Notes
- Comment your code with `#` to explain what each part does.
- Keep variable names meaningful: `price_shirt`, `qty_jeans`, `total_shirt`.
- Use `print()` for quick debugging and output verification.
- Remember the difference between `=` (assignment) and `==` (comparison).
- Python lines are separated by new lines, not semicolons.
- Use blank lines to make your code easier to read.
- When your code gives an error, read the message carefully: it usually tells you the exact problem.

## Common errors to avoid

- Mixing text and numbers without conversion.
- Using string methods on non-string values.
- Forgetting that `input()` returns a string.
- Confusing `""` (empty text) with `None`.
- Using reserved words as variable names.

---

## Suggested practice

- Run each file and observe the output.
- Try changing values and re-running the script.
- Add your own examples of `print()`, `input()`, and data-type conversions.
- Practice writing a small script that asks for two numbers and prints their sum.
