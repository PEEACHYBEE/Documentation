def sort_transients_price(transients, sort_choice):
    """Sort a list of transients by price per head.

    Args:
        transients (list): A list of transient dictionaries to be sorted.
        sort_choice (str): The sort order, either "asc" for ascending or "desc" for descending.

    Returns:
        list: A sorted list of transients based on the specified sort order.
    """
    if sort_choice == "asc":
        return sorted(transients, key=lambda x: x["price_per_head"])
    elif sort_choice == "desc":
        return sorted(transients, key=lambda x: x["price_per_head"], reverse=True)


def filter_transients(transients, filter_choice, filter_query):
    """Filter a list of transients based on the specified criteria.

    Args:
        transients (list): A list of transient dictionaries to be filtered.
        filter_choice (int): The filtering criteria (1 for name, 2 for location).
        filter_query (str): The query to filter the transients by.

    Returns:
        list: A list of transients that match the filtering criteria.
    """
    if filter_choice == 1:
        return [t for t in transients if filter_query.lower() in t["name"].lower()]
    elif filter_choice == 2:
        return [t for t in transients if filter_query.lower() in t["location"].lower()]
    return transients
