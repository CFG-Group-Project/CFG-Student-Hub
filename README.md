<html>

# CFG Group project - Summer '22 Cohort
## Team Members

 - [Samantha Colcough](https://github.com/samanthacolclough) 
 - [Amina](https://github.com/aminacodes)
 - [Ayisha Alli](https://github.com/AyishaAlli)
 - [Victoria ](https://github.com/vixbc)
 - [Elham Hagi](https://github.com/ellehagi)

## About 
A web app for CFG nano degree students. 
This space is made for students (by students!) and can be utilised on a number of different levels. 
There are a number of different features that can be used for effective learning to ensure that students are getting the most while completing the course with Code First Girls. 

## Features
1. Login/Registration System : With Error handling
2. Functional forum : [studentRoom](https://www.thestudentroom.co.uk/) type of vibe, Post, Comment and Like!
3. Resources page: One stop shop for CFG Resourses + Note takinng
4. Studyzone : Pomodoro timer with music & motivation 
5. Profile Page : Edit profile details, such as Full name and username etc

## Getting Started 

### Technologies
- Python Django 
- HTML
- CSS
- Bootstapp 
- MySQL
- JavaScript

### Installation
1. Clone Repo 
```commandline
git clone https://github.com/CFG-Group-Project/CFG-Student-Hub.git
```

2. Create an environment <em>(Optional)</em> - [How to create a virtual Environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

3. Install Required Packages
```commandline
pip3 install -r requirements.txt
```

4. Copy contents of setup.sql and run in MySQL WORKBENCH
   (DONT FORGET to add your password to the query, where it says "Current-Root-Password")

5. Add your password to 'DATABASES' Section in CFG-Student-Hub/setup/setup/settings.py 
   (Where is says " password: '' ")

6. Change directory to setup
```commandline
cd setup
```

7. Create tables 
```commandline
python manage.py makemigrations
python manage.py migrate
```

8. Run Server
```commandline
python manage.py runserver localhost:8080
```
## Testing 
Replace 'app-name' with the name of the app you want to test
```commandline
python manage.py test app-name.tests

```

## Acknowledgments 
Our instructors: 
- [Carlo]()
- [Alex]()

Thank you for supporting us throughout this whole course! We've had a blast!
</html>
