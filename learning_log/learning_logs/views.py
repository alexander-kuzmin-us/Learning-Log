from django.shortcuts import render


# Views for learning logs.
def index(request):
    """The home page for learning log."""
    return render(request, 'learning_logs/index.html')

