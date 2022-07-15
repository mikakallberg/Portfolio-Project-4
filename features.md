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
- The front page has two different views in desktop mode. One when the site user is not logged in and one when the user is logged in, this can been seen in the navigation bar at the top.
- When the user is logged in they can access their particular functions.
- -Admin can reach admin view thru the url window, on top of all functionality a regular user can access.
- - a regular site user can access the logout page, creating comments/editing/deleting comments and likin and unliking posts.
- - when a user logs in or out a message displays at the top of the page for three seconds to indicate the users action was successfull. This is du to a combination of backend fucnctions in the apps code, Bootstrap messages and JavaScript, and some custome JavaScript code written at the bottom of the base.html page.
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
- When registering for this site a user is presented with an allauth form page. That connects to a comment model in models.py, and the information is stored in postgres database.
#
#### Login page
#
![Sign out](/media/signout_page_big.jpeg)                 | ![Sign out message](/media/signin_msg.jpeg)
#
- The login page is also from allauth.
#
#### Logout page
#
![Sign out](/media/signout_page_big.jpeg)                 | ![Sign out message](/media/signin_msg.jpeg)
#
- The logout page is an allauth page
#
#### Edit Comment page
#
![Eidt comment](/media/admin_edit_comment.jpeg)
#
- The  front end of this page is basic, but backend ensures that only the user that leaves this indivual comment is the one who ca access this edit page through an if-statement with an equals equals attribute.
- The authorized user, in this case admin, has a basic text field, where they can edit and then automatically be transferred back to commented blogpost, or go to home page, if they don't want to edit.
#
#### Delete Comment page
#
![Delet comment](/media/delete_comment.jpeg)
#
- The delete comment page is only accessable if the user trying to access it also is the one who has left the comment. For more information see security features.
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
- Rendering a blog post content into a downloadable PDF
- Unittesting to decrease the amount of manual testing necessery.
- More site user controlled features, like editing password, adding a image, gathering liked and commented post on a page of their own.
#
* [Back to README Home page](/README.md)
#