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
- 
- 

# Testing
### Validator testing
Validator testing!
### Manual Testing
- Ensured successfull launch of app in Heroku after name change of Project folder.
- Ensured continued successfull deployement to Heroku following bug in models.py author attribute.
- Ensured functionality, creation and edititing, of posting a blog entry, in admin view, and use of summernote applications.
- Ensured fucntionality of admin.py/PostAdmin/prepopulated_fields, and ensured publishing successfully.
### Automated Testing
- Continual testing done through the ------ method described in "The Clean Coder- A Code of Conduct for Professional Programmers" by Robert C. Martin and Hello Django lessons.
![TDD Testing example](Image goes here)
## Bugs
### Bugs through the creation process
- First bug was connected to trying to gifure out how to write automated tests. It took a lot of research and getting advice from programmers more advanced then me. But in the end I managed to create my very first succesfull automatic test. 
![Bug 1](static/assets/images/bug_nr_one.png)
- Major bug in models.py file when trying to migrate the database. Error message asked to change something in author attribute, but that didn't resolve issue. Had to reset database using the guide from [Delfstack](https://www.delftstack.com/howto/django/django-reset-database/).
- Bug in models.py/excerpt before migrating nedded a default or blank=True.
- Bug in admin.py/@admin.register(BlogPost) automated adding of brackets, could not migrate before removed.
- Bug where index.html didn't render in view. Bugfix add "context_object_name = 'post_list'" to PostList class, system was asked to query from backend, but not what to query. Established bridge to published blogpost through name in for loop on line 10 in index.html.
- Inability to render post_detail.html, misspelling in if-statement attribute on line 24, reported in error statement. Bugfix, correct spelling misstake.
- Inconsistent migration history, resolved by resetting both the SQLite3 amd postgreSQL databases.

    - 
    - 

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
- [Daisy McGirr](https://github.com/Daisy-McG) for helping me and giving me insights into backend cooperation with frontend.

### Content
- 

### Media
- For how to make the nav-bar https://github.com/artkonekt/menu/blob/master/README.md was used.
- As template for README https://github.com/mikakallberg/readme-template/blob/master/README.md was used
- 

- 
- 
- 
