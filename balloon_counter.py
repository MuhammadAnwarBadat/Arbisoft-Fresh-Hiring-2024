def count_balloons(pattern, start_index, end_index):
    """Counts the number of balloons of each color within a specified range.

    Args:
        pattern: A string representing the balloon pattern.
        start_index: The starting index of the range (inclusive).
        end_index: The ending index of the range (inclusive).

    Returns:
        A string containing the counts of blue, orange, and white balloons, in that order.
    """

    balloon_counts = {"b": 0, "o": 0, "w": 0}
    pattern_length = len(pattern)

    for i in range(start_index, end_index + 1):
        balloon_index = i % pattern_length
        color = pattern[balloon_index]
        balloon_counts[color] += 1

    # Ensure consistent color order (blue, orange, white)
    result = "b{}o{}w{}".format(balloon_counts["b"], balloon_counts["o"], balloon_counts["w"])
    return result

# Read input from the file "input.txt"
with open("input.txt", "r") as file:
    pattern = file.readline().strip()
    start_index = int(file.readline().strip())
    end_index = int(file.readline().strip())

# Calculate and print the balloon counts
balloon_counts = count_balloons(pattern, start_index, end_index)
print(balloon_counts)