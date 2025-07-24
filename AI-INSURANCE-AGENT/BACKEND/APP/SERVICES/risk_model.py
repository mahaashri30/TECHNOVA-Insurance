def calculate_risk(user_profile: dict) -> str:
    age = user_profile.get("age", 30)
    if age < 35:
        return "Low Risk"
    elif age < 50:
        return "Medium Risk"
    else:
        return "High Risk"
