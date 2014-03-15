# returns the sign on 'day' : 'month' in the tropical zodiac
def what_is_my_sign(day, month):
    # 'signs[month]' is the sign which has it's beginning in 'month'
    # (0 - december, 1 - january, ..., 12 - december)
    signs = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus",
            "Gemini", "Cancer", "Leo", "Virgo",
            "Libra", "Scorpio", "Sagittarius", "Capricorn"]

    # the day on which the sign changes in a month
    # (0 - december, 1 - january, ..., 12 - december)
    sign_change = [22, 21, 20, 21, 21, 22, 22, 23, 23, 24, 24, 23, 22]

    if day >= sign_change[month]:
        return signs[month]
    else:
        return signs[month - 1]