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

## Usage
The application is designed to facilitate the management of user golden samples. 
Its features include:

Adding, editing, and deleting user profiles.
Adding, editing, and deleting samples.
Adding and editing sample operations as collecting for production and other purposes as well as return.
User panel functionality, including registration, login, and logout.

## Contributions
Any additional contribution to the project, such as reporting bugs, 
proposing new features, etc. is more than very welcome. Please contact me regarding your observations, suggestions and comments.
