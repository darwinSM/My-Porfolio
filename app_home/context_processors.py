from django.conf import settings

def debug_mode (request):
    """
    Summary:
        This function is useful for showing the "Django-admin" button in all templates across the project.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        dict: Returns a context variable accessible in the navbar.html
    """
    return {
        "DEBUG": settings.DEBUG, 
    }

