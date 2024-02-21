from django.db import models
from django.utils.timezone import now

# User model 
class User(models.Model):
    """
    A base model representing a user with common fields like first name, last name, and date of birth.
    """
    first_name = models.CharField(null=False, max_length=30, default='john')
    last_name = models.CharField(null=False, max_length=30, default='doe')
    dob = models.DateField(null=True)

    def __str__(self):
        """
        Returns a string representation of the User object.
        """
        return self.first_name + " " + self.last_name

# Instructor model
class Instructor(User):
    """
    A model representing an instructor, inheriting from the User model.
    """
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()
    
    def __str__(self):
        """
        Returns a string representation of the Instructor object.
        """
        return "First name: " + self.first_name + ", " + \
               "Last name: " + self.last_name + ", " + \
               "Is full time: " + str(self.full_time) + ", " + \
               "Total Learners: " + str(self.total_learners)

# Learner model
class Learner(User):
    """
    A model representing a learner, inheriting from the User model.
    """
    STUDENT = 'student'
    DEVELOPER = 'developer'
    DATA_SCIENTIST = 'data_scientist'
    DATABASE_ADMIN = 'dba'
    
    OCCUPATION_CHOICES = [
        (STUDENT, 'Student'),
        (DEVELOPER, 'Developer'),
        (DATA_SCIENTIST, 'Data Scientist'),
        (DATABASE_ADMIN, 'Database Admin')
    ]
    
    occupation = models.CharField(
        null=False, 
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT
    )
    
    social_link = models.URLField(max_length=200)

    def __str__(self):
        """
        Returns a string representation of the Learner object.
        """
        return "First name: " + self.first_name + ", " + \
               "Last name: " + self.last_name + ", " + \
               "Date of Birth: " + str(self.dob) + ", " + \
               "Occupation: " + self.occupation + ", " + \
               "Social Link: " + self.social_link

# Course model
class Course(models.Model):
    """
    A model representing a course with a name, description, instructors, and enrolled learners.
    """
    name = models.CharField(null=False, max_length=100, default='online course')
    description = models.CharField(max_length=500)
    
    instructors = models.ManyToManyField(Instructor)
    learners = models.ManyToManyField(Learner, through='Enrollment')
    
    def __str__(self):
        """
        Returns a string representation of the Course object.
        """
        return "Name: " + self.name + "," + \
            "Description: " + self.description

# Lesson model
class Lesson(models.Model):
    """
    A model representing a lesson in a course with a title, content, and associated course.
    """
    title = models.CharField(max_length=200, default="title")
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the Lesson object.
        """
        return "Title: " + self.title + ", " + \
                "Course: " + self.course + ", " + \
                "Content: " + self.content

# Enrollment model as a lookup table with additional enrollment info
class Enrollment(models.Model):
    """
    A model representing an enrollment with a learner, course, enrollment date, and mode.
    """
    AUDIT = 'audit'
    HONOR = 'honor'
    COURSE_MODES = [
        (AUDIT, 'Audit'),
        (HONOR, 'Honor'),
    ]
    
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(default=now)
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)

    def __str__(self):
        """
        Returns a string representation of the Enrollment object.
        """
        return "Learner: " + str(self.learner) + ", " + \
               "Course: " + str(self.course) + ", " + \
               "Date Enrolled: " + str(self.date_enrolled) + ", " + \
               "Mode: " + self.mode
