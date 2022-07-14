# Deployment

The project is not deployed
### Checklist:
- to keep track of what to do and improvements on the initial plan, I use a checklist. Since this project isn't working, the list is incomplete.

![Checklist](image-link here)

### Initial Deployment:
- Following the "I think therefore I blog walkthru"
- Install basic packages in GitPod with the following commands:
                                                    - pip3 install 'django<4' gunicorn
                                                    - pip install dj_database_url psycopg2
                                                    - pip3 install dj3-cloudinary-storage
                                                    - pip3 freeze --local > requirements.txt
                                                    - django-admin startproject THEGREENTHUMB . (This was incorrect practise, so I used the search function to change all instances of uppercase to lowercase).
                                                    - python3 manage.py startapp blog
                                                    - pip3 install django-crispy-forms
                                                    - Migrate the work using:
                                                                            - python3 manage.py makemigrations --dry-run
                                                                            - python3 manage.py makemigrations
                                                                            - python3 manage.py migrate --plan
                                                                            - python3 manage.py migrate
                                                    - Make sure project deploys in preview (python3 manage.py runserver)
                                                    - In envy.py add my Cloudinary API variable, postgres DATABASE_URL.
                                                    - Make sure env.py is in the gitignore-file
- Commit all changes to GitHub for initial deployment to Heroku
                                                    - git add .
                                                    - git commit -m "add message here"
                                                    - git push
                                                    - Here I realized that I forgot to hide the secret key in env.py.
                                                    - Create new secret key and go through the process again adn make sure to add my new secret key into env.py.
- In Heroku Create a new app by:
                               - In front view- press New->Create new app
                               - Choose a unique app name, that conforms to heroku naming standard and choose region (Europe). Press Create app
                               - Attache Heroku Postgres as DATABASE, under Resources
                               - Under Settings-> Config vars: 
                                                            - add my Cloudinary API variable
                                                            - add DISABLE_COLLECTSTATIC, this to prevent accidentally showing debug messages while DEBUG is True in settings.py
                                                            - add port 8000
                                                            - add SECRET_KEY from app in Gitpod
                               - Under Deploy choose deployment methos Github and search for my repo. I am already connected since before.
                               - Make sure branch to deploy is set on main.
                               - Deploy branch
                               - Successful deployment, unfortunately I forgot to take a screenshot of this. So no picture of the awesome rocket.
### Final Deployment:
- For the final deployment I again follow the  videos in "I think therefore I blog walkthru"
                - In GitPod:
                            - Before deployment I've done an intial testing of all features in preview.
                            - Settings -> Change DEBUG to False.
                            - Settings -> Add X_FRAME_OPTIONS = 'SAMEORIGIN'
                            - git add .
                            - git commit -m "Deployment commit"
                            - git push
                            - Since this did'nt work connection to Heroku was established through login in to heroku through terminal
                            - heroku login -i
                            - heroku run python3 manage.py migrate
                            - heroku run python3 manage.py migrate --app the-green-thumb
                            - this launched the site successfully
                            - set debug to false to let CSS come through.
                            -create a superuser in heroku
                            - heroku login -i
                            - heroku run python3 manage.py createsuperuser --app the-green-thumb
                - In Heroku:
                            - Remove DISABLE_COLLECTSTATIC
                            - Deploy manually
                            - Deployment syccessfull with all functionality and style.