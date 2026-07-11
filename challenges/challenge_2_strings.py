# Challenge 2: Strings - Web Server Log Parser & Cleaner
# Complete the functions below to parse and clean messy logs and csv records.

def clean_log_line(raw_log):
    """
    Data Engineering context: Logging systems or messaging queues often produce 
    messages with extra quotes, tabs, or padding. We need to clean them first.

    Task:
    - Strip any leading/trailing whitespace (spaces, tabs, newlines) from `raw_log`.
    - Strip any double quotes `"` or single quotes `'` that surround the string.
    - Return the fully cleaned string.

    Example:
    clean_log_line('  "2026-07-10 14:35:22 | ERROR | Connection failure"  ') 
    -> '2026-07-10 14:35:22 | ERROR | Connection failure'
    """
    # TODO: Implement this function
    pass


def parse_log_timestamp(log_line):
    """
    Data Engineering context: Slicing specific portions of fixed-width records.

    Task:
    - Use string slicing to extract the first 19 characters of the log line 
      (which contains the timestamp in YYYY-MM-DD HH:MM:SS format).
    - If the input log line is shorter than 19 characters, return None.

    Example:
    parse_log_timestamp("2026-07-10 14:35:22 | ERROR | Database connection timed out") 
    -> "2026-07-10 14:35:22"
    """
    # TODO: Implement this function
    pass


def check_error_severity(log_line):
    """
    Data Engineering context: Filtering logs based on severity levels.

    Task:
    - Perform a case-insensitive check to see if the log line contains either "error" or "warning".
    - Return True if either of those words are present, and False otherwise.
    - Hint: convert the string to lower case using .lower() first, then use the `in` operator.

    Example:
    check_error_severity("2026-07-10 14:35:22 | ERROR | Connection refused") -> True
    check_error_severity("2026-07-10 14:35:22 | INFO | System running normal") -> False
    """
    # TODO: Implement this function
    pass


def parse_csv_row(csv_row):
    """
    Data Engineering context: Parsing text files row by row into data fields.

    Task:
    - Split the `csv_row` string using the comma `,` as a delimiter.
    - Strip the surrounding whitespace from each element in the resulting list.
    - Return the list of clean data elements.
    - Hint: You can use a list comprehension or clean the items in a loop.
      If loops haven't been learned yet, you can also access elements manually if the row has a fixed length of 3 elements, 
      but a loop/list comprehension is best. Let's make sure it handles any number of elements using list comprehension!

    Example:
    parse_csv_row("  101 , John Doe ,  Software Engineer  ") -> ["101", "John Doe", "Software Engineer"]
    """
    # TODO: Implement this function
    pass
