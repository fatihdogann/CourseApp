# Course App

Course App is a Django-based online learning platform that allows users to browse, create, and manage courses. The platform features user authentication, course categorization, and a responsive design.

## Features

- User registration and authentication
- Course creation and management
- Course categorization
- Responsive design for all devices
- Search and filtering capabilities
- User dashboards for course instructors

## Technologies Used

- Python 3.13+
- Django 5.1+
- Bootstrap 5
- SQLite (default database)
- HTML5 & CSS3

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/courseapp.git
   cd courseapp
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000` in your browser

## Project Structure

```
courseapp/
├── accounts/          # User authentication and profiles
├── courses/           # Course management and display
├── pages/             # Static pages (home, about)
├── static/            # CSS, JavaScript, and images
├── templates/         # HTML templates
├── manage.py          # Django management script
└── requirements.txt   # Project dependencies
```

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.