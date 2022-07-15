# Testing
* [Back to README Home page](/README.md)
#
## Navigating Testing
   - [Validator Testing](#validator-testing)
   - [Manual testing](#manual-testing)
   - [Automated Testing](#automated-testing)
#
### Validator testing
#### CSS testing with Jiqsaw
- Comes back with no errors
#
![CSS testing](/media/css_testing.png)
#
#### HTML testing
- All HTML-files comes back with errors and warnings because of django tags. As such nothing will be done to fix those error.
  See images for examples
#
  ![base.html testing](/media/basehtml_test.jpeg)
#

### Lighthouse testing
#
   Desktop                                             | Mobile
   :--------------------------------------------------: | :--------------------------------------------------:
   ![Desktop](/media/lighthouse_desktop.jpeg)          | ![Mobile](/media/lighthouse_mobile.jpeg)
#
### Am I Responsive
#
![Am I Responsive](/media/amiresponsive.png)

### Manual Testing
#### Checklist for manual testing
#
![Checklist](/media/testing.png)
#
#### Manual Testing during development
- Ensured successfull initial launch.
- Ensured successfull launch of app in Heroku after name change of Project folder.
- Ensured continued successfull deployement to Heroku following bug in models.py author attribute.
- Ensured functionality, creation and edititing, of posting a blog entry, in admin view, and use of summernote applications.
- Ensured functionality of admin.py/PostAdmin/prepopulated_fields, and ensured publishing successfully.
- Ensured functionality of login, commenting and like for user.
- Ensured functionality of alert messages, when commenting, login, logout.
- Ensured functionality of copyright.
- After fixing CSS style for sign in and signup pages, made sure logout page looked good.
- After solution to bug related to summernote editor. Made sure creating post and affiliated functions still worked.
- Ensured no unauthorized access through CSRF-tokens, django if statements that restricts view depending on the status of the site user.

#### Manual Testing after deployment in Heroku launched app
- Ensured login, logout, admin access capability for admin.
- Ensured admin capability to create content, edit and delete content, and upload multiple images to Cloudinary.
- Ensured Carousel works as intented.
- Ensured Site user can view content without registering.
- Ensured Site User can register, like/unlike, create a comment, edit and delete an approved comment, and exit edit and delete view if they want.
- Ensured responsive deisgn on screens down to 300px.
- Ensured registered site user can not access admin portal.
- Ensured site users cannot access admin portal
- Ensured site users cannot access logour page without being logged in to account.
- Ensured site users cannot edit or delete other site users comments or likes.
- Ensured all functionality works in both desktop and mobile as intented.
- Ensured automatic deployment functionality.
#
![Error message when user tries to reach admin page](/media/error_msg_user.jpeg)
#

### Automated Testing
- Due to unforseen circumstances there was no time to build any unittest. The settings are left as a future feature update.

#
* [Back to README Home page](/README.md)
#