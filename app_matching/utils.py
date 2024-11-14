# utils.py or matching_utils.py

def calculate_match_score(user_profile, user_preference):
    score = 0
    total_weight = 0
    
    # Compare Gender (Single Value)
    if user_profile.Gender == user_preference.Gender:
        score += 10
    total_weight += 10

    # Compare Age (Range)
    if user_profile.Age >= user_preference.Age[0] and user_profile.Age <= user_preference.Age[1]:
        score += 20
    total_weight += 20

    # Compare Height (Range)
    if user_profile.Height >= user_preference.Height[0] and user_profile.Height <= user_preference.Height[1]:
        score += 15
    total_weight += 15

    # Compare Weight (Range)
    if user_profile.Weight >= user_preference.Weight[0] and user_profile.Weight <= user_preference.Weight[1]:
        score += 10
    total_weight += 10

    # Compare Income (Range)
    if user_profile.Income >= user_preference.Income[0] and user_profile.Income <= user_preference.Income[1]:
        score += 15
    total_weight += 15

    # Compare Religion (Single Value)
    if user_profile.Religion == user_preference.Religion:
        score += 5
    total_weight += 5

    # Compare Caste (Single Value)
    if user_profile.Caste == user_preference.Caste:
        score += 5
    total_weight += 5

    # Compare Profession (Multi-Value)
    if user_profile.Profession in user_preference.Profession:
        score += 10
    total_weight += 10

    # Compare Education (Multi-Value)
    if user_profile.Education in user_preference.Education:
        score += 10
    total_weight += 10

    # Compare Location (Multi-Value)
    if user_profile.Location in user_preference.Location:
        score += 10
    total_weight += 10

    # Compare Language (Multi-Value)
    if user_profile.Language in user_preference.Language:
        score += 5
    total_weight += 5

    # Compare Marital Status (Single Value)
    if user_profile.Marital_status == user_preference.Marital_status:
        score += 5
    total_weight += 5

    # Calculate match percentage
    match_percentage = (score / total_weight) * 100 if total_weight > 0 else 0

    return match_percentage
