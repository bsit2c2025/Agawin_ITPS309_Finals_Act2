# Login & Register Form

A small Django project with separate login and registration pages, styled after the Activity #1 designs.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/>. Create an account from the Register link. Use its email or generated username with the password to log in. Usernames are generated from the part of the email before `@` and made unique when needed.

The login and registration fields use floating labels: the label moves up and shrinks when the field is focused or has a value. The password reset flow prints its email and reset link in the Django development server terminal.

## Pages

- `/` — Login
- `/register/` — Register
- `/password-reset/` — Request a reset link
- `/admin/` — Django admin

For a class deployment, set a new `SECRET_KEY`, set `DEBUG = False`, and add the deployed hostname to `ALLOWED_HOSTS` in `authsite/settings.py`.


# Screenshots

Login Page
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/9ba0f7e3-2871-424f-acb8-d1cfa57af2bc" />

Register Page
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/35a87288-96e5-43f9-8951-58df48b89de2" />

Success Login
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/18de0fcb-3e35-45d3-82ba-f11e93935ea0" />

Forgot Password
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/9059e4ac-552d-4e02-8966-a683ec1261c3" />



