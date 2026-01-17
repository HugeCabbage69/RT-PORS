# RT-PORS - Real-Time Power Outage Reporting System

A comprehensive web application designed to help users track and report power outages in real-time, making life easier during blackouts.

## Overview

RT-PORS enables users to:
- **Report power outages** in their locality with geographic data
- **View outage status** on an interactive map in real-time
- **Receive OTP-based authentication** for secure access - Yet to be implemented properly
- **Mark affected areas** to help the community stay informed
- **Access critical information** about outages and status updates



## Technology Stack

### Backend
- **Framework**: FastAPI (Python)
- **Validation**: Pydantic
- **Server**: Uvicorn
- **Data Storage**: JSON (temporary) → MySQL (planned)
- **Dependencies**: fastapi, pydantic, uvicorn, requests

### Frontend
- **HTML5/CSS3** - Responsive web interface
- **JavaScript** - Interactive functionality
- **Leaflet.js** - Interactive mapping and geolocation
- **Maps**: Real-time outage visualization

## Features

### Authentication 
(Still Working on it)
- **OTP-Based Login** - Secure one-time password authentication
- **User Registration** - Create new user accounts
- **Session Management** - Persistent user sessions

### Reporting
- **Report Outages** - Submit power outage reports with location
- **Mark Affected Areas** - Identify and mark regions experiencing outages
- **Real-time Updates** - View live status of reported outages

### User Interface
- **Interactive Map** - Leaflet-based map showing outages
- **Responsive Design** - Works on desktop and mobile browsers
- **User Profile** - Account management and preferences


## Installation & Setup

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd BACKEND
   ```

2. Install dependencies:
   
   ```bash
   cd BACKEND
   pip install -r requirements.txt
   ```
   Or install manually:
   ```bash
   pip install fastapi pydantic uvicorn requests
   ```

3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd Frontend
   ```

2. Open `index.html` in a web browser or serve via a local HTTP server:
   ```bash
   # Using Python
   python -m http.server 8001
   ```

3. Access the application at `http://localhost:8001`

## Current Status

-  Backend structure **initialized** with FastAPI
-  Frontend UI with interactive map
-  Login routes (in progress)
-  Database migration to MySQL (planned)

## Database Schema (Current)

### Users (`users.json`)
- User registration and authentication data

### OTPs (`otps.json`)
- OTP verification records

### Marked Areas (`marked_areas.json`)
- User-reported power outage locations

## Future Enhancements

- [ ] MySQL database implementation
- [ ] Real-time notifications for outages
- [ ] Worker side application to update status
- [ ] Mobile app (React Native/Expo)
- [ ] Advanced filtering and analytics
- [ ] Integration with power distribution companies
- [ ] Community ratings and reviews

## Support

For issues, questions, or suggestions, please open an issue in the project repository.


