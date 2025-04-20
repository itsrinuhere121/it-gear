# backend/app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite configuration (for development)
# Use environment variables instead of hardcoding
import os
DATABASE_URL = "mysql+pymysql://root:rootpass@localhost:3306/GearTrack"

engine = create_engine(DATABASE_URL)
# Create database engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
Base.metadata.create_all(bind=engine)