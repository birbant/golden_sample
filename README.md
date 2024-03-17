# GOLDEN SAMPLE

## Introduction
Derived from my personal experience gained in Quality Management in injection molding industry I made simple application for management of golden samples. 
Consider context od keeping golden sample as a sample reference which is crucial for approving further production orders.

> An approved prototype, also known as a Golden Sample, is a model provided by your manufacturer prior to full-scale production. 
> It serves as an exemplar of your desired product, meeting all specified quality criteria. 

## Requirements
```bash
#create a virtual environment for application libriaries in Windows OS:
#add Python interpreter
#activating hermetic environment

venv\Scripts\activate
pip  install  -r  requirements.txt
pip  list
```
Check: [tutorial venv](https://docs.python.org/3/tutorial/venv.html)
as well as: [djangoproject](https://www.djangoproject.com/) 

## Technologies used for making Golden Sample App:

- Python
- Django
- HTML
- CSS
- Bootstrap
- reCAPTCHA 

## Installation

Steps required to install and run the project locally.

1. Clone the repository:
	
    ```bash
    https://github.com/birbant/golden_sample
    ```
2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Perform database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```
   
6. Run golden sample app 
   ```bash
   # Access from browser or use curl
   curl 127.0.0.1:8000/
    ```
## Usage
The application is designed to facilitate the management of user golden samples. 
Its features include:

- [Adding](/static/read-me-photos/emp%20add.png),
[editing](/static/read-me-photos/emp%20edd.png) and 
[deleting](/static/read-me-photos/emp%20del.png) employees from [database](/static/read-me-photos/emplo.png).

- [Adding](/static/read-me-photos/sam%20add.png),
[editing](/static/read-me-photos/sam%20upd.png) and 
[deleting](/static/read-me-photos/sam%20del.png) samples from [database](/static/read-me-photos/samp.png).

- Sample [operations](/static/read-me-photos/ope.png): [collecting](/static/read-me-photos/sam%20add.png) 
(for production and for other purposes) and return with storage tracking. 
- User [panel](/static/read-me-photos/dashboard.png) and other functionalities including: [registration](/static/read-me-photos/register.png) with 
secure captcha tests, [login](/static/read-me-photos/login.png), [logout](/static/read-me-photos/logout.png), 
[statistics](/static/read-me-photos/stat.png) and customized error [404](/static/read-me-photos/404.png) messages.

## Contributions
Any additional contribution to the project, such as reporting bugs, proposing new features, etc. is more 
than very welcome. Please contact me regarding your observations, suggestions and comments.
- - - - - - 
Current version of Golden Sample needs to be treated as base - let's call it v1 - in development of this 
particular concept with rather quite large room for improvement. 