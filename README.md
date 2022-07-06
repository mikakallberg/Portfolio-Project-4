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
    - [Media](#media)

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


# Game Content
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
- [Daisy McGirr](https://github.com/Daisy-McG) for helping me and giving me insights into backend cooperation with frontend, helping me debug the create_post bug.
- [Bim Williams](https://github.com/MrBim) for being a good person to talk, and for supplying link to API to render content into a downloadable PDF.

### Content
- This project is modelled and followed using the "I Think Therefore I Blog" [walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/), produced by Matt Rudge at Code Institute. Using this allowed me to focus on understanding the concepts instead of inventing the wheel with every line of code I produce.
- Another source used in this project is [Djanogcentral](https://djangocentral.com/building-a-blog-application-with-django/). Wherever code from this walkthrough is used, there is credit given in that file.

### Media
- For how to make the README nav-bar https://github.com/artkonekt/menu/blob/master/README.md was used.
- As template for README https://github.com/mikakallberg/readme-template/blob/master/README.md was used.
- 

- 
- 
- 
