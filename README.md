# DishDemocracy
Recruitment Task for Brain station 23 PLC.

Welcome to DishDemocracy README. This is a documentation of the DishDemocracy webapp containing launch instruction, project description, project features and a roadmap to this project creation.

## Prerequisites

- Python (3.0 or higher)

## Follow these Instructions for a Successful Launch

1. Clone the repository

   ```bash
   git clone https://github.com/imnasim31415/DishDemocracy-Backend

2. Navigate to the project directory

    ```bash

   cd DishDemocracy

3. Create a virtual environment (optional but recommended)

    ```bash

    python -m venv venv
    ```

4. Activate the virtual environment:

    On Windows:

    ```bash

    .\venv\Scripts\activate
    ```

    On macOS/Linux:

    ```bash

    source venv/bin/activate
    ```

5. Install project dependencies:

    ```bash

    pip install -r requirements.txt
    ```

6. Apply database migrations:
    ```bash

    python manage.py migrate
    ```

7. Create a superuser (for Django admin access):

   ```bash

   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash

   python manage.py runserver
   ```



# Project Description

## Overview

DishDemocracy is a webapp built for Brain station 23 PLC, one of the largest and fast-growing companies in our country. With this growth, they are encountering challenges in providing lunch options to their employees. They aim to offer great lunches, but since everyone has different preferences, ordering individual meals for each person is impractical. To address this, DishDemocracy (a voting app for lunch) is created. Restaurants can display their menus, and all employees can vote for their favorite dishes. The menu with the most votes will be chosen for the day. This approach ensures that everyone has a role in deciding what's for lunch, making it a fair and enjoyable process!

## Features

### Authentication

The app provides authentication to increase security of user accounts.

User Types:
- Restaurant Owners
- Employees
  
![Home Page](https://github.com/imnasim31415/DishDemocracy-Backend/blob/main/dishdemocracy/screenshots/homepage.png)
 
### Restaurant Management

- **Registering Restaurant**
 ![Restaurant Registration Page](https://github.com/imnasim31415/DishDemocracy-Backend/blob/main/dishdemocracy/screenshots/reg%20rest.png)

- **Uploading Menu**
![Uploading Menu](https://github.com/imnasim31415/DishDemocracy-Backend/blob/main/dishdemocracy/screenshots/menu.png)


### Employee Management

- **Registering Employee**
![Employee Registration Page](https://github.com/imnasim31415/DishDemocracy-Backend/blob/main/dishdemocracy/screenshots/reg%20employe.png)


### Voting Process
   
- **Voting for Restaurant Menu**
  ![Voting](https://github.com/imnasim31415/DishDemocracy-Backend/blob/main/dishdemocracy/screenshots/empvotpage.png)


### Results and Restrictions

- **Getting Results**
  ![Voting](https://github.com/imnasim31415/DishDemocracy-Backend/blob/main/dishdemocracy/screenshots/winner.png)

### Logout


## Implementation

**Framework:** Django

## ER Diagram



![ER Diagram](https://github.com/imnasim31415/DishDemocracy-Backend/blob/main/dishdemocracy/screenshots/ERD.png)
