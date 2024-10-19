def sort_transients_price(transients, sort_choice):
    """

    @param transients:
    @param sort_choice:
    @return:
    """
    if sort_choice == "asc":
        return sorted(transients, key=lambda x: x["price_per_head"])
    elif sort_choice == "desc":
        return sorted(transients, key=lambda x: x["price_per_head"], reverse=True)


def filter_transients(transients, filter_choice, filter_query):
    """

    @param transients:
    @param filter_choice:
    @param filter_query:
    @return:
    """
    if filter_choice == 1:
        return [t for t in transients if filter_query.lower() in t["name"].lower()]
    elif filter_choice == 2:
        return [t for t in transients if filter_query.lower() in t["location"].lower()]
    return transients