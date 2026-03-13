from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
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

if __name__ == '__main__':
    # Use environment variable for port (Render provides this)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
