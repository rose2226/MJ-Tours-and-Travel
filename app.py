from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from datetime import datetime
import json
import os
BOOKINGS_FILE = 'bookings.json'
CONTACTS_FILE = 'contacts.json'
FEEDBACK_FILE = 'feedback.json'

# Admin credentials 
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'mjtours@2026'  

app = Flask(__name__)
app.secret_key = 'mj-tours-secret-key-2026'

# Store bookings and contacts in JSON files (in production, use a database)
BOOKINGS_FILE = 'bookings.json'
CONTACTS_FILE = 'contacts.json'

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/destinations')
def destinations():
    return render_template('destinations.html')

@app.route('/tours')
def tours():
    return render_template('tours.html')

@app.route('/itineraries')
def itineraries():
    return render_template('itineraries.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    try:
        booking_data = {
            'id': datetime.now().strftime('%Y%m%d%H%M%S'),
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'phone': request.form.get('phone'),
            'destination': request.form.get('destination'),
            'tour_package': request.form.get('tour_package'),
            'travel_date': request.form.get('travel_date'),
            'travelers': request.form.get('travelers'),
            'special_requests': request.form.get('special_requests'),
            'timestamp': datetime.now().isoformat()
        }
        
        bookings = load_data(BOOKINGS_FILE)
        bookings.append(booking_data)
        save_data(BOOKINGS_FILE, bookings)
        
        flash('Your booking request has been submitted successfully! We will contact you shortly.', 'success')
        return redirect(url_for('booking'))
    except Exception as e:
        flash('An error occurred. Please try again.', 'error')
        return redirect(url_for('booking'))

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    try:
        contact_data = {
            'id': datetime.now().strftime('%Y%m%d%H%M%S'),
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'subject': request.form.get('subject'),
            'message': request.form.get('message'),
            'timestamp': datetime.now().isoformat()
        }
        
        contacts = load_data(CONTACTS_FILE)
        contacts.append(contact_data)
        save_data(CONTACTS_FILE, contacts)
        
        flash('Thank you for contacting us! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    except Exception as e:
        flash('An error occurred. Please try again.', 'error')
        return redirect(url_for('contact'))

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    try:
        feedback_data = {
            'id': datetime.now().strftime('%Y%m%d%H%M%S'),
            'name': request.form.get('name') or 'Anonymous',
            'email': request.form.get('email') or 'Not provided',
            'rating': request.form.get('rating'),
            'comment': request.form.get('comment'),
            'timestamp': datetime.now().isoformat()
        }
        
        feedback = load_data(FEEDBACK_FILE)
        feedback.append(feedback_data)
        save_data(FEEDBACK_FILE, feedback)
        
        flash('Thank you for your feedback! We appreciate it! ⭐', 'success')
        return redirect(request.referrer or url_for('index'))
    except Exception as e:
        flash('An error occurred. Please try again.', 'error')
        return redirect(request.referrer or url_for('index'))

# Admin Login
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            flash('Welcome to MJ Tours Admin Dashboard!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('admin_login.html')

# Admin Logout
@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('admin_login'))

# Check if admin is logged in
def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            flash('Please login to access admin panel', 'error')
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

# Admin Dashboard
@app.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    # Load all data
    bookings = load_data(BOOKINGS_FILE)
    contacts = load_data(CONTACTS_FILE)
    feedback = load_data(FEEDBACK_FILE)
    
    # Calculate statistics
    total_bookings = len(bookings)
    total_contacts = len(contacts)
    total_feedback = len(feedback)
    
    # Calculate average rating
    if feedback:
        ratings = [int(f['rating']) for f in feedback if f.get('rating')]
        avg_rating = round(sum(ratings) / len(ratings), 1) if ratings else 0
    else:
        avg_rating = 0
    
    # Get recent items (last 5)
    recent_bookings = sorted(bookings, key=lambda x: x['timestamp'], reverse=True)[:5]
    recent_contacts = sorted(contacts, key=lambda x: x['timestamp'], reverse=True)[:5]
    recent_feedback = sorted(feedback, key=lambda x: x['timestamp'], reverse=True)[:5]
    
    return render_template('admin_dashboard.html',
                         total_bookings=total_bookings,
                         total_contacts=total_contacts,
                         total_feedback=total_feedback,
                         avg_rating=avg_rating,
                         recent_bookings=recent_bookings,
                         recent_contacts=recent_contacts,
                         recent_feedback=recent_feedback)

# View All Bookings
@app.route('/admin/bookings')
@admin_required
def admin_bookings():
    bookings = load_data(BOOKINGS_FILE)
    bookings = sorted(bookings, key=lambda x: x['timestamp'], reverse=True)
    return render_template('admin_bookings.html', bookings=bookings)

# View All Contacts
@app.route('/admin/contacts')
@admin_required
def admin_contacts():
    contacts = load_data(CONTACTS_FILE)
    contacts = sorted(contacts, key=lambda x: x['timestamp'], reverse=True)
    return render_template('admin_contacts.html', contacts=contacts)

# View All Feedback
@app.route('/admin/feedback')
@admin_required
def admin_feedback():
    feedback = load_data(FEEDBACK_FILE)
    feedback = sorted(feedback, key=lambda x: x['timestamp'], reverse=True)
    
    # Calculate average rating
    if feedback:
        ratings = [int(f['rating']) for f in feedback if f.get('rating')]
        avg_rating = round(sum(ratings) / len(ratings), 1) if ratings else 0
    else:
        avg_rating = 0
    
    return render_template('admin_feedback.html', feedback=feedback, avg_rating=avg_rating)

# Delete Booking
@app.route('/admin/delete_booking/<booking_id>', methods=['POST'])
@admin_required
def delete_booking(booking_id):
    bookings = load_data(BOOKINGS_FILE)
    bookings = [b for b in bookings if b['id'] != booking_id]
    save_data(BOOKINGS_FILE, bookings)
    flash('Booking deleted successfully', 'success')
    return redirect(url_for('admin_bookings'))

# Delete Contact
@app.route('/admin/delete_contact/<contact_id>', methods=['POST'])
@admin_required
def delete_contact(contact_id):
    contacts = load_data(CONTACTS_FILE)
    contacts = [c for c in contacts if c['id'] != contact_id]
    save_data(CONTACTS_FILE, contacts)
    flash('Contact deleted successfully', 'success')
    return redirect(url_for('admin_contacts'))

# Delete Feedback
@app.route('/admin/delete_feedback/<feedback_id>', methods=['POST'])
@admin_required
def delete_feedback(feedback_id):
    feedback = load_data(FEEDBACK_FILE)
    feedback = [f for f in feedback if f['id'] != feedback_id]
    save_data(FEEDBACK_FILE, feedback)
    flash('Feedback deleted successfully', 'success')
    return redirect(url_for('admin_feedback'))

if __name__ == '__main__':
    # Use environment variable for port (Render provides this)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
