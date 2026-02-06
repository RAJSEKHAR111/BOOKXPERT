# Task 1: Get Matching Person Names
# Objective:
# Build a name-matching system that finds the most similar names from a dataset when a user
# inputs a name.
# Key Steps:
# • Data Preparation: Store similar names (like Geetha, Gita, Gitu, etc.) in a list, take at
# least 30 names.
# • Similarity Matching: When a user enters a name, find the most similar name(s) using
# any library, Vector DB Search or anything, that is your choice.
# Expected Output:
# • Best Match: The closest matching name with a similarity score.
# • List of Matches: A ranked list of other similar names with scores.


from rapidfuzz import process, fuzz

# 1. Data Preparation: List of 30+ similar names [cite: 6]
dataset_names = [
    "Rajsekhar", "Raj", "Sekhar", "Rajshekar", "Rajesh",
    "Geetha", "Gita", "Gitu", "Geeta", "Jeeta",
    "Krishna", "Krisna", "Krish", "Kistna", "Christna",
    "Mohammed", "Mohamed", "Mohammad", "Muhammed", "Mamadu",
    "Alexander", "Alex", "Xander", "Aleksander", "Alyx",
    "Elizabeth", "Eliza", "Beth", "Liz", "Elisabeth",
    "Srinivas", "Vasu", "Srinu", "Shrinivas", "Vasudev"
]

def find_best_matches(input_name, limit=5):
    """
    Finds the most similar names using Weighted Ratio matching.
    Returns: Best Match and a List of Matches with scores.
    """
    # [cite: 7] Similarity Matching
    results = process.extract(
        input_name, 
        dataset_names, 
        scorer=fuzz.WRatio, 
        limit=limit
    )
    
    # Formatting output for clarity
    formatted_results = [{"name": name, "score": score} for name, score, index in results]
    
    return {
        "best_match": formatted_results[0] if formatted_results else None, # [cite: 9]
        "all_matches": formatted_results # [cite: 10]
    }

# Simple CLI test
if __name__ == "__main__":
    user_input = input("Enter a name to search: ")
    match_data = find_best_matches(user_input)
    print(f"\nBest Match: {match_data['best_match']}")
    print("Top 5 Matches:")
    for m in match_data['all_matches']:
        print(f"- {m['name']} (Score: {m['score']:.2f})")