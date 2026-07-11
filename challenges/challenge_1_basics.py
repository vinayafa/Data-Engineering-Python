# Challenge 1: Basics - Database Config Loader
# Complete the functions below to load database connection details.

def load_db_port(port_str):
    """
    Data Engineering context: Connection inputs from environment variables or UI prompts 
    always arrive as strings. We must safely convert them to integers.

    Task:
    - Convert the parameter `port_str` to an integer.
    - If conversion is successful, return the port integer.
    - If the conversion fails (e.g. ValueError), return None.

    Example:
    load_db_port("5432") -> 5432
    load_db_port("invalid") -> None
    """
    # TODO: Implement this function
    pass


def format_connection_uri(host, port, db_name):
    """
    Data Engineering context: Building database connection strings programmatically.

    Task:
    - Check if host and db_name are non-empty strings, and port is an integer.
      (Hint: use isinstance() or simple truthiness checks).
    - If the inputs are valid, return a connection string in the format:
      "postgresql://host:port/db_name"
    - If inputs are invalid or missing, return None.

    Example:
    format_connection_uri("localhost", 5432, "analytics") -> "postgresql://localhost:5432/analytics"
    format_connection_uri("", 5432, "analytics") -> None
    """
    # TODO: Implement this function
    pass
