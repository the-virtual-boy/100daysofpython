# Publishing Web Blog Online

Day 71 involved learning about web application hosting options. The requirement were to make the necessary changes and accounts to be able to host the now finished web blog capstone project so it can actually be reached from the internet. For this project, several options of hosting websites were given, such as Heroku and Render. The project involved simply following simple instructions to
1) version our app and host it on github.
2) allow it to be ran in "production mode" via a WSGI server, in this case, `gunicorn`
3) make sure all secret data is converted to grabbing values by environment variables as to not push it to version control.
4) deploy the application using the code from github.
5) set up the application in the hosting site to properly run the app.

For this project, I used [render](https://render.com) since that was the site the instructor used for the steps. As with the previous day, the version control part was simple, and is already set, however as one look of my code would tell, I've been using `dotenv` to store and access secrets so that I don't have to bother with environment variables, this required creating a secret file in the web app server instead of setting environment variables. Another short day but it was satisfying to finally be able to share a link to the capstone I've been working on for quite some time now.