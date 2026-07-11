#!/usr/bin/env python3
import sys

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_header(title):
    print(f"\n{BOLD}{CYAN}=== {title} ==={RESET}")

def print_success(msg):
    print(f"  {GREEN}✓ {msg}{RESET}")

def print_failure(msg, details=None):
    print(f"  {RED}✗ {msg}{RESET}")
    if details:
        print(f"    {YELLOW}Hint: {details}{RESET}")

def run_basics_tests():
    print_header("Challenge 1: Basics - Database Config Loader")
    try:
        from challenges.challenge_1_basics import load_db_port, format_connection_uri
    except Exception as e:
        print_failure("Could not import functions from challenges.challenge_1_basics", str(e))
        return False

    success = True
    
    # Test load_db_port
    try:
        if load_db_port("5432") == 5432 and load_db_port("invalid") is None and load_db_port("8080") == 8080:
            print_success("load_db_port() works correctly.")
        else:
            print_failure("load_db_port() failed tests.", "Expected load_db_port('5432') -> 5432 and load_db_port('invalid') -> None.")
            success = False
    except Exception as e:
        print_failure("load_db_port() raised an error during execution.", str(e))
        success = False

    # Test format_connection_uri
    try:
        t1 = format_connection_uri("localhost", 5432, "analytics") == "postgresql://localhost:5432/analytics"
        t2 = format_connection_uri("", 5432, "analytics") is None
        t3 = format_connection_uri("localhost", "5432", "analytics") is None  # port must be int
        t4 = format_connection_uri("localhost", 5432, "") is None
        
        if t1 and t2 and t3 and t4:
            print_success("format_connection_uri() works correctly.")
        else:
            print_failure("format_connection_uri() failed tests.", 
                          "Expected format_connection_uri('localhost', 5432, 'analytics') -> 'postgresql://localhost:5432/analytics'. Host/DB must be non-empty strings and port must be integer.")
            success = False
    except Exception as e:
        print_failure("format_connection_uri() raised an error during execution.", str(e))
        success = False

    return success


def run_strings_tests():
    print_header("Challenge 2: Strings - Web Server Log Parser")
    try:
        from challenges.challenge_2_strings import clean_log_line, parse_log_timestamp, check_error_severity, parse_csv_row
    except Exception as e:
        print_failure("Could not import functions from challenges.challenge_2_strings", str(e))
        return False

    success = True

    # Test clean_log_line
    try:
        t1 = clean_log_line('  "2026-07-10 | ERROR | Connection failure"  ') == '2026-07-10 | ERROR | Connection failure'
        t2 = clean_log_line("  '2026-07-10 14:35:22' \t") == "2026-07-10 14:35:22"
        if t1 and t2:
            print_success("clean_log_line() works correctly.")
        else:
            print_failure("clean_log_line() failed tests.", "Ensure you strip outer whitespace and both double and single quotes.")
            success = False
    except Exception as e:
        print_failure("clean_log_line() raised an error.", str(e))
        success = False

    # Test parse_log_timestamp
    try:
        t1 = parse_log_timestamp("2026-07-10 14:35:22 | ERROR | DB failed") == "2026-07-10 14:35:22"
        t2 = parse_log_timestamp("short log") is None
        if t1 and t2:
            print_success("parse_log_timestamp() works correctly.")
        else:
            print_failure("parse_log_timestamp() failed tests.", "Extract the first 19 characters. Return None if line length is less than 19.")
            success = False
    except Exception as e:
        print_failure("parse_log_timestamp() raised an error.", str(e))
        success = False

    # Test check_error_severity
    try:
        t1 = check_error_severity("2026-07-10 | ERROR | Connection failure") is True
        t2 = check_error_severity("warning: Disk partition almost full") is True
        t3 = check_error_severity("INFO: pipeline complete") is False
        if t1 and t2 and t3:
            print_success("check_error_severity() works correctly.")
        else:
            print_failure("check_error_severity() failed tests.", "Ensure case-insensitive check for 'error' or 'warning'.")
            success = False
    except Exception as e:
        print_failure("check_error_severity() raised an error.", str(e))
        success = False

    # Test parse_csv_row
    try:
        t1 = parse_csv_row("  101 , John Doe ,  Software Engineer  ") == ["101", "John Doe", "Software Engineer"]
        t2 = parse_csv_row("a,b,c,d") == ["a", "b", "c", "d"]
        if t1 and t2:
            print_success("parse_csv_row() works correctly.")
        else:
            print_failure("parse_csv_row() failed tests.", "Split the row by commas and strip whitespace from each element.")
            success = False
    except Exception as e:
        print_failure("parse_csv_row() raised an error.", str(e))
        success = False

    return success


