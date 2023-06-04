from utils.http_method import Http_methods
import random
base_url = "https://todo-app-sky.herokuapp.com/"
my_list = ['API Autotest_1', 'API Autotest_2', 'API Autotest_3', 'API Autotest_4', 'API Autotest_5']
class Todo_list_api():

    """creating new task"""
    @staticmethod
    def create_new_task():
        random_name = random.choice(my_list)
        json_create_new_task = {
            "title": random_name,
            "completed": False
        }
        post_url = base_url
        print(post_url)
        result_post = Http_methods.post(post_url, json_create_new_task)
        print(result_post.text)
        return result_post

    """checking created task"""
    @staticmethod
    def get_new_task(task_id):
        get_url = base_url + str(task_id)
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """cross created task"""
    @staticmethod
    def patch_new_task(task_id):
        patch_url = base_url + str(task_id)
        print(patch_url)
        json_cross_created_task = {"completed": True}
        result_patch = Http_methods.patch(patch_url, json_cross_created_task)
        print(result_patch.text)
        return result_patch

    """delete crossed task"""
    @staticmethod
    def delete_new_task(task_id):
        delete_url = base_url + str(task_id)
        print(delete_url)
        result_delete = Http_methods.delete(delete_url)
        print(result_delete.text)
        return result_delete
