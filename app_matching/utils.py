def calculate_match_score(user1_preference, user2_profile):
    
    
    if user1_preference.Gender != user2_profile.Gender:
        return 0 
    
    score = 0
    total_weight = 0
    
    # Compare Gender (Single Value)
    if user2_profile.Gender == user1_preference.Gender:
        score += 10
    else:
        score -= 10  # Deduct points if they don't match
    total_weight += 10

    # Compare Age (Range)
    if user2_profile.Age >= user1_preference.Age[0] and user2_profile.Age <= user1_preference.Age[1]:
        score += 20
    else:
        score -= 10  # Deduct points if they don't match
    total_weight += 20

    # Compare Height (Range)
    if user2_profile.Height >= user1_preference.Height[0] and user2_profile.Height <= user1_preference.Height[1]:
        score += 15
    else:
        score -= 7  # Deduct points if they don't match
    total_weight += 15

    # Compare Weight (Range)
    if user2_profile.Weight >= user1_preference.Weight[0] and user2_profile.Weight <= user1_preference.Weight[1]:
        score += 10
    else:
        score -= 5  # Deduct points if they don't match
    total_weight += 10

    # Compare Income (Range)
    if user2_profile.Income >= user1_preference.Income[0] and user2_profile.Income <= user1_preference.Income[1]:
        score += 15
    else:
        score -= 7  # Deduct points if they don't match
    total_weight += 15

    # Compare Religion (Single Value)
    if user2_profile.Religion == user1_preference.Religion:
        score += 5
    else:
        score -= 2  # Deduct points if they don't match
    total_weight += 5

    # Compare Caste (Single Value)
    if user2_profile.Caste == user1_preference.Caste:
        score += 5
    else:
        score -= 2  # Deduct points if they don't match
    total_weight += 5

    # Compare Profession (Multi-Value)
    if user2_profile.Profession in user1_preference.Profession:
        score += 10
    else:
        score -= 5  # Deduct points if they don't match
    total_weight += 10

    # Compare Education (Multi-Value)
    if user2_profile.Education in user1_preference.Education:
        score += 10
    else:
        score -= 5  # Deduct points if they don't match
    total_weight += 10

    # Compare Location (Multi-Value)
    if user2_profile.Location in user1_preference.Location:
        score += 10
    else:
        score -= 5  # Deduct points if they don't match
    total_weight += 10

    # Compare Language (Multi-Value)
    if user2_profile.Language in user1_preference.Language:
        score += 5
    else:
        score -= 2  # Deduct points if they don't match
    total_weight += 5

    # Compare Marital Status (Single Value)
    if user2_profile.Marital_status == user1_preference.Marital_status:
        score += 5
    else:
        score -= 2  # Deduct points if they don't match
    total_weight += 5

    # Calculate match percentage
    match_percentage = (score / total_weight) * 100 if total_weight > 0 else 0

    return match_percentage
