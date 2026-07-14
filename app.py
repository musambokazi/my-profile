from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Database Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'portfolio.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=False)
    github_url = db.Column(db.String(200), nullable=True)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Initial Data
about_data = {
    "name": "Mbokazi, Magembe H T Musa",
    "title": "Systems Developer",
    "bio": [
        "I'm a dedicated Systems Developer with a passion for building innovative solutions that drive business success. I specialize in creating robust, scalable applications that solve real-world problems.",
        "With expertise in modern web technologies and software engineering practices, I deliver high-quality solutions that transform ideas into powerful digital products."
    ],
    "profile_pic": "nobackg.png",
    "nav_profile": "profile pic.jpg",
    "logo": "logo.png",
    "github": "https://github.com/musambokazi"
}

def init_db():
    with app.app_context():
        db.create_all()
        # Create admin user if not exists
        if User.query.filter_by(username='admin').first() is None:
            hashed_pw = generate_password_hash('admin123') # Default password
            admin = User(username='admin', password_hash=hashed_pw)
            db.session.add(admin)
        
        if Skill.query.count() == 0:
            skills = [
                Skill(name="Web Development", description="Full-stack web applications with HTML5, CSS3, and responsive design"),
                Skill(name="Frontend Development", description="Interactive user interfaces with JavaScript and React"),
                Skill(name="Backend Development", description="Server-side solutions with Python and modern frameworks"),
                Skill(name="Software Architecture", description="Object-oriented design and C# enterprise applications"),
                Skill(name="Systems Integration", description="Connecting and optimizing complex software systems for seamless operation")
            ]
            db.session.bulk_save_objects(skills)
        
        if Project.query.count() == 0:
            projects = [
                Project(title="Web Portfolio Platform", image="logo.png", description="A responsive portfolio website built with HTML5, CSS3, and vanilla JavaScript.", github_url="https://github.com/musambokazi/my-profile"),
                Project(title="React Kasi Mashesha App (Delivary App)", image="applogo.png", description="A dynamic web application with React featuring real-time data visualization.", github_url="https://github.com/musambokazi/kasi-mashesha"),
                Project(title="Full-Stack System Solution", image="back ground.jpg", description="An enterprise-level application combining Python backend, C# components, and a modern frontend.", github_url="https://github.com/musambokazi/enterprise-solution")
            ]
            db.session.bulk_save_objects(projects)
        
        db.session.commit()

@app.route('/')
def index():
    skills = Skill.query.all()
    projects = Project.query.all()
    return render_template('index.html', about=about_data, skills=skills, projects=projects)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('view_messages'))
        flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/contact', methods=['POST'])
def contact():
    data = request.form
    if request.is_json:
        data = request.get_json()
    
    name = data.get('name')
    email = data.get('email')
    message_text = data.get('message')
    
    if not name or not email or not message_text:
        if request.is_json:
            return jsonify({"status": "error", "message": "All fields are required."}), 400
        flash("All fields are required.", "error")
        return redirect(url_for('index', _anchor='contact'))

    new_message = Message(name=name, email=email, message=message_text)
    db.session.add(new_message)
    db.session.commit()
    
    if request.is_json:
        return jsonify({"status": "success", "message": f"Thank you, {name}! Your message has been sent."})
    
    flash(f"Thank you, {name}! Your message has been sent successfully.", "success")
    return redirect(url_for('index', _anchor='contact'))

@app.route('/admin/messages')
@login_required
def view_messages():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('admin_messages.html', messages=messages)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
