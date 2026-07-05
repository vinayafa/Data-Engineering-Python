# split() breaks a string into smaller pieces.
# If we use a space as the separator, Python splits the date and time apart.
stamp = "2026-09-20 14:40"
print(stamp.split(" "))

# A comma-separated string can also be split into a list.
# The spaces around some values stay in the output because split() only uses the comma here.
csv_file = "1234, Max , USA , 1970-10-05,M"
print(csv_file.split(","))