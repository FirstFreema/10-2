import json
import pickle


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}"

    def pack_json(self):
        return json.dumps(self, cls=BookJSONEncoder)

    def pack_pickle(self):
        return pickle.dumps(self)

    @classmethod
    def unpack_json(cls, data):
        book_data = json.loads(data)
        return cls(book_data["title"], book_data["author"], book_data["genre"])

    @classmethod
    def unpack_pickle(cls, data):
        return pickle.loads(data)


class BookJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return {
                "title": obj.title,
                "author": obj.author,
                "genre": obj.genre
            }
        return super().default(obj)