import requests


def test_server_message() -> None:
    """
    Function to test server message.

    Returns:
        None
    """
    try:
        url = "http://127.0.0.1:8080/api/chat/message"
        data = {"session_id": "1", "msg": "可以简要介绍一下你自己吗？", "actor_id": "1"}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Success. message response body: ", response.text)
        else:
            print(f"Request failed with status code {response.status_code}")
    except Exception as e:
        print("Please start the server first.")
        print("Request failed with exception: ", e)


if __name__ == "__main__":
    test_server_message()
