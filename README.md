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
1. Login/Registration System
2. Functional forum  (stackOverflow type of vibe)
3. Resources page 
4. Profile Page 
5. Studyzone (Pomodoro timer with music)

## Getting Started 

### Technologies
- HTML
- CSS
- Python Django 
- Bootstapp 
- MySQL
- JavaScript

### Installation
1. Clone Repo 
```commandline
git clone https://github.com/CFG-Group-Project/CFG-Student-Hub.git
```

1. Create an environment <em>(Optional)</em> - [How to create a virtual Environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

2. Install Required Packages
```commandline
pip3 install -r requirements.txt
```

2. Copy contents of setup.sql and run in MySQL WORKBENCH (DONT FORGET to add your password to the query)

3. Add your password to 'DATABASES' Section in CFG-Student-Hub/setup/setup/settings.py (Where is says password: '')

4. Change directory to setup
```commandline
cd setup
```

5. Create tables 
```commandline
python manage.py makemigrations
python manage.py migrate
```

6. Run Server
```commandline
python manage.py runserver localhost:8080
```
### Testing 
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
