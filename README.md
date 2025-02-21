# Django Project

## Project Structure
```
Question_1,Question_2,Question_3/                  # Root directory of the project
│
├── Question_1, Question_2, Question_3/            # Main project directory
│   ├── __init__.py         # Marks the directory as a Python package
│   ├── settings.py         # Project settings and configuration
│   ├── urls.py             # Root URL configuration
│   ├── asgi.py             # ASGI configuration for async server support
│   └── wsgi.py             # WSGI configuration for deployment
│
├── Home/                  # Example Django app
│   ├── migrations/         # Database migration files
│   ├── __init__.py         # Marks the app as a Python package
│   ├── admin.py            # Admin configuration for the app
│   ├── apps.py             # App configuration
│   ├── models.py           # Database models
│   ├── tests.py            # Test cases
│   ├── views.py            # View functions/classes
│   ├── signals.py          # Signal handlers (All answers are in this file)
│   └── ...
│
├── manage.py               # Command-line utility for Django
└── requirements.txt        # List of project dependencies
```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Run the server:
   ```sh
   python manage.py runserver
   ```

## Usage
- The main project structure contains three directories: `Question_1`, `Question_2`, and `Question_3`.
- The `Home` app contains models, views, admin configuration, and Django signals.
- All signal-related logic is implemented in `Home/signals.py`.

## Contributing
Feel free to fork this repository, submit issues, and create pull requests.

## License
This project is licensed under the MIT License.

