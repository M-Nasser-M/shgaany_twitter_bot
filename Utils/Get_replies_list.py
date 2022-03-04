def get_reply_list():
    with open("replies.txt", "r", encoding='utf-8') as fr:
        replies = fr.readlines()
        cleaned_replies = []
        for reply in replies:
            cleaned_replies.append(reply.replace('\n', ''))
        return cleaned_replies
