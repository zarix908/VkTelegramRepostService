import vk

from entities.post import Post
from utils import try_get_item


class VkApi:
    def __init__(self, access_token):
        session = vk.Session(access_token=access_token)
        self.__api = vk.API(session)

    def get_latest_group_post(self, group_id):
        response = self.__api.wall.get(
            owner_id=group_id,
            count=1,
            v='5.101'
        )

        last_post = self.extract_last_post(response)

        if not last_post:
            return None

        return Post(
            last_post.get('id'),
            last_post.get('text')
        )

    def extract_last_post(self, response):
        posts = response.get('items')
        return try_get_item(posts, 0)
