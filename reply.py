from Config import Config_api
from Utils import Handle_Last_mention_id
import random


def reply_to_mentions(replies):
    last_mention_id = Handle_Last_mention_id.get_last_mention_id()
    if last_mention_id:
        mentions = Config_api.api.mentions_timeline(since_id=last_mention_id)
    else:
        mentions = Config_api.api.mentions_timeline(count=50)
    if len(mentions) > 0:
        for mention in reversed(mentions):
            screen_name = mention.user.screen_name
            last_mention_id = mention.id
            try:
                reply = replies[random.randint(0, (len(replies) - 1))]
                Config_api.client.create_tweet(in_reply_to_tweet_id=mention.id,
                                               text=f"@{screen_name} {reply}")
            except Exception:
                print("api limit probably reached")
    else:
        print("no new mentions to reply to")

    Handle_Last_mention_id.write_last_mention_id(last_mention_id)
