import requests
from MyInstagramClient import MyInstagramClient

COMMENTS_NUMBER = 1000

class InstagramApi():
    api = None
    
    def __init__(self, username, password):
        self.api = MyInstagramClient(username=username, password=password)

    def _login_success_callback():
        print("Login Success")

    def _get_media_id(self, post_hash):
        res = requests.get("https://api.instagram.com/oembed/?url=https://www.instagram.com/p/{}/".format(post_hash))
        return res.media_id

    def _write_usernames_txt(self, usernames):
        with open('usernames.txt', 'w') as writer:
            for u in usernames:
                writer.write(u + "\n")

    def _return_media_n_comments(self, post_hash, post_number_comments):
        media_id = MEDIA_ID if MEDIA_ID != None else self._get_media_id(post_hash)

        return self.api.media_n_comments(media_id=media_id, n=post_number_comments)

    def return_all_comments_users(self, post_hash, post_number_comments):
        comments = self._return_media_n_comments(post_hash, post_number_comments)
        
        usernames = []
        for comment in comments:
            usernames.append(result['user']['username'])

        self._write_usernames_txt(usernames)

        return usernames