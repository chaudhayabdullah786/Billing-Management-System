import os
from datetime import timedelta

class Config:
    # Secret key for sessions
    SECRET_KEY = os.environ.get('SESSION_SECRET') or 'dev-secret-key-change-in-production'
    
    # Database URI (fallback to local SQLite)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///grocery.db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 300,
        'pool_pre_ping': True,
    }
    
    # Session lifetime
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
    # File upload limits
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    
    # Business logic
    TAX_RATE = 0.18
    LOW_STOCK_THRESHOLD = 10
