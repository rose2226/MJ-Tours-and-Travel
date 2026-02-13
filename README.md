# MJ Tours & Travels - Professional Travel Website

A sophisticated, multi-page tour and travel website built with Flask, HTML, CSS, and JavaScript. Features elegant green color scheme, smooth animations, slideshow functionality, and comprehensive booking system.

## 🌟 Features

- **Multi-page Architecture**: Home, About, Destinations, Tours, Itineraries, Blog, Testimonials, Contact, Booking
- **Elegant Design**: Classic green and gold color scheme with professional typography
- **Hero Slideshow**: Animated background slideshow on homepage
- **Responsive Layout**: Mobile-first design that works on all devices
- **Booking System**: Functional booking form with Flask backend
- **Contact Form**: Elegant contact page with map integration
- **Animations**: Scroll-triggered animations and smooth transitions
- **CEO Section**: Dedicated space for CEO photo and information on About page
- **Blog & Testimonials**: Dedicated pages for content and reviews
- **Interactive Features**: Counters, carousels, filters, and more

## 📁 Project Structure

```
mj-tours-website/
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── bookings.json              # Booking data storage
├── contacts.json              # Contact form submissions
├── static/
│   ├── css/
│   │   ├── style.css          # Main stylesheet
│   │   └── additional.css     # Additional utilities
│   ├── js/
│   │   └── main.js            # JavaScript functionality
│   ├── images/                # Logo and icons
│   └── assets/                # Your images, videos, etc.
│       ├── hero1.jpg          # Hero slideshow image 1
│       ├── hero2.jpg          # Hero slideshow image 2
│       ├── hero3.jpg          # Hero slideshow image 3
│       ├── hero4.jpg          # Hero slideshow image 4
│       ├── ceo-photo.jpg      # CEO photograph (IMPORTANT)
│       ├── welcome.jpg        # Welcome section image
│       ├── our-story.jpg      # About page image
│       ├── team-member-1.jpg  # Team member photos
│       ├── team-member-2.jpg
│       ├── team-member-3.jpg
│       ├── dest-paris.jpg     # Destination images
│       ├── dest-bali.jpg
│       ├── dest-maldives.jpg
│       ├── dest-dubai.jpg
│       ├── dest-tokyo.jpg
│       ├── dest-santorini.jpg
│       ├── contact-image.jpg
│       ├── contact-bg.jpg
│       ├── booking-hero.jpg
│       └── ... (add more as needed)
└── templates/
    ├── base.html              # Base template
    ├── index.html             # Homepage
    ├── about.html             # About Us page
    ├── destinations.html      # Destinations page
    ├── tours.html             # Tours page
    ├── itineraries.html       # Itineraries page
    ├── blog.html              # Blog page
    ├── testimonials.html      # Testimonials page
    ├── contact.html           # Contact page
    └── booking.html           # Booking page
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Git
- A code editor (VS Code recommended)

### Step-by-Step Setup

1. **Clone or download the project**
   ```bash
   cd mj-tours-website
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # Activate on Windows
   venv\Scripts\activate
   
   # Activate on Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask
   ```

4. **Add your images to the assets folder**
   - Place all your images in `static/assets/`
   - **IMPORTANT**: Add CEO photo as `static/assets/ceo-photo.jpg`
   - Add hero slideshow images: `hero1.jpg`, `hero2.jpg`, `hero3.jpg`, `hero4.jpg`
   - Add destination images, team photos, etc.
   - You can use stock photos from Unsplash, Pexels, or your own

5. **Update CEO information**
   - Open `templates/about.html`
   - Find `[CEO Name]` and replace with actual name
   - Update CEO bio text

6. **Run the application**
   ```bash
   python app.py
   ```

7. **View in browser**
   - Open http://localhost:5000
   - The website should now be running!

## 🎨 Customization

### Colors
The color scheme uses CSS variables. To change colors, edit `static/css/style.css`:

```css
:root {
    --primary-green: #2d5016;      /* Main green */
    --secondary-green: #3d6b1f;    /* Secondary green */
    --gold: #d4af37;                /* Gold accent */
    /* ... more colors */
}
```

### Fonts
Current fonts:
- **Display**: Playfair Display (headings)
- **Body**: Montserrat (text)
- **Elegant**: Cormorant Garamond (accents)

To change, modify the Google Fonts import in `static/css/style.css`

### Contact Information
Update contact details in:
- `templates/base.html` (header and footer)
- `templates/contact.html` (contact page)
- `app.py` (email recipients)

### Adding New Destinations/Tours
1. Add images to `static/assets/`
2. Edit `templates/destinations.html` or `templates/tours.html`
3. Add new card sections following existing patterns

## 📱 Responsive Design

The website is fully responsive with breakpoints at:
- Mobile: < 768px
- Tablet: 768px - 1024px
- Desktop: > 1024px

## 🔧 Features Details

### Hero Slideshow
- Auto-plays with 5-second intervals
- Pause on hover
- Dot navigation
- Smooth fade transitions

### Booking System
- Stores submissions in `bookings.json`
- Form validation
- Flash messages for feedback
- Can be easily connected to a database

### Contact Form
- Stores submissions in `contacts.json`
- Email integration ready
- Google Maps embedded
- Elegant validation

### Animations
- Scroll-triggered fade-in animations
- Counter animations on statistics
- Hover effects on cards
- Smooth page transitions

## 🌐 Deployment

### GitHub
```bash
git init
git add .
git commit -m "Initial commit - MJ Tours & Travels"
git branch -M main
git remote add origin https://github.com/yourusername/mj-tours.git
git push -u origin main
```

### Heroku
1. Create `Procfile`:
   ```
   web: gunicorn app:app
   ```
2. Install gunicorn:
   ```bash
   pip install gunicorn
   pip freeze > requirements.txt
   ```
3. Deploy to Heroku

### Other Platforms
- **Vercel**: Use Flask adapter
- **Railway**: Direct Flask support
- **PythonAnywhere**: Upload and configure
- **DigitalOcean**: Use App Platform

## 📝 Content Guidelines

### Images
- **Hero images**: 1920x1080px, landscape, high quality
- **Destination cards**: 800x600px
- **CEO photo**: 600x800px, professional headshot
- **Team photos**: 500x500px, square
- **Blog images**: 1200x800px

### Writing Tone
- Professional yet approachable
- Emphasize luxury and expertise
- Use active voice
- Keep paragraphs concise

## 🔒 Security Notes

For production deployment:
1. Change the `secret_key` in `app.py`
2. Use environment variables for sensitive data
3. Implement CSRF protection
4. Add rate limiting
5. Use HTTPS
6. Sanitize all user inputs
7. Implement proper database instead of JSON files

## 🆘 Troubleshooting

**Images not showing?**
- Check file paths in templates
- Ensure images are in `static/assets/`
- Check file extensions (case-sensitive on Linux)

**Styles not applying?**
- Clear browser cache
- Check CSS file paths
- Verify Flask is serving static files

**Forms not submitting?**
- Check Flask is running
- Verify form action URLs
- Look for JavaScript errors in console

## 📞 Support

For issues or questions:
- Check the Flask documentation: https://flask.palletsprojects.com/
- Review HTML/CSS/JS in browser dev tools
- Ensure all dependencies are installed

## 📄 License

This project is created for MJ Tours & Travels. All rights reserved.

## 🎯 Next Steps

1. **Add real content**: Replace placeholder text with actual company information
2. **Professional photos**: Add high-quality images
3. **Database integration**: Connect to PostgreSQL or MongoDB
4. **Email system**: Set up automated booking confirmations
5. **Payment gateway**: Integrate Stripe or PayPal
6. **SEO optimization**: Add meta tags, sitemap, robots.txt
7. **Analytics**: Add Google Analytics
8. **Live chat**: Integrate customer support chat

---

**Built with care for MJ Tours & Travels** ✈️🌍

For best results, use high-quality images and customize all placeholder content with your actual company information.
