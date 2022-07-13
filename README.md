# The Green Thumb

# Navigation Through Content
* [Deployed page](https://the-green-thumb.herokuapp.com/)
* [Project Purpose](#project-purpose)
    - [Learning Outcomes](#learning-outcomes)
    - [Project Requirements](#project-requirements)
* [Initial Planning](#initial-planning)
    - [Lucid Chart](#lucid-chart)
    - [Code Plan](#code-plan)
    - [Media for Inspiration](#media-for-inspiration)
* [Features](#features)
	- [Existing Features](#existing-features)
    - [Features left to implement](#features-left-to-implement)
* [Testing](#testing)
    - [Validator testing](#validator-testing)
    - [Other testing done](#other-testing-done)
* [Bugs](#bugs)
    - [Bugs through the  creation process](#bugs-through-the-creation-process)
    - [Unfixed bugs](#unfixed-bugs)
* [Deployment](#deployment)
* [Credits](#credits)
    - [Mentoring](#mentoring)
    - [Content](#content)
    - [Media](/credits.md)

# Project Purpose
## Learning Outcomes
Taken from Assessment Handbook provided by Code Institute.


### Project requirements
Taken from Assessment Handbook provided by Code Institute or derived therefrom.
- Required langauge: [Python](https://www.python.org/doc/essays/blurb/) 
- Using APIs and library software [Wikipedia](https://en.wikipedia.org/wiki/API)
- Deploy to a cloud-based platform [Heroku](https://www.heroku.com/home)


# Initial planning
### 



### GitHub Projects



### Code Plan

Initial Plan page 1.                                 | Initial Plan page 2
:--------------------------------------------------: | :--------------------------------------------------:
![Initial Plan 1](image file link goes here)  | ![Initial Plan 2](image file link goes here)


### Media for inspiration
- 


# User Experience (UX)
## Demographics

## User Goal


# Blog Content
## Features

### Existing features


### Features left to implement
- Open up possibility for more content creators, and with that being able to search for thier contributions via user_email, as well as title and/or content of post.


# Technologies and Libraries used

### Languages used
- [Python](https://www.python.org/doc/essays/blurb/) 

- [HTML](https://www.w3schools.com/html/html_intro.asp)

- [CSS](https://www.w3schools.com/css/css_intro.asp)

- [JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)

### APIs
- https://pypi.org/project/django-copyright/
- https://pypi.org/project/reportlab/

# Testing
### Validator testing
Validator testing!
### Manual Testing
- Ensured successfull launch of app in Heroku after name change of Project folder.
- Ensured continued successfull deployement to Heroku following bug in models.py author attribute.
- Ensured functionality, creation and edititing, of posting a blog entry, in admin view, and use of summernote applications.
- Ensured functionality of admin.py/PostAdmin/prepopulated_fields, and ensured publishing successfully.
- Ensured functionality of login, commenting and like for user.
- Ensured functionality of alert messages, when commenting, login, logout.
- Ensured functionality of copyright.
- After fixing CSS style for sign in and signup pages, made sure logout page looked good.
- After solution to bug related to summernote editor. Made sure creating post and affiliated functions still worked.

### Automated Testing
- Continual testing done through the ------ method described in "The Clean Coder- A Code of Conduct for Professional Programmers" by Robert C. Martin and Hello Django lessons.
![TDD Testing example](Image goes here)
## Bugs
### Bugs through the creation process
- First bug was connected to trying to gifure out how to write automated tests. It took a lot of research and getting advice from programmers more advanced then me. But in the end I managed to create my very first succesfull automatic test. 
![Bug 1](media/bug_nr_one.png)
- Major bug in models.py file when trying to migrate the database. Error message asked to change something in author attribute, but that didn't resolve issue. Had to reset database using the guide from [Delfstack](https://www.delftstack.com/howto/django/django-reset-database/).
- Bug in models.py/excerpt before migrating nedded a default or blank=True.
- Bug in admin.py/@admin.register(BlogPost) automated adding of brackets, could not migrate before removed.
- Bug where index.html didn't render in view. Bugfix add "context_object_name = 'post_list'" to PostList class, system was asked to query from backend, but not what to query. Established bridge to published blogpost through name in for loop on line 10 in index.html.
- Inability to render post_detail.html, misspelling in if-statement attribute on line 24, reported in error statement. Bugfix, correct spelling misstake.
- Inconsistent migration history, resolved by resetting both the SQLite3 amd postgreSQL databases.
- Blog content and excerpt did not appear. Coder forgot to properly add content and excerpt, solved by adding content and excerpt. (Yes, coder and tutor support agent laughed)
- When adding a create_post.html, page doesn't render, gives an error 404 page. Solution change places of the paths in url_patterns in urls.py.
- When trying to POST a new blogpost through the UI, throws error 404, the path the system is taking goes through the projects urls.py. It doesnt find the "http://localhost:8000/create_post/POST" url pattern. Solution add success_url = '/' to forms.py.
- When trying to add summernote editer to my form it's not working. Solution:
  - in forms.py:
    - change the import and class to a class CreatePostForm(forms.ModelForm)
  - in views.py:
    - Add a class: class CreatePostView(CreateView)
  - In blog/urls.py:
    - change path to: path('create_post/', views.CreatePostView.as_view(), name='create_post'),
- Bug when trying to upload images from UI in cerate_post.html. After meeting with mentor who adviced to fullfill CRUD through comments, so not to expose uploading images to someone trying to overload my filespace in cloudinary. Also It's only going to be admin who posts blogposts.
- Bug in automatically rendered excerpt. Paragraph-elements and classes that render automatically from content gets displayed in excerpt. Solution add a safe tag to the post.content block tag.
- Bug. Trying to add label to commentform in UI. Solution add a comma to fields attribute and relaunch server.
- Large bug. post_detail.html not loading, because of commentsection. cleaning up form for comments and trying different ways of rendering the commentform.
- Large bug. update_post.html not redirecting to post_detail.html. Solution chaning the successful_url to a function form_valid under CommentUpdateView.
- Bug when returning after deleting comment. Solution taking post.slug along from initial url and returning at as argument in a reverse_lazy.
- Bug in carousel at post_detail.html. Typo was found in for loop. 


### Unfixed bugs
- 
- 
- 
- 

# Deployment

The project is not deployed
### Checklist:
- to keep track of what to do and improvements on the initial plan, I use a checklist. Since this project isn't working, the list is incomplete.

![Checklist](image-link here)

# Credits

## Thank you
- [Spencer Barriball](https://github.com/5pence) for always being there and being a fantastic mentor.
- [Daisy McGirr](https://github.com/Daisy-McG) for helping me and giving me insights into backend cooperation with frontend, helping me with some debugs and lessons around django.
- [Bim Williams](https://github.com/MrBim) for being a good person to talk, and for supplying link to API to render content into a downloadable PDF.

### Content
- This project is modelled and followed using the "I Think Therefore I Blog" [walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/), produced by Matt Rudge at Code Institute. Using this allowed me to focus on understanding the concepts instead of inventing the wheel with every line of code I produce.
- Another source used in this project is [Djanogcentral](https://djangocentral.com/building-a-blog-application-with-django/). Wherever code from this walkthrough is used, there is credit given in that file.

### Media
- For how to make the README nav-bar https://github.com/artkonekt/menu/blob/master/README.md was used.
- As template for README https://github.com/mikakallberg/readme-template/blob/master/README.md was used.
favicon: https://pixabay.com/sv/vectors/v%c3%a4xter-mycket-liten-sprouty-gr%c3%b6n-576558/
soil post
- https://sv.wikipedia.org/wiki/Backtimjan
https://unsplash.com/photos/jin4W1HqgL4?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/pj7NdlymKq8?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/9SjCXUq_qSE?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://www.soils.org/files/sssa/iys/march-soils-overview.pdf
https://www.clientearth.org/latest/latest-updates/news/why-soil-matters/
tomatoe post
https://www.gardenersworld.com/how-to/grow-plants/how-to-grow-tomatoes/
https://pixabay.com/sv/photos/tomater-vin-tr%c3%a4dg%c3%a5rd-f%c3%a4rsk-mogen-4474174/
https://unsplash.com/photos/3rGrIigBq8Q?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/S3wQbItzrg4?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/BQgNC4arlKY?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/A1CTgIViTMc?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/ettlwvew0-g?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink

carrots
https://www.gardeningknowhow.com/edible/vegetables/carrot/how-to-grow-carrots.htm
https://unsplash.com/photos/La8Y09cg_yo?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/iPiXhoMUcV8?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink

the humble potatoe
https://unsplash.com/photos/jPJ3GqH_HsE?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLinkpotat
https://unsplash.com/photos/484GsKrL5r8?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/2qEv_MOltfk?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/Dibo4TSF3Jw?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink

Salad
https://www.almanac.com/how-grow-your-own-salad-greens
https://www.almanac.com/video/growing-lettuce-and-salad-greens-containers
https://unsplash.com/photos/Bbq3H7eGids?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/bk11wZwb9F4?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/dI6hZvxWvTw?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/R-8-da2yRgg?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink

Onions
https://www.almanac.com/growing-onions
https://unsplash.com/photos/7CcXR5wIhEY?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/0Y8bjjMU7KQ?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/nCgFMzie7_A?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/YC2H1-tMy5o?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink

Bell peppers
https://www.almanac.com/plant/bell-peppers
https://unsplash.com/photos/H1C11hL-oiw?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/vrbZVyX2k4I?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink
https://unsplash.com/photos/xHnZIPZNxZk?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink

- 
- 
- 
