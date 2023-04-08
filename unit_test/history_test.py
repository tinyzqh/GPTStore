from src.utils.history_utils import construct_fragment
from src.history.history_buffer import HistoryBuffer, Fragment, history_buffer_add


def test_construct_fragment():
    """
    This function is used to test the construct fragment function.
    """
    fragment = construct_fragment(timestamp=0, query="你好", response="你好")
    assert isinstance(fragment, Fragment), "The type of fragment is not Fragment."
    print("Success test_construct_fragment !")


def test_history_buffer():
    """
    This function is used to test the history buffer.
    """
    history_buffer = HistoryBuffer()
    history_buffer.add(role="ielts", session_id="0", fragment=construct_fragment(0, "你好", "你好"))
    history_buffer.add(role="ielts", session_id="0", fragment=construct_fragment(1, "你叫什么名字", "我叫ielts"))
    history_buffer.add(role="ielts", session_id="0", fragment=construct_fragment(2, "你是谁", "我是ielts"))
    history_buffer.get(role="ielts", session_id="0")
    print("Success test_history_buffer!")


def test_history_buffer_add():
    """
    This function is used to test the history buffer add function.
    """
    history_buffer = HistoryBuffer()
    history_buffer_add(history_buffer=history_buffer, role="ielts", session_id="0", query="你好", response="你好")

    history_buffer.add(role="ielts", session_id="0", fragment=construct_fragment(0, "你好", "你好"))
    history_buffer.add(role="ielts", session_id="0", fragment=construct_fragment(1, "你叫什么名字", "我叫ielts"))
    history_buffer.add(role="ielts", session_id="0", fragment=construct_fragment(2, "你是谁", "我是ielts"))
    history_buffer.add(role="ielts", session_id="0", fragment=construct_fragment(0, "你好", "你好"))
    history_buffer.add(role="ielts", session_id="0", fragment=construct_fragment(1, "你叫什么名字", "我叫ielts"))

    history_buffer_add(history_buffer=history_buffer, role="ielts", session_id="0", query="你好", response="你好")
    print("Success test_history_buffer_add!")


if __name__ == "__main__":
    test_construct_fragment()
    test_history_buffer()
    test_history_buffer_add()
