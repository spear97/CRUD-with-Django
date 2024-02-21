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
- 
