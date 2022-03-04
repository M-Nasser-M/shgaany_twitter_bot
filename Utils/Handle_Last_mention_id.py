def get_last_mention_id():
    try:
        with open("last_mention_id.txt", "r") as fr:
            file_content = fr.read()
            last_seen_id = file_content.strip()
            fr.close()
            return last_seen_id
    except FileNotFoundError:
        with open("last_mention_id.txt", "w") as fw:
            fw.write("")
            return ""


def write_last_mention_id(last_seen_id):
    with open("last_mention_id.txt", "w") as fw:
        fw.write(str(last_seen_id))
        fw.close()
