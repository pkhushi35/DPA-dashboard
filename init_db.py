from database import Base, engine
from models import ThreatIndicator

Base.metadata.create_all(bind=engine)
print("Database tables created.")