# Django E-Commerce Project 🛒

Welcome to my Django E-Commerce web application! This project was built to demonstrate a functional online store with features like product management, a shopping cart, and user authentication.

## 🚀 Features

- **Product Catalog**: Browse a wide range of products with high-quality images and descriptions.
- **Dynamic Search**: Easily find products using the built-in search functionality.
- **Shopping Cart**: Add items to your cart and manage them before "checkout".
- **User Authentication**: Secure login and logout system with a personalized user profile page.
- **Admin Dashboard**: Full administrative control to add, edit, or delete products and categories.
- **Responsive Design**: Built with Bootstrap 5 to ensure a great experience on both mobile and desktop.

## 🛠️ Tech Stack

- **Backend**: Django 6.0 (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5.3
- **Database**: SQLite3
- **Authentication**: Django's built-in Auth System
- **Session Management**: Session-based Shopping Cart

## 📦 Installation & Setup

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <YOUR_GITHUB_REPO_URL>
   cd myproject
   ```

2. **Create and activate a virtual environment**:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```powershell
   python manage.py migrate
   ```

5. **Start the development server**:
   ```powershell
   python manage.py runserver 8001
   ```

6. **Access the app**:
   Open your browser and visit [http://127.0.0.1:8001/](http://127.0.0.1:8001/)

## 🔑 Admin Access

To access the admin dashboard at `/admin/`, you can create a superuser:
```powershell
python manage.py createsuperuser
```

---
*Created by Dilli as a final project for demonstrating web development skills.*
