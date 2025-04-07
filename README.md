# Learning Log: Track Your Learning Journey with confidence!

A robust web application built with Django that helps you track and organize your learning progress. Keep a record of topics you're interested in and maintain detailed journal entries as you learn about each subject

![Django](https://img.shields.io/badge/Django-3.1.4-green)
![Bootstrap4](https://img.shields.io/badge/Bootstrap-4-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Features

- **User Authentication**: Secure registration and login system
- **Topic Management**: Create, view, and organize your learning topics
- **Journal Entries**: Add detailed entries to each topic as you learn
- **User Privacy**: Each user can only access their own topics and entries
- **Responsive Design**: Mobile-friendly interface using Bootstrap 4

## Getting Started

### Prerequisites

- Python 3.6+
- Django 3.1+
- Bootstrap4

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/learning-log.git
   cd learning-log
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

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at: `http://localhost:8000`

## Usage

1. **Register an Account**: Create a new account to get started
2. **Add Topics**: Add topics you're interested in learning
3. **Create Entries**: Add detailed journal entries to track your learning progress
4. **Edit and Update**: Modify your entries as you learn more

## Project Structure

- **learning_logs**: Main application for topic and entry management
- **users**: Application handling user authentication and profiles
- **templates**: HTML templates for rendering views
- **forms**: Form definitions for data input

## Security

- User data is protected with Django's authentication system
- Each user can only access their own topics and entries
- CSRF protection enabled for all forms

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add some amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- This project was created as a final project for the CS50 Web track
- Built with Django framework
- Styled with Bootstrap 4
