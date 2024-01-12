# Porfolio Website

This is the code that supports my portfolio website which is also being hosted on a free tier server on Render.com here: https://my-python-blog-y651.onrender.com/

The website is used to promote my skills, link to this very github account as well as my linked in, and give a way for inquiries to be sent right to the page. Aside from that, the page also serves as an example of some of the skills I have gained in Python, including building a full backend using flask, user authentication to keep others from reading the submitted messages, connection to postgres to store those messages as well as a list of registered users, and front end templating with Bootstrap and WTForms.

## Building on the Code

This project can also be downloaded and used as a template for building upon or helping someone create their own blog. A short explanation of some of the folders and files

- /: The root folder is where the main.py and forms.py folders which hold the backend code and the classes for wtforms respectively. Main.py is where any other routes, logic, or frameworks would be added to

- /templates: This is where any html files would go, including index.html and all the other pages used in this portfolio such as the login page, admin page, even the template for the header and footers.

- /static: this is where all static data such as images, CSS style files and javascript goes.

A few other important files not exactly related to the blog include:

- requirements.txt: This file is what lists all the python plugin dependencies and are all installed at once with `pip install -r requirements.txt`

- Procfile: this file is only used when hosting your website on the internet with a site like Render.com. It is the interface that allows the application to act as a full blown web server.

## Thoughts

Honestly, this was a completely 180 from the morse code project. I feel it's really a lot harder to go crazy with something like this without the proper experience, and what was given in this course just wasn't enough. I would have loved to let loose with fonts, design and color, but even within the first hour it was so frustrating to even try to figure out how to get anything to behave the way I wanted it to that it felt useless. I basically gave up and accepted that most of this course was about backend and that's where I should focus for now.

Copy and pasting was the name of the game with this project. To get me most of the way there on design I copied a free theme from https://HTML5up.net which was introduced early in the web design section. From there I used bootstrap and wtforms to try to get some minor editing in. I focused more on the content and getting the "contact me" section at the bottom working. I used flask_sqlalchemy to push the messages into a sqlite DB, and used flask_authentication to secure an admin page where I can read and delete all messages that were submitted.

The project didn't feel very difficult at all, there was some cleanup, and a bit of troubleshooting involved but copying and pasting made it pretty straight forward. At the same time, implementing anything new in the design felt impossibly difficult. I know I'll get into frontend and webdesign in the near future, so hopefully I can come back to this project and really make it my own. In the shorter term, maybe going over specifically the design lessons will be helpful.