import json
import os
import secrets
from datetime import datetime, timedelta
from typing import Optional, Dict, Any

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

SESSIONS_FILE = os.path.join(DATA_DIR, "sessions.json")
USERS_FILE = os.path.join(DATA_DIR, "users.json")


def read_json(path: str) -> dict:
    """Read JSON file and return as dict."""
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str, data: dict):
    """Write dict to JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def generate_token() -> str:
    """Generate a secure random token."""
    return secrets.token_urlsafe(32)


def create_session(phone: str) -> dict:
    """Create a new session for a user."""
    sessions = read_json(SESSIONS_FILE)
    token = generate_token()
    
    # Create session data with expiry (24 hours from now)
    expiry = (datetime.now() + timedelta(hours=24)).isoformat()
    
    session_data = {
        "phone": phone,
        "created_at": datetime.now().isoformat(),
        "expires_at": expiry,
        "active": True
    }
    
    sessions[token] = session_data
    write_json(SESSIONS_FILE, sessions)
    
    return {
        "token": token,
        "phone": phone,
        "expires_at": expiry
    }


def verify_token(token: str) -> Optional[Dict[str, Any]]:
    """Verify if token is valid and return session data."""
    sessions = read_json(SESSIONS_FILE)
    
    if token not in sessions:
        return None
    
    session = sessions[token]
    
    # Check if session is still active
    if not session.get("active"):
        return None
    
    # Check if session has expired
    expires_at = datetime.fromisoformat(session["expires_at"])
    if datetime.now() > expires_at:
        session["active"] = False
        write_json(SESSIONS_FILE, sessions)
        return None
    
    return session


def logout(token: str) -> bool:
    """Logout a user by deactivating their session."""
    sessions = read_json(SESSIONS_FILE)
    
    if token in sessions:
        sessions[token]["active"] = False
        write_json(SESSIONS_FILE, sessions)
        return True
    
    return False


def get_user_sessions(phone: str) -> list:
    """Get all active sessions for a user."""
    sessions = read_json(SESSIONS_FILE)
    user_sessions = []
    
    for token, session in sessions.items():
        if session["phone"] == phone and session.get("active"):
            expires_at = datetime.fromisoformat(session["expires_at"])
            if datetime.now() <= expires_at:
                user_sessions.append({
                    "token": token,
                    "created_at": session["created_at"],
                    "expires_at": session["expires_at"]
                })
    
    return user_sessions
