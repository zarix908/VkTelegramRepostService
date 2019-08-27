def try_get_item(_list, index):
    if index is None:
        return None

    if index < 0:
        raise ValueError('index must be >= 0')
    elif index > len(_list):
        return None

    return _list[index]
