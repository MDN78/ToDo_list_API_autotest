import json
"""Method's for checking answers"""

class Checking():
    """Method for checking status code"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print(f"Success! Status code = {result.status_code}")

    """Method for checking fields"""
    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value
        print("All fields exists")

    """Method for checking values in jsons fields"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f"Field '{field_name}' is right!")

    """Method for checking certain values in jsons fields"""
    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info
        print(f"Phrase '{search_word}' exist!")
