from user import User
from post import Post

app_user_one = User("bobbyyyyy16@gmail.com", "Abhishek", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("aa@bb.com", "bobby", "supersecret", "devrel")
app_user_two.get_user_info()

new_post = Post("meeting with new developer", app_user_two.name)
new_post.get_post_info()
