# Course App

![Django](https://img.shields.io/badge/Django-5.1-green)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)
![License](https://img.shields.io/badge/License-MIT-red)

Course App is a Django-based online learning platform that allows users to browse, create, and manage courses. The platform features user authentication, course categorization, and a responsive design.

## 🌟 Features

- **User Authentication**: Secure registration and login system
- **Course Management**: Create, update, and delete courses
- **Category System**: Organize courses by categories with dynamic creation
- **Responsive Design**: Mobile-friendly interface that works on all devices
- **Admin Dashboard**: Comprehensive admin panel for managing content
- **Course Search**: Easily find courses by category or tags
- **Teacher Dashboard**: Instructors can manage their own courses

## 🛠️ Technologies Used

- **Backend**: Python 3.13+, Django 5.1+
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Database**: SQLite (default, easily switchable to PostgreSQL/MySQL)
- **Authentication**: Django's built-in authentication system
- **Static Files**: CSS, JavaScript, and image handling with Django's static files system

## 📁 Project Structure

```
courseapp/
├── accounts/          # User authentication and profiles
│   ├── migrations/    # Database migrations
│   ├── templates/     # Account-related templates
│   ├── admin.py       # Admin panel configuration
│   ├── apps.py        # App configuration
│   ├── forms.py       # User forms
│   ├── models.py      # User-related models
│   ├── urls.py        # URL routing
│   └── views.py       # View functions
├── courses/           # Course management and display
│   ├── migrations/    # Database migrations
│   ├── templates/     # Course-related templates
│   ├── admin.py       # Admin panel configuration
│   ├── apps.py        # App configuration
│   ├── forms.py       # Course forms
│   ├── models.py      # Course models
│   ├── urls.py        # URL routing
│   └── views.py       # View functions
├── pages/             # Static pages (home, about)
│   ├── migrations/    # Database migrations
│   ├── templates/     # Page templates
│   ├── admin.py       # Admin panel configuration
│   ├── apps.py        # App configuration
│   ├── models.py      # Page models
│   ├── urls.py        # URL routing
│   └── views.py       # View functions
├── static/            # CSS, JavaScript, and images
│   ├── css/           # Stylesheets
│   ├── js/            # JavaScript files
│   └── img/           # Image files
├── templates/         # Base templates and partials
│   ├── partials/      # Reusable template components
│   └── base.html      # Base template
├── media/             # User-uploaded content
├── manage.py          # Django management script
├── requirements.txt   # Project dependencies
├── LICENSE            # License information
└── README.md          # Project documentation
```

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/courseapp.git
   cd courseapp
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional but recommended):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Visit the application**:
   Open your browser and go to `http://127.0.0.1:8000`

## 👤 Default Admin User

A default admin user has been created for testing purposes:
- **Username**: `admin`
- **Email**: `admin@example.com`
- **Password**: `admin123`

You can access the admin panel at `http://127.0.0.1:8000/admin/`

## 🎨 Design Features

- **Modern Color Scheme**: Red and blue gradient with green accents
- **Responsive Layout**: Works on mobile, tablet, and desktop
- **Interactive Elements**: Hover effects and smooth transitions
- **Social Media Integration**: Footer with social media links
- **Clean Typography**: Poppins font for a modern look

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Create a new Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For support or questions, please contact:
- Email: info@courseapp.com
- Phone: 0552 576 38 94

## 🙏 Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)