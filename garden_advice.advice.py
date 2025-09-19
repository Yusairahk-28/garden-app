"""Provides gardening advice based on the season and plant type."""

# Gardening advice 
ADVICE = {
    "summer": {
        "flower": "Water your plants regularly and provide some shade.\nUse fertilizer to encourage blooms.",
        "vegetable": "Water your plants regularly and provide some shade.\nKeep an eye out for pests!"
    },
    "winter": {
        "flower": "Protect your plants from frost with covers.\nUse fertilizer sparingly.",
        "vegetable": "Protect your plants from frost with covers.\nConsider growing indoors or in a greenhouse."
    },
    "spring":{
        "flower": "Prep your soil with compost.\nWater deeply."
        "vegetable": "Make sure your plants get at least 6 to 8 hours of sunlight per day"
    }
    "autumn":{
        "flower": "Prune dead and living plants./nApply a slow-release fertilizer."
        "vegetable": "Plant cool season vegetables./Ensure proper spacing." 
    }
}


def get_advice(season: str, plant_type: str) -> str:
    """Return gardening advice based on season and plant type."""
    season = season.lower()
    plant_type = plant_type.lower()

    if season in ADVICE and plant_type in ADVICE[season]:
        return ADVICE[season][plant_type]
    elif season not in ADVICE:
        return "No advice available for this season yet."
    else:
        return "No advice available for this type of plant yet."


def main():
    """Main program to interact with the user."""
    season = input("Enter the season (spring/summer/autumn/winter): ").strip()
    plant_type = input("Enter the plant type (flower/vegetable): ").strip()

    print("\n Gardening Advice ")
    print(get_advice(season, plant_type))


if __name__ == "__main__":
    main()
