# Blog Content
#
* [Back to README Home page](/README.md)
## Navigating Features
* [Features](#features)
   - [Existing features](#existing-features)
   - [Possible improvements](#features-left-to-implement)
#
## Features

### Existing features
#
#### Front page and media query
#
![Front page](/media/not_login.jpeg)  | ![Front page](/media/loggedin.jpeg)
#

![Front page small screen](/media/pageview_sm_screen.jpeg) |![SignUp](/media/signup_sm_screen.jpeg) | ![Blogpost view small screen](/media/comment_view_sm_screen.jpeg)
#
![Comment view small screen](/media/comment_view_sm_screen.jpeg)|![Empty comment](/media/empty_comment.jpeg) | ![Second page](/media/second_page_sm_screen.jpeg)
#
#### Blogpost page
#
![Shows slide](/media/shows_slide.jpeg)                 | ![Comment approval](/media/comment_approval.jpeg)
:------------------------------------------------------:|:----------------------------------------:
![Show comment security](/media/two_comments.jpeg)      | ![User view](/media/user_two_comments.jpeg)
#
- Through the slug, which is created automatically while the admin writes the post heading, the indivual blogpoast can be reached. Every visistor can access this view and read the content.
- But in order to interact the visitor has to register or log in.
- When this is done more features are accessable to the site user. Liking and unliking a post, commenting on a post.
- Backend wise the comment is rendered through a crispy form in forms.py and the model for the form is rendered from models.py.
- And after the comment is approved the user that left the comment have access to editing and deleting their comment.
- the comment along with all other content created through the UI- and Admin-view, is saved and rendered from the postgres database.
#
#### About page
#
![About](/media/about_page.jpeg)
#
- On the about page site users get to meet Tessa. It's simple page, with the basic navigation on top and social links in the footer.
#
#### Register page
#
![Register](/media/signout_page_big.jpeg)                 | ![Register message](/media/signin_msg.jpeg)
#
#### Login page
#
![Sign out](/media/signout_page_big.jpeg)                 | ![Sign out message](/media/signin_msg.jpeg)
#
#### Logout page
#
![Sign out](/media/signout_page_big.jpeg)                 | ![Sign out message](/media/signin_msg.jpeg)
#
#### Edit Comment page
#
![Eidt comment](/media/admin_edit_comment.jpeg)
#
- The  front end of this page is basic, but backend ensures that only the user that leaves this indivual comment is the one who ca access this edit page through an if-statement with an equals equals attribute.
- The authorized user, in this case admin, has a basic text field, where they can edit and then automatically be transferred back to commented blogpost, or go to home page, if they don't want to edit.
#### Delete Comment page
#
![Delet comment](/media/delete_comment.jpeg)
#
#### Admin page
#
![Admin approve comments](/media/approve_comments.jpeg) | ![Admin edit/delete blogpost](/media/blogpost_view.jpeg)
:------------------------------------------------------:|:----------------------------------------:
![Admin create/edit blogpost view](/media/create_post.jpeg) | ![Upload images](/media/upload_images.jpeg)
#
- In the admin view a user with superuser status or staff status, has access.
- Here django functionality ensures communication with databases, frameworks, tools and cloudbased services.
- The look and functionality is created in models.py, rendering the view is handled in views.py. 

### Features left to implement
- Open up possibility for more content creators, and with that being able to search for thier contributions via user_email, as well as title and/or content of post.

#
* [Back to README Home page](/README.md)
#