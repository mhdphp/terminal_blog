from database import Database
from models.post import Post

Database.initialize()

# create a post and save it in the database
# post = Post(blog_id="123",
#             title="A second blog title",
#             content="Some content for the second post",
#             author="Mykky")
#
# post.save_to_mongo()

# display the post
#post = Post.from_mongo("64641986527042e8a744430fd037cebe")
#print(post)

# displays all the posts from blog_id = '123'
posts = Post.from_blog('123')
#loop through the posts
for post in posts:
    print(post)




