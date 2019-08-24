import unittest
from unittest.mock import Mock, MagicMock
from repost_service import RepostService


class TestRepostService(unittest.TestCase):
    def setUp(self):
        self.__vk_api = Mock()
        self.__vk_group_id = 'group_id'

        self.__telegram_api = Mock()
        self.__telegram_channel_id = 'channel_id'

        self.__store = Mock()

        self.__repost_service = RepostService(
            self.__vk_api,
            self.__vk_group_id,
            self.__telegram_api,
            self.__telegram_channel_id,
            self.__store
        )

        self.__post = Mock()
        self.__post.id = 'post_id'

    def test_publish_new_post(self):
        self.__vk_api.get_latest_group_post = MagicMock(
            return_value=self.__post
        )
        self.__telegram_api.publish_to_channel = MagicMock()
        self.__store.has = MagicMock(
            return_value=False
        )

        self.__repost_service.repost_latest()

        self.__telegram_api.publish_to_channel \
            .assert_called_once_with(
                self.__telegram_channel_id, self.__post
            )

    def test_add_new_post_to_store(self):
        self.__vk_api.get_latest_group_post = MagicMock(
            return_value=self.__post
        )
        self.__store.has = MagicMock(
            return_value=False
        )
        self.__store.push = MagicMock()

        self.__repost_service.repost_latest()

        self.__store.push.assert_called_once_with(
            self.__post
        )

    def test_not_publish_published_post(self):
        self.__vk_api.get_latest_group_post = MagicMock(
            return_value=self.__post
        )
        self.__telegram_api.publish_to_channel = MagicMock()
        self.__store.has = MagicMock(
            return_value=True
        )

        self.__repost_service.repost_latest()

        self.__telegram_api.publish_to_channel \
            .assert_not_called()

    def test_not_add_published_post_to_store(self):
        self.__vk_api.get_latest_group_post = MagicMock(
            return_value=self.__post
        )
        self.__store.has = MagicMock(
            return_value=True
        )
        self.__store.push = MagicMock()

        self.__repost_service.repost_latest()

        self.__store.push.assert_not_called()
