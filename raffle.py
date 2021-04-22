
from random import randrange
from instagram_api import InstagramApi

COMMENTS_NUMBER = 1000

class Raffle():
    instagram_client = None

    def __init__(self, username, password):
        self.instagram_client = InstagramApi(username, password)

    def _get_random_user(self, max):
        return randrange(max)

    def raffle(self, post_hash, post_number_comments):
        usernames = self.instagram_client.return_all_comments_users(post_hash, post_number_comments)
        index = self._get_random_user(len(usernames))
        return usernames[index]

