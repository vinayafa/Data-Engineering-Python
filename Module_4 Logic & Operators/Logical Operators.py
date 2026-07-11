# Logical operators combine boolean expressions.

# and returns True only if both conditions are True.
print(3 > 1 and 5 < 1)
print(3 > 1 and 5 > 1)

# or returns True if at least one condition is True.
print(3 > 1 or 5 < 1)
print(3 > 1 or 5 > 1)

# Real-life example: check whether a system is under pressure.
# If CPU or memory is above 90%, the system may need attention.
cpu_usage = 70
memory_usage = 50
print(cpu_usage > 90 or memory_usage > 90)

# Definition: and needs both conditions to be True, while or needs only one condition to be True.