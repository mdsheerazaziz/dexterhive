def format_timestamp(timestamp):
    """

    Args:
        timestamp: Timestamp with date time seperated by T

    Returns:
        Timestamp in "date time" format

    """
    modified_date = None
    if timestamp:
        modified_timestamp = timestamp.split('T')
        modified_date = modified_timestamp[0] + " " + modified_timestamp[1][:8]
    return modified_date
