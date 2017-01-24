from database import Database
from models.blog import Blog


class Menu(object):

    def __init__(self):
        # ask user for author name
        self.user = input("Enter you author name: ")
        self.user_blog = None
        # Check if they're already have an account
        # if not, prompt then the create one
        # underscore means that these methods are private methods,
        # could be accessed only from this class (developer convention)
        if self._user_has_account():
            print("Welcome, back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        # returns true or false
        blog = Database.find_one(collection='blogs', query={'author': self.user})
        if blog is not None:
            # save the existing blog of the user in the object user_blog
            # self.user_blog = blog
            # better to work with a object than with data as in precedent example
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input('Enter blog title: ')
        description = input('Enter blog description: ')
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        # save the object blog new created in user_blog object
        self.user_blog = blog


    def run_menu(self):
        # User want to read or write blogs?
        read_or_write = input('Do you want to read (R) or write (W)? ')
        # if read
        if read_or_write == 'R':
            # list blogs in database
            self._list_blogs()
            # allow user to pick one
            self._view_blog()
            # display posts in the blog
        elif read_or_write == 'W':
        #if they want to write, user_blog is an object
            self.user_blog.new_post()
        else:
            print('Thank you for blogging!')

    # list all the blogs from the collection 'blogs'
    def _list_blogs(self):
        # get all the blogs from the collection 'blogs'
        blogs = Database.find(collection='blogs', query={})

        #print all the blogs from the blogs
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blog(self):
        blog_to_see = input('Please enter the Id of the blog you want: ')
        # get the blog based on its id = blog_to_see
        blog = Blog.from_mongo(blog_to_see)
        # get all posts from the blog
        posts = blog.get_posts()
        # print all posts
        for post in posts:
            print("Date: {}, Title: {}\n\n{}".format(post['created_date'], post['title'], post['content']))