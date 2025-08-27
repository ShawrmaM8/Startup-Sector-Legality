import os

BASE_DIR = r"C:\Users\muzam\OneDrive\Desktop\PROJECTS\Education\Micro Projects\3.2) Startup Category Law"

# Paths
DATA_PATH = os.path.join(BASE_DIR, "slaw_data", "qtr_startup_regulations.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "lawscorer.pkl")


SECTORS = [
    "EdTech", "FinTech", "HealthTech", "ECommerce", "AgriTech", "CleanTech",
    "PropTech", "LegalTech", "GovTech", "Media & Entertainment", "Gaming",
    "Cybersecurity", "AI & Data Science", "Robotics", "Manufacturing & Industry 4.0",
    "Energy & Utilities", "Transportation & Mobility", "Food & Beverage", "Retail",
    "Travel & Hospitality", "Logistics & Supply Chain", "Biotech & Pharma",
    "Consumer Electronics", "Social Impact / Non-Profit", "Other"
]
