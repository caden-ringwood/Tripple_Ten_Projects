def fibonacci_sequence(n):
    result = []
    a = 0
    b = 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


# This implementation contains several bugs
def calculate_fibonacci_stats(sequence_length):
    sequence = fibonacci_sequence(sequence_length)
    stats = {
        "sequence": sequence,
        "average": sum(sequence) / len(sequence),
        "maximum": max(sequence),
        "minimum": min(sequence),
        "length": len(sequence),
    }
    return stats
