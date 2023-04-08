class Fragment:
    """
    Fragment of the conversation.
    """

    timestamp: int
    query: str
    response: str


def construct_fragment(timestamp: int, query: str, response: str) -> Fragment:
    """
    Construct a fragment of the conversation.

    Args:
        timestamp (int): Timestamp.
        Query (str): Query.
        Response (str): Response.

    Returns:
        fragment (Fragment): Fragment of the conversation. (timestamp, Query, Response)
    """
    fragment = Fragment()
    fragment.timestamp = timestamp
    fragment.query = query
    fragment.response = response
    return fragment
