from database import Database
from models.blog import Blog

Database.initialize()

blog = Blog(author="Mihai", title="Blog title1", description="Blog description1")
blog.save_to_mongo()

blog.new_post()

from_database = Blog.from_mongo(blog.id)
print(blog.get_posts())

