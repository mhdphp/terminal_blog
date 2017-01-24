import uuid
from database import Database
from models.post import Post
import datetime

class Blog(object):

    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id


    def new_post(self):
        title = input('Enter the post title: ')
        content = input('Enter the content of the post: ')
        date = input('Enter the post date or leave it blank for today (in format DDMMYYYY): ')
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        post = Post(blog_id = self.id,
                    title = title,
                    content = content,
                    author = self.author,
                    created_date = date
                    )
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)


    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())


    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    # @staticmethod
    # def get_from_mongo(id):
    #     blog_data = Database.find_one(collection='blogs',
    #                                   query={'id':id})
    #     return Blog(author=blog_data['author'],
    #                 title=blog_data['title'],
    #                 description=blog_data['description'],
    #                 id=blog_data['id'])


    # @classmethod instead of staticmethod
    @classmethod
    # cls substitutes the current class
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs',
                                      query={'id':id})
        return cls(author = blog_data['author'],
                   title = blog_data['title'],
                   description = blog_data['description'],
                   id = blog_data['id'])
