# MJ Tours & Travels - Premium Travel Booking Platform

**Live Website:** [https://mjtoursandtravel.pythonanywhere.com](https://mjtoursandtravel.pythonanywhere.com)

---

## 🌍 About Us

MJ Tours & Travels is a comprehensive travel booking platform offering curated tour packages to over **150+ destinations** worldwide. From luxury getaways and cultural tours to adventure expeditions, we specialize in creating unforgettable travel experiences with expert guides, premium accommodations, and seamless logistics.

Whether you're dreaming of a romantic escape or an adrenaline-filled adventure, MJ Tours & Travels delivers personalized journeys with professionalism and passion.

---

## ✨ Features

### Customer-Facing Features
- **150+ Destinations** across 6 continents
- **Curated Tour Packages** with durations from 5 to 14 days
- **Detailed Day-by-Day Itineraries** including activities and highlights
- **Travel Videos** – stunning destination footage and tour previews
- **Customer Reviews & Testimonials**
- **Travel Blog** – expert tips, destination guides, and travel insights
- **Online Booking System** – simple and secure booking process
- **Multiple Contact Forms** for inquiries
- **Visitor Feedback System** with star ratings and comments
- **Fully Mobile Responsive** design

### Admin Features
- **Secure Admin Dashboard** with protected login
- **Booking Management** – view, track, and update bookings
- **Contact & Inquiry Management**
- **Feedback Analytics** – monitor customer satisfaction
- **Statistics Dashboard** – key performance metrics
- **Data Export** – download customer and booking data
- **Delete/Archive** functionality for historical records

### Analytics & Tracking
- **Google Analytics** integration
- **Event Tracking** for bookings, contacts, and feedback
- **Real-time Statistics** on visitor behavior and engagement

---

## 🛠️ Technology Stack

### Backend
- **Framework**: Flask (Python 3.10)
- **Session Management**: Flask Sessions
- **Data Storage**: JSON file-based system
- **Email**: Flask-Mail (SMTP ready)

### Frontend
- **HTML5 & CSS3** with semantic markup
- **JavaScript (ES6+)** for interactivity and form validation
- **Font Awesome 6.4.0** for icons
- **Google Fonts**: Anton, Crimson Text, Work Sans, Cinzel

### Design & UX
- **Primary Colors**: Green (`#2d5016`) & Gold (`#d4af37`)
- **Typography**: Elegant editorial style with modern accents
- **Animations**: Smooth CSS transitions and scroll effects
- **Approach**: Mobile-first, fully responsive design

### Deployment
- **Hosting**: PythonAnywhere
- **Version Control**: Git & GitHub

---

## 📁 Project Structure

```bash
MJ-Tours-and-Travel/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── .gitignore
├── static/
│   ├── assets/                 # Images, logo, videos
│   ├── css/                    # Stylesheets
│   └── js/                     # JavaScript files
└── templates/
    ├── base.html               # Base template
    ├── index.html
    ├── tours/
    ├── admin/
    ├── contact.html
    └── ...
