from random import randint
from django.shortcuts import render


def get_image(request):
    # nginx -> load folder
    # object storage -> aws S3 -> clouflare r2
    # django-storages
    # whitenoise (simflify - no configuration)
    pass


# Create your views here.
def dashboard_webpage(request, *args, **kwagrs):
    print(request.user, request.user.is_authenticated)
    # if not request.user.is_authenticated:
    #     return redirect("/auth/google/login")
    my_value = str(request.user) + f"{randint(0, 12546656545646)}"
    template_context = {
        "my_value": my_value,
        "not_actual_context": "not it´s ready",
        "colors": ["red", "blue"],
    }
    return render(request, "dashboard/main.html", template_context)


def about_us_page(request):
    return render(request, "about.html")
