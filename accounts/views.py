from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

User = get_user_model()


def login_view(request):
    if request.user.is_authenticated:
        return redirect("welcome")

    if request.method == "POST":
        email_or_username = request.POST.get("email_or_username", "").strip()
        password = request.POST.get("password", "")
        username = email_or_username
        if "@" in email_or_username:
            user = User.objects.filter(email__iexact=email_or_username).first()
            username = user.get_username() if user else email_or_username

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("welcome")
        messages.error(request, "That email/username and password don't match.")

    return render(request, "accounts/login.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("welcome")

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        agreed = request.POST.get("agree") == "on"
        errors = []

        if not name:
            errors.append("Please enter your name.")
        if not email or "@" not in email:
            errors.append("Please enter a valid email address.")
        elif User.objects.filter(email__iexact=email).exists():
            errors.append("An account with that email already exists.")
        if len(password) < 8:
            errors.append("Your password must be at least 8 characters long.")
        if not agreed:
            errors.append("Please agree to the Terms of Service and Privacy Policy.")

        if not errors:
            base_username = email.split("@", 1)[0].strip() or "user"
            username = base_username
            suffix = 1
            while User.objects.filter(username__iexact=username).exists():
                username = f"{base_username}{suffix}"
                suffix += 1
            first_name = name.split()[0]
            last_name = " ".join(name.split()[1:])
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            messages.success(request, "Your account is ready. Please log in.")
            return redirect("login")

        for error in errors:
            messages.error(request, error)

    return render(request, "accounts/register.html")


@login_required
def welcome_view(request):
    return render(request, "accounts/welcome.html")


def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect("login")
