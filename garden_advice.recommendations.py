
"""Provides plant recommendations based on the season."""

# Plant recommendations stored in a dictionary
PLANT_RECOMMENDATIONS = {
    "spring": ["Lettuce", "Spinach", "Tulips"],
    "summer": ["Tomatoes", "Sunflowers", "Basil"],
    "autumn": ["Carrots", "Kale", "Chrysanthemums"],
    "winter": ["Garlic", "Onions", "Poinsettias"]
}


def recommend_plants(season: str) -> str:
    """Return a list of plants recommended for the given season."""
    season = season.lower()
    if season in PLANT_RECOMMENDATIONS:
        plants = ", ".join(PLANT_RECOMMENDATIONS[season])
        return f"Recommended plants for {season.capitalize()}: {plants}"
    else:
        return "No recommendations available for this season yet."


def main():
    """Main program to interact with the user."""
    season = input("Enter the season (spring/summer/autumn/winter): ").strip()

    print("\n Plant Recommendations ")
    print(recommend_plants(season))


if __name__ == "__main__":
    main()
