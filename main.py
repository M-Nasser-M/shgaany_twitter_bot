import time
from Utils import Get_replies_list
from reply import reply_to_mentions

reply_list = Get_replies_list.get_reply_list()

while True:
    reply_to_mentions(reply_list)
    time.sleep(13)
