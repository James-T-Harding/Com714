def describe_friend(name):
    """

    :param name: Friend name
    :return: Friend Description
    """

    friend_dict = {"50 Cent": "He be getting rich or die trying.",
                   "Dr Dre": "He be needing California love.",
                   "Rihanna": "She be needing an umbrella."}

    low = name.lower()

    return friend_dict[low] if low in friend_dict else "They be cool"


def get_desc(friend):
    print(f"The ")
