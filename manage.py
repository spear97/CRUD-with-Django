import os
import sys

if __name__ == "__main__":
    # Set the Django settings module to 'settings'
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    try:
        # Import execute_from_command_line to run Django management commands
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            # Check if Django is installed
            import django
        except ImportError:
            # If Django is not installed, raise an ImportError
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    # Execute Django management commands from the command line arguments
    execute_from_command_line(sys.argv)
