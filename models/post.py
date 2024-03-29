from common.database import Database
import uuid
import datetime

class Post(object):

    def __init__(self, blog_id, title, content, author, created_date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json())

    def json(self):
        return {
            '_id':self._id,
            'blog_id':self.blog_id,
            'author':self.author,
            'content':self.content,
            'title':self.title,
            'created_date':self.created_date
        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'_id':id})
        #return cls(post_data['blog_id'],post_data['title'],post_data['content'],
        #            post_data['author'],post_data['created_date'],post_data['_id'])
        return cls(**post_data)     #do the same thing

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find('posts', {'blog_id':id})]
