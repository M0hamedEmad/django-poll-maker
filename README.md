# Django Poll Maker
An app that lets you make advanced and secure poll

# Demo
## https://djpollmaker.herokuapp.com/

## Vote
### https://djpollmaker.herokuapp.com/vote/what-best-programing-language-1/

###  login
username : demo
password: demodemo123

https://djpollmaker.herokuapp.com/accounts/login/

deshboard
![](https://user-images.githubusercontent.com/75542426/130637213-ba0eabe6-3958-4e6a-b02f-158d88f14610.png)

![1](https://user-images.githubusercontent.com/75542426/130637090-f49c3568-02be-4062-b32a-8299265e79ed.png)
![2](https://user-images.githubusercontent.com/75542426/130637098-d1ab3f37-f95b-4347-98e0-d46087f22902.png)
![3](https://user-images.githubusercontent.com/75542426/130637102-f0be3d2f-0adf-4e66-ab0a-7b80e114e9fb.png)


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
 * singel answer vote or multiple answers
 * Determine when voting begins and ends
 * Activate or inactive the poll
 * visitor counter
 * Title and Summary Poll
 * image in question or answer
 * code for poll if poll creator is Unknown to make delete or update to poll
 * login with google account
 * 

