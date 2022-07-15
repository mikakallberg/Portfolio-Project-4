# The Green Thumb

![Header](/media/Header_for_readme.png)
## Navigation Through Content
#
* [Deployed page](https://the-green-thumb.herokuapp.com/)
* [Project Purpose](#project-purpose)
    - [Learning Outcomes](#learning-outcomes)
    - [Project Requirements](#project-requirements)
* [Initial Planning](/deployment.md)
* [User Experience](#user-experience-ux)
    - [Demographics](#demographics)
    - [User Goal](#user-goals)
* [Features](/features.md)
* [Testing](/testing.md)
* [Bugs](/bugs.md)
* [Deployment](/deployment.md)
* [Credits](#credits)
    - [Mentoring](#mentoring)
    - [Content credits](#content-credits)
    - [Media](/credits.md)

## Project Purpose
#
(Taken from Assessment Handbook provided by Code Institute)
#
- Project purpose:
  In this project, you'll build a Full-Stack site based on business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide role-based access to the site's data or other activities based on the dataset.
#
## Learning Outcomes
- Use an Agile methodology to plan and design a Full-Stack Web application using an MVC framework and related contemporary technologies.
- - [see User goals](#user-goals)
- - [Checklist in deployment](/deployment.md)
- Implement a data model, application features and business logic to manage, query and manipulate data to meet given needs in a particular real-world domain.
- - [see Features](/features.md)
- Identify and apply authorisation, authentication and permission features in a Full-Stack web application solution.
- - [see Features](/features.md)
- Create manual and/or automated tests for a Full-Stack Web application using an MVC framework and related contemporary technologies.
- - [see Testing](/testing.md)
- Use a distributed version control system and a repository hosting service to document, develop and maintain a Full-Stack Web application using an MVC framework and related contemporary technologies.
- - [GitHub](https://github.com)
- Deploy a Full-Stack Web application using an MVC framework and related contemporary technologies to a cloud-based platform.
- - [Heroku](https://www.heroku.com/)
- Understand and use object-based software concepts
- - [see Features](/features.md)

#
## Technologies and Libraries used

### Languages used
- [Django](https://www.djangoproject.com/) 

- [HTML](https://www.w3schools.com/html/html_intro.asp)

- [CSS](https://www.w3schools.com/css/css_intro.asp)

- [JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)

### Databases
- [Postgresql](https://www.postgresql.org/)
- - As database in Heroku
- [SQLite](https://www.sqlite.org/index.html)
- - As database for Gitpod, the initial thought was to use this for unittest.
  The setting is left as part of future features, to have automatic testing instead of manual testing

### Frameworks and tools
- [Bootstrap](https://getbootstrap.com/)
- [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Summernote](https://summernote.org/)
- [Fontawesome](https://fontawesome.com/)
- [Django-Crispyforms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django-Copyright](https://pypi.org/project/django-copyright/)
- [Google fonts](https://fonts.google.com/specimen/Playfair+Display?category=Serif,Sans+Serif#standard-styles)

### Cloud storage and deployment services
- [Cloudinary](https://cloudinary.com/)
- [Heroku](https://www.heroku.com/)
- [Gunicorn](https://gunicorn.org/)


## Initial planning
#
### Initial plan
- In the intial meeting there was three ideas. Recipe website, Garden blog and Car Dealship. Two rough wireframes where created.
#
Wireframe 1                                         | Wireframe 2
:--------------------------------------------------: | :--------------------------------------------------:
 ![Wireframe 1](/media/wireframe.png)                | ![Wireframe 2](/media/wireframe_2.png)
#
### Plan
- it was decided to build a Garden blog, so a rough sketch of a garden blog with inspiration from existing blogs where made. 
  Please visit [credits to see the inspiration used](/credits.md)
#
 Home Page                                            | Blogpost page
:---------------------------------------------------: | :--------------------------------------------------:
 ![Rough sketch of Garden blog](/media/front_page.png)|  ![Rough sketch of blogpost page](/media/post_page.png)
#

## User Experience (UX)
#
## Demographics
- People who want to know more about gardening and adjancent subject.

## User Goals
#
- As a Site User I can view a list of posts so that I can select one to read
- As a Site User I can click on a post so that I can read the full text
- As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral
- As a Site User / Admin I can view comments on an individual post so that I can read the conversation
- As a Site User I can register an account so that I can comment and like
- As a Site User I can leave comments, edit and delete comments, on a post so that I can be involved in the conversation
- As a Site Admin I can create, read, update and delete posts so that I can manage my blog content
- As a Site Admin I can create draft posts so that I can finish writing the content later
- As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments
- As a Content Creator I can upload more then one image so that I can have multiple images in a carousel

## Credits
#
## Thank you
- [Spencer Barriball](https://github.com/5pence) for always being there and being a fantastic mentor.
- [Daisy McGirr](https://github.com/Daisy-McG) for helping me and giving me insights into backend cooperation with frontend, helping me with some debugs and lessons around django.
- [Bim Williams](https://github.com/MrBim) for being a good person to talk, and for supplying link to API to render content into a downloadable PDF.

### Content credits
- This project is modelled and followed using the "I Think Therefore I Blog" [walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/), produced by Matt Rudge at Code Institute. Using this allowed me to focus on understanding the concepts instead of inventing the wheel with every line of code I produce.
- Another source used in this project is [Djanogcentral](https://djangocentral.com/building-a-blog-application-with-django/). Wherever code from this walkthrough is used, there is credit given in that file.
- To upload multiple images I took a lot of inspiration from a content creator on Youtube called [The Pylot](https://www.youtube.com/watch?v=-0nYBqY9i5w), my code is not a copy paste of his, but I used his video as a stepping stone to get functionality for my Carousels. I also used docs from [Cloudinary](https://cloudinary.com/documentation/django_image_and_video_upload).
- For the alt_tags a line of code from a question on [StackOverflow](https://stackoverflow.com/questions/65415221/best-method-to-store-alt-tags-in-django) was used.

### Media
- For how to make the README nav-bar https://github.com/artkonekt/menu/blob/master/README.md was used.
- As template for README https://github.com/mikakallberg/readme-template/blob/master/README.md was used.

#
* [Back to top](#the-green-thumb)
#