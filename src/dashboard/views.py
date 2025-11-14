from django.shortcuts import render


# Create your views here.
def dashboard_webpage(request, *args, **kwagrs):
    print(request.user, request.user.is_authenticated)
    # if not request.user.is_authenticated:
    #     return redirect("/auth/google/login")
    my_value = str(request.user)
    template_context = {
        "my_value": my_value,
        "not_actual_context": "not it´s ready",
        "colors": ["red", "blue"],
    }
    return render(request, "dashboard.html", template_context)
