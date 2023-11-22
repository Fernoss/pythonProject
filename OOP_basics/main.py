from user import User
from post import Post

# creating an object
app_user_one = User("jj@jj.com", "Jon Jonsson", "pwd1", "DevOps Engineer")

# trying the function get_user_info of class User
app_user_one.get_user_info()

# trying the function change_job_title of class User
app_user_one.change_job_title("Head of DevOps")
app_user_one.get_user_info()

# Post class object creation
new_post = Post("Working with Jira", app_user_one.name)
new_post.get_post_info()
