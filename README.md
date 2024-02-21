# CRUD with Django

This Django project serves as a Learning Platform Management System. It includes models for users, instructors, learners, courses, lessons, and enrollments, allowing for the management of various educational aspects. Below is an overview of the project structure and functionality:

## Project Structure
- `crud/`: Django app for handling CRUD operations and managing the learning platform.
- `settings.py`: Django settings file with database configuration and installed apps.
- `migrations/`: Directory containing database migration files for model changes.

## Models

1. User
   - Fields:
     - `first_name`: First name of the user.
     - `last_name`: Last name of the user.
     - `dob`: Date of birth of the user.
2. Instructor (inherits from User)
   - Additional Fields:
     - `full_time`: Boolean indicating if the instructor is full-time.
     - `total_learners`: Integer representing the total number of learners under the instructor. 
3. Learner (inherits from User)
   - Additional Fields:
     - `occupation`: Choice field for learner's occupation (e.g., student, developer, data scientist).
     - `social_link`: URLField for the learner's social media profile.
4. Course
   - Fields:
     - `name`: Name of the course.
     - `description`: Description of the course.
   - Relationships:
     - Many-to-Many with `Instructor` (through `instructors`).
     - Many-to-Many with `Learner ` (through `learners` and `Enrollment`). 
5. Lesson
   - Fields:
     - `title`: Title of the lesson.
     - `content`: Content of the lesson.
   - Relationships:
     - Foreign key to `Course`.
6. Enrollment
   - Fields:
     - `date_enrolled`: Date when the learner enrolled.
     - `mode`: Mode of enrollment (audit or honor).
   - Relationships:
     - Foreign key to `Learner`.
     - Foreign key to `Course`.

## Scripts
- `write.py`: Script to seed the database with sample data.
   - `write_instructors()`: Adds instructor data to the database.
   - `write_courses()`: Adds course data to the database.
   - `write_learners()`: Adds learner data to the database.
   - `clean_data()`: Cleans existing data from the database.
- `find_queries.py`: Script demonstrating various query operations on the models. Finds instructors, learners, and performs filtering operations.
- `manage.py`: Django management script to run commands and manage the project.

## Insturctions
1. Setup PostgreSQL Database:
   - Ensure PostgreSQL is installed and running.
   - Configure database settings in `settings.py`.
   - Create a database named `postgres` with the provided credentials.
2. Run Migrations:
   - Apply migrations to create database schema: `python manage.py migrate`.
3. Seed Database:
   - Run the script to populate the database with sample data: `python seed_data.py`.
4. Explore Queries:
   - Run the script `find_queries.py` to explore various query operations.

## Running the Project
1. Activate the virtual environment:
   ```bash
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ``
2. Start the Django development server:
   ```bash
   python manage.py runserver
   ``
3. Access the admin panel at http://localhost:8000/admin/ to manage the data.
   - Login with the admin credentials.
   - Explore and manage users, instructors, learners, courses, lessons, and enrollments.

## Requirements
- Python 3.x
- Django 4.2.5
- PostgreSQL

## Notes
- Ensure PostgreSQL is properly configured and running before running the project.
- For detailed instructions and explanations, refer to the inline comments in the code files.
