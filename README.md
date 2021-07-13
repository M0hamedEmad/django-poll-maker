# Django Poll Maker
An app that lets you make advanced and secure poll
# Usage
It's best to install Python projects in a Virtual Environment. Once you have set up a Virtual Environment, clone this project
 ```
 git clone https://github.com/M0hamedEmad/django-poll-maker.git
 ```
 then cd to file and Run
 ```
pip install -r requirements.txt #install required packages
python manage.py migrate # run first migration
python manage.py runserver # run the server
 ```
 then open in your browser http://127.0.0.1:8000/
 
 # Make a Superuser
 Run
 ```
 python manage.py createsuperuser
 ```
 then write a username, email, password 
 go to http://127.0.0.1:8000/admin  a django admin
 or http://127.0.0.1:8000/dashboard  a dashboard for admin and editors
 
# Secure
The IP of the device is recorded after each vote is made, and when the device re-enters the poll, its vote is returned, and if it modifies the vote, the initial vote is erased.

# Features
 singel answer vote or multiple answers
 Determine when voting begins and ends
 Activate or inactive the poll
 visitor counter
 Title and Summary Poll
 image in question or answer
 code for poll if poll creator is Unknown to make delete or update to poll
 login with google account
 
