from utils.api import Todo_list_api
from utils.checking import Checking
import json
"""Create, change and delete new task"""
class Test_create_task():

    def test_create_new_task(self):

        print("\nMethod POST")
        result_post = Todo_list_api.create_new_task()
        check_post = result_post.json()
        task_id = check_post.get("id")
        Checking.check_status_code(result_post, 201)
        Checking.check_json_token(result_post, ['id', 'title', 'completed', 'order', 'url'])
        Checking.check_json_value(result_post, 'completed', False)
        Checking.check_json_search_word_in_value(result_post, 'title', 'API')

        print("Method GET-POST")
        result_get = Todo_list_api.get_new_task(task_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['id', 'title', 'completed', 'order', 'url'])
        Checking.check_json_value(result_get, 'completed', False)

        print("Method PATCH")
        result_patch = Todo_list_api.patch_new_task(task_id)
        Checking.check_status_code(result_patch, 200)
        Checking.check_json_token(result_patch, ['id', 'title', 'completed', 'order', 'url'])
        Checking.check_json_value(result_patch, 'completed', True)

        print("Method GET-PATCH")
        result_get = Todo_list_api.get_new_task(task_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['id', 'title', 'completed', 'order', 'url'])
        Checking.check_json_value(result_get, 'completed', True)

        print("Method DELETE")
        result_delete = Todo_list_api.delete_new_task(task_id)
        Checking.check_status_code(result_delete, 204)

        print("Method GET-DELETE")
        result_get = Todo_list_api.get_new_task(task_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['status', 'message'])
        Checking.check_json_value(result_get, 'status', 404)
        Checking.check_json_search_word_in_value(result_get, 'message', 'Todo with identifier')
        # token = json.loads(result_get.text)
        # print(list(token))
