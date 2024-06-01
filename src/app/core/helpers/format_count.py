def format_count(count: int):
    if not isinstance(count, int):
        return count

    if count > 1000:
        return f"{(count / 1000):.1f}K"

    return str(count)
