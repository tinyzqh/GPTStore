import collections
from typing import Tuple, List

from src.utils.role_utils import role2actorid
from src.utils.history_utils import Fragment, construct_fragment


class HistoryBuffer(object):
    """
    Store the history of the conversation.
    """

    def __init__(self, max_length: int = 15) -> None:
        """
        Initialize the history buffer.

        Args:
            max_length (int): Maximum length of the history buffer.

        Returns:
            None
        """
        self.max_length = max_length
        self.history_buffer = {role: {} for role in role2actorid}

    def add(self, role: str, session_id: str, fragment: Fragment) -> None:
        """
        Add a message to the history buffer.

        Args:
            role (str): Role name.
            session_id (str): Session ID.
            fragment (Fragment): Fragment of the conversation. (timestamp, Query, Response)

        Returns:
            None
        """
        assert role in self.history_buffer, "Role name is not valid."
        if session_id not in self.history_buffer[role]:
            self.history_buffer[role][session_id] = collections.deque(maxlen=self.max_length)
        self.history_buffer[role][session_id].append(fragment)

    def get(self, role: str, session_id: str) -> List[Tuple[int, str, str]]:
        """
        Get the history of a session.

        Args:
            role (str): Role name.
            session_id (str): Session ID.

        Returns:
            history (List[Tuple[int, str, str]]): History of the session.
        """
        assert role in self.history_buffer, "Role name is not valid."
        if session_id in self.history_buffer[role]:
            return list(self.history_buffer[role][session_id])
        else:
            return list()

    def get_timestamp(self, role: str, session_id: str) -> int:
        """
        Get the timestamp of the last message in the history buffer.

        Args:
            role (str): Role name.
            session_id (str): Session ID.

        Returns:
            timestamp (int): Timestamp of the last message.
        """
        assert role in self.history_buffer, "Role name is not valid."
        if session_id in self.history_buffer[role]:
            return self.history_buffer[role][session_id][-1].timestamp
        else:
            return -1

    def save(self, path: str) -> None:
        """
        Save the history buffer to a file.

        Args:
            path (str): File path.

        Returns:
            None
        """
        pass


def history_buffer_add(history_buffer: HistoryBuffer, role: str, session_id: str, query: str, response: str) -> None:
    """
    Add a message to the history buffer.

    Args:
        history_buffer (HistoryBuffer): History buffer.
        role (str): Role name.
        session_id (str): Session ID.
        query (str): Query.
        response (str): Response.

    Returns:
        None
    """
    timestamp = history_buffer.get_timestamp(role=role, session_id=session_id)
    fragment = construct_fragment(timestamp=timestamp + 1, query=query, response=response)
    history_buffer.add(role, session_id, fragment)
