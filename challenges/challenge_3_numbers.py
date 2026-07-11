# Challenge 3: Numbers - Metric Calculator & Sensor Validator
# Complete the functions below to perform arithmetic, rounding, and type validations.

def calculate_pipeline_throughput(rows_processed, duration_seconds):
    """
    Data Engineering context: Performance metrics are calculated to track the efficiency 
    of ETL jobs. We compute rows processed per second and round it.

    Task:
    - If duration_seconds is 0 or negative, return 0.0.
    - Calculate throughput as: rows_processed / duration_seconds.
    - Round the result to 2 decimal places and return it as a float.

    Example:
    calculate_pipeline_throughput(10500, 3.5) -> 3000.0
    calculate_pipeline_throughput(100, 3) -> 33.33
    """
    # TODO: Implement this function
    pass


def round_financial_metric(amount):
    """
    Data Engineering context: Aligning financial transactional figures to a unified standard decimal precision.

    Task:
    - Return the absolute value of `amount` rounded to 2 decimal places.
    - (Hint: use abs() first, then round(value, 2)).

    Example:
    round_financial_metric(-123.4567) -> 123.46
    round_financial_metric(88.1) -> 88.1
    """
    # TODO: Implement this function
    pass


def validate_sensor_reading(value):
    """
    Data Engineering context: Validating data types of raw stream ingestion inputs.

    Task:
    - Determine if the variable `value` is numeric (either an instance of `int` or `float`).
      Hint: use isinstance() or compare type.
    - If it is numeric:
      - Determine if it represents a whole number (i.e. has no decimal fraction).
        Hint: For a float, you can use `.is_integer()`. For an int, it's always a whole number.
      - Return a tuple: `(True, is_whole_number_boolean)`
    - If it is not numeric:
      - Return a tuple: `(False, False)`

    Example:
    validate_sensor_reading(45) -> (True, True)
    validate_sensor_reading(45.0) -> (True, True)
    validate_sensor_reading(45.67) -> (True, False)
    validate_sensor_reading("45") -> (False, False)
    """
    # TODO: Implement this function
    pass
