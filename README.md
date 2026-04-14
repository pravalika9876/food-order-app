# GastroGo - Premium Food Delivery Web App

A production-level food ordering simulation built with Flask, SQLAlchemy, and SocketIO.

## 🚀 Features
- **User Authentication**: Secure login/register system.
- **Dynamic Restaurant Listing**: Browse restaurants with ratings and categories.
- **Interactive Menu**: Add items to cart with live updates.
- **AI Recommendation**: "People also ordered" feature based on cart actions.
- **Real-time Order Tracking**: Leaflet.js map with simulated rider movement.
- **Voice Search**: Search for food using your voice (Speech Recognition API).
- **Dark/Light Mode**: Sleek theme toggle with persistent storage.
- **Modern UI**: Glassmorphism, premium typography, and smooth animations.

## 🛠️ Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install flask flask-sqlalchemy flask-login flask-socketio flask-cors
   ```

2. **Seed the Database**:
   ```bash
   python seed.py
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the App**:
   Open `http://localhost:5000` in your browser.

## 📁 Project Structure
- `app.py`: Backend routes and logic.
- `models.py`: Database schema.
- `seed.py`: Initial data population.
- `static/`: CSS and assets.
- `templates/`: HTML templates with Jinja2.
- `foodapp.db`: SQLite database (generated after seed).
