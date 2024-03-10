def alternate(s):
    unique_chars = set(s)
    max_length = 0

    for char1 in unique_chars:
        for char2 in unique_chars:
            if char1 != char2:
                filtered_str = [c for c in s if c in (char1, char2)]
                valid = all(filtered_str[i] != filtered_str[i + 1] for i in range(len(filtered_str) - 1))

                if valid:
                    max_length = max(max_length, len(filtered_str))

    return max_length
