class RepostService:
    def __init__(
        self,
        vk_api,
        vk_group_id,
        telegram_api,
        telegram_channel_id,
        store
    ):
        self.__vk_api = vk_api
        self.__vk_group_id = vk_group_id
        self.__telegram_api = telegram_api
        self.__telegram_channel_id = telegram_channel_id
        self.__store = store

    def repost_latest(self):
        post = self.__vk_api.get_latest_group_post(
            self.__vk_group_id
        )

        if not self.__store.has(post):
            self.__store.push(post)
            self.__telegram_api.publish_to_channel(
                self.__telegram_channel_id, post
            )
