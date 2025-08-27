import pandas as pd
from slaw_data_loader import load_data
from slaw_config import SECTORS

def check_compliance(sector: str):
    """Check compliance for a given sector and return legality score and notes."""
    df = load_data()
    
    if sector not in df["sector"].values:
        return {"score": 0, "notes": f"Invalid sector: {sector}"}
    
    sector_data = df[df["sector"] == sector].iloc[0]  # get first match
    
    score = 100
    notes = []

    # Licensing requirement
    if sector_data["license_required"] == "Yes":
        score -= 20
        notes.append(f"Requires license: {sector_data['license_type']}.")

    # Foreign ownership cap
    max_ownership = sector_data["max%_foreign_ownership"]
    if max_ownership < 100:
        score -= 20
        notes.append(f"Foreign ownership capped at {max_ownership}%.")
    
    # Restrictions
    if pd.notna(sector_data["restrictions"]) and sector_data["restrictions"].strip() != "":
        score -= 20
        notes.append(f"Restrictions: {sector_data['restrictions']}.")

    # Ensure score is between 0 and 100
    score = max(0, min(score, 100))
    
    return {
        "score": score,
        "notes": " ".join(notes) if notes else "No major compliance issues."
    }