def run_numbers_tests():
    print_header("Challenge 3: Numbers - Metric Calculator & Sensor Validator")
    try:
        from challenges.challenge_3_numbers import calculate_pipeline_throughput, round_financial_metric, validate_sensor_reading
    except Exception as e:
        print_failure("Could not import functions from challenges.challenge_3_numbers", str(e))
        return False

    success = True

    # Test calculate_pipeline_throughput
    try:
        t1 = calculate_pipeline_throughput(10500, 3.5) == 3000.0
        t2 = calculate_pipeline_throughput(100, 3) == 33.33
        t3 = calculate_pipeline_throughput(100, 0) == 0.0
        t4 = calculate_pipeline_throughput(100, -2) == 0.0
        if t1 and t2 and t3 and t4:
            print_success("calculate_pipeline_throughput() works correctly.")
        else:
            print_failure("calculate_pipeline_throughput() failed tests.", "Compute throughput as rows/seconds, rounded to 2 decimal places. Return 0.0 if duration <= 0.")
            success = False
    except Exception as e:
        print_failure("calculate_pipeline_throughput() raised an error.", str(e))
        success = False

    # Test round_financial_metric
    try:
        t1 = round_financial_metric(-123.4567) == 123.46
        t2 = round_financial_metric(88.1) == 88.1
        if t1 and t2:
            print_success("round_financial_metric() works correctly.")
        else:
            print_failure("round_financial_metric() failed tests.", "Return absolute value of amount rounded to 2 decimal places.")
            success = False
    except Exception as e:
        print_failure("round_financial_metric() raised an error.", str(e))
        success = False

    # Test validate_sensor_reading
    try:
        t1 = validate_sensor_reading(45) == (True, True)
        t2 = validate_sensor_reading(45.0) == (True, True)
        t3 = validate_sensor_reading(45.67) == (True, False)
        t4 = validate_sensor_reading("45") == (False, False)
        t5 = validate_sensor_reading(None) == (False, False)
        if t1 and t2 and t3 and t4 and t5:
            print_success("validate_sensor_reading() works correctly.")
        else:
            print_failure("validate_sensor_reading() failed tests.", "Return (is_numeric, is_whole_number) as a tuple.")
            success = False
    except Exception as e:
        print_failure("validate_sensor_reading() raised an error.", str(e))
        success = False

    return success


def run_logic_tests():
    print_header("Challenge 4: Logic - ETL Data Quality Gate")
    try:
        from challenges.challenge_4_logic import is_record_valid, validate_batch_quality, alert_on_failures
    except Exception as e:
        print_failure("Could not import functions from challenges.challenge_4_logic", str(e))
        return False

    success = True

    # Test is_record_valid
    try:
        t1 = is_record_valid({"id": 1, "email": "test@analytics.com", "status": "ACTIVE"}) is True
        t2 = is_record_valid({"id": -5, "email": "test@analytics.com", "status": "ACTIVE"}) is False
        t3 = is_record_valid({"id": 1, "email": "test@analytics.com", "status": "INACTIVE"}) is False
        t4 = is_record_valid({"id": 1, "email": "test_analytics_com", "status": "ACTIVE"}) is False
        t5 = is_record_valid({"id": 1, "email": "test@analytics.org", "status": "PENDING"}) is True
        t6 = is_record_valid({"id": 1, "email": "test@analytics.net", "status": "ACTIVE"}) is True
        t7 = is_record_valid({"email": "test@analytics.com", "status": "ACTIVE"}) is False
        if t1 and not t2 and not t3 and not t4 and t5 and t6 and not t7:
            print_success("is_record_valid() works correctly.")
        else:
            print_failure("is_record_valid() failed tests.", "Check ID > 0, status is ACTIVE/PENDING, and email is non-empty string with '@' ending in .com/.org/.net.")
            success = False
    except Exception as e:
        print_failure("is_record_valid() raised an error.", str(e))
        success = False

    # Test validate_batch_quality
    try:
        t1 = validate_batch_quality([True, True, True]) is True
        t2 = validate_batch_quality([True, False, True]) is False
        t3 = validate_batch_quality([]) is False
        if t1 and not t2 and not t3:
            print_success("validate_batch_quality() works correctly.")
        else:
            print_failure("validate_batch_quality() failed tests.", "Return True if list is not empty and all elements are True.")
            success = False
    except Exception as e:
        print_failure("validate_batch_quality() raised an error.", str(e))
        success = False

    # Test alert_on_failures
    try:
        t1 = alert_on_failures([False, False, True]) is True
        t2 = alert_on_failures([False, False]) is False
        t3 = alert_on_failures([]) is False
        if t1 and not t2 and not t3:
            print_success("alert_on_failures() works correctly.")
        else:
            print_failure("alert_on_failures() failed tests.", "Return True if any element in list is True.")
            success = False
    except Exception as e:
        print_failure("alert_on_failures() raised an error.", str(e))
        success = False

    return success


def main():
    print(f"\n{BOLD}{YELLOW}========================================={RESET}")
    print(f"{BOLD}{YELLOW}   DATA ENGINEERING PYTHON TEST RUNNER   {RESET}")
    print(f"{BOLD}{YELLOW}========================================={RESET}")

    results = {
        "Basics (Challenge 1)": run_basics_tests(),
        "Strings (Challenge 2)": run_strings_tests(),
        "Numbers (Challenge 3)": run_numbers_tests(),
        "Logic (Challenge 4)": run_logic_tests()
    }

    print_header("SUMMARY")
    passed_count = 0
    for name, success in results.items():
        status = f"{GREEN}PASSED{RESET}" if success else f"{RED}FAILED{RESET}"
        if success:
            passed_count += 1
        print(f"  {name:<25}: {status}")

    print(f"\n{BOLD}Total Progress: {passed_count}/4 Challenges Completed.{RESET}")
    if passed_count == 4:
        print(f"\n{GREEN}🎉 Congratulations! You have successfully solved all challenges!{RESET}\n")
    else:
        print(f"\n{YELLOW}💡 Keep going! Fix the failed functions and run `python run_tests.py` again.{RESET}\n")

if __name__ == "__main__":
    main()
