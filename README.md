# Django Project multiple databases

## Step 1: Create a Virtual Environment
Create a virtual environment and activate:
- On Windows:
    ```
    python -m venv env
    env\Scripts\activate.bat
    ```
- On Unix/MacOS:
    ```
    python -m venv env
    source env/bin/activate
    ```

## Step 2: Install Django
```
pip install django
```

## Step 3: Run Migrations
```
python manage.py migrate_all
```

## Step 4: Run the Django Project
Start the development server with the following command:
```
python manage.py runserver
```
Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view your application.
