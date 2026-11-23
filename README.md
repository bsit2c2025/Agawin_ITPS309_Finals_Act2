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
