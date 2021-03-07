# E-SIWES Portal Created Using Django
The portal replaces the manual training logbook which assists students to keep records of daily activities during the course of the SIWES programme.

# About SIWES
The Student Industrial Work Experience Scheme (SIWES), also known as Industrial Training is a compulsory skills training programme designed to expose and prepare students of Nigerian Universities, Polytechnics, Colleges of Education, Colleges of Technology and Colleges of Agriculture, for the industrial work situation they’re likely to meet after graduation.



Feel free to make changes based on your requirements.

[Front-end Template](http://adminlte.io "Admin LTE.io")




And if you like this project, then ADD a STAR ⭐️  to this project 👆


## Features of this Project

### A. Admin Users Can
1. See Overall Summary
2. Manage Logbook (Add Remark)
3. Manage Students (Add, Update and Delete)
4. Manage Companies (Add, Update and Delete)

### B. Company/Industrial-Based Supervisors Can
1. See the Overall Summary related to their students
2. Sign Weekly Logbook
3. Update Profile

### C. Students Can
1. See the Overall Summary 
2. Update Profile
3. Add Logbook
4. Update Logbook (If Logbook has not been signed by Supervisor)


## 📸 ScreenShots

<img src="ss/1.png"/>
<img src="ss/2.png"/>
<img src="ss/3.png"/>
<img src="ss/4.png"/>
<img src="ss/5.png"/>

| Admin| Staff| Student |
|------|-------|---------|
|<img src="ss/admin5.png" width="400">|<img src="ss/company1.png" width="400">|<img src="ss/student1.png" width="400">|
|<img src="ss/admin2.png" width="400">|<img src="ss/company2.png" width="400">|<img src="ss/student2.png" width="400">|
|<img src="ss/admin3.png" width="400">|<img src="ss/company3.png" width="400">|<img src="ss/student3.png" width="400">|
|<img src="ss/admin4.png" width="400">|<img src="ss/company4.png" width="400">|<img src="ss/student4.png" width="400">|
|<img src="ss/admin1.png" width="400">|<img src="ss/company5.png" width="400">|<img src="ss/student5.png" width="400">|
|<img src="ss/admin6.png" width="400">|<img src="ss/company6.png" width="400">|<img src="ss/student6.png" width="400">|



## Support Developer
1. Add a Star 🌟  to this 👆 Repository
2. Follow on Twitter/Github


## Passport/Images
Images are from [Unsplash](https://unsplash.com)


## How to Install and Run this project?

### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```
For Linux
```
$  virtualenv .
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```

For Linux
```
$  source bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/jobic10/student-management-using-django.git
```

Then, Enter the project
```
$  cd student-management-using-django
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip3 install -r requirements.txt
```

**5. Add the hosts**

- Got to settings.py file 
- Then, On allowed hosts, Use **[]** as your host. It's there already!
```python
ALLOWED_HOSTS = []
```

**6. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

Command for Linux:
```python
$ python3 manage.py runserver
```

**7. Login Credentials**

Create Super User (HOD)
Command for PC:
```
$  python manage.py createsuperuser
```

Command for Mac:
```
$  python3 manage.py createsuperuser
```

Command for Linux:
```
$  python3 manage.py createsuperuser
```



Then Add Email and Password

**or Use Default Credentials**

*For HOD /SuperAdmin*
Email: admin@admin.com
Password: admin

*For Staff*
Email: company@company.com
Password: company

*For Student*
Email: student@student.com
Password: student



## For Sponsor or Projects Enquiry
1. Email - jobowonubi@gmail.com
2. LinkedIn - [jobic10](https://www.linkedin.com/in/jobic10 "Owonubi Job Sunday on LinkedIn")
2. Twitter - [jobic10](https://www.twitter.com/jobic10 "Owonubi Job Sunday on Twitter")



