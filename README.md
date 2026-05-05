# Mbokazi, Magembe Hopewell Thulebona Musa - Portfolio

**Systems Developer**

A professional portfolio showcasing expertise in systems development, full-stack web applications, and software architecture. This project has been upgraded to a **full-stack system** with a dedicated database and administrative backend.

## 🌟 Key Features

- **Dynamic Database Layer:** Integrated **SQLAlchemy** with a SQLite database to manage skills, projects, and inbound messages.
- **Secure Authentication:** Protected administrative area using **Flask-Login** with hashed passwords for secure data management.
- **Interactive AJAX Contact Form:** Real-time message submission using the **Fetch API**, providing instant feedback without page reloads.
- **Admin Dashboard:** A private interface (`/admin/messages`) to view and manage contact requests from potential clients.
- **Single-Page Scroll Experience:** Smooth, full-height sections with **CSS Scroll Snapping** for a modern, fluid user journey.
- **Animated Scroll Reveal:** Intersection Observer logic that triggers entry animations as you explore the site.

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Jinja2, **Flask-SQLAlchemy**, **Flask-Login**
- **Database:** SQLite
- **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript (ES6+)
- **Typography:** Outfit (Google Fonts)

## 📁 Project Structure

```text
my-profile/
├── app.py              # Application logic, Database models & Routes
├── portfolio.db        # SQLite database file (Auto-generated)
├── requirements.txt    # Project dependencies
├── static/             # Static assets
│   ├── css/
│   │   └── style.css   # Premium glassmorphic styles
│   └── images/         # Profile and project images
└── templates/          # HTML Templates
    ├── index.html      # Main landing page
    ├── login.html      # Secure admin login portal
    └── admin_messages.html # Private message dashboard
```

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd my-profile
   ```

2. **Set up Virtual Environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # .venv\Scripts\activate   # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```
   *Note: The database and default admin user are automatically initialized on the first run.*

5. **View in browser:**
   - Public Site: [http://127.0.0.1:5000](http://127.0.0.1:5000)
   - Admin Login: [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login)

## 🔐 Default Admin Credentials

- **Username:** `admin`
- **Password:** `admin123`
*(Please ensure you change these in `app.py` before any public deployment.)*

## 📫 Contact Information

- **Tel:** 0606086023
- **Email:** [musambokazi2000@gmail.com](mailto:musambokazi2000@gmail.com)

---
© 2025 Mbokazi Magembe Hopewell Thulebona Musa