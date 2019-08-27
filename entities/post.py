class Post:
    def __init__(self, _id, text):
        self.__id = _id
        self.__text = text

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f'id:   {self.__id}\n' \
               f'text: {self.__text}\n'
