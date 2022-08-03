<html>

# CFG Group porject - Summer '22 Cohort
## Team Members

 - [Samantha Colcough](https://github.com/samanthacolclough) 
 - [Amina](https://github.com/aminacodes)
 - [Ayisha Alli](https://github.com/AyishaAlli)
 - [Victoria ](https://github.com/vixbc)
 - [Elham Hagi](https://github.com/ellehagi)



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
5. Run Server
```commandline
python manage.py runserver localhost:8080
```
### Testing 
Replace 'app-name' with the name of the app you want to test
```commandline
python manage.py test app-name.tests

```

</html>
