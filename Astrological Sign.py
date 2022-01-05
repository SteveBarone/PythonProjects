# Python program to display astrological sign or Zodiac sign for a DOB
def zodiac_sign(day,month):
    # checks month and date within the valid range of a specified zodiac
    if month == 'December':
        astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'

    elif month == 'January':
        astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'

    elif month == 'February':
        astro_sign = 'Aquarius' if (day < 19) else 'Pisces'

    elif month == 'March':
        astro_sign = 'Pisces' if (day < 21) else 'Aries'

    elif month == 'April':
        astro_sign = 'Aries' if (day < 20) else 'Taurus'

    elif month == 'May':
        astro_sign = 'Taurus' if (day < 21) else 'Gemini'

    elif month == 'June':
        astro_sign = 'Gemini' if (day < 21) else 'Cancer'

    elif month == 'July':
        astro_sign = 'Cancer' if (day < 23) else 'Leo'

    elif month == 'August':
        astro_sign = 'Leo' if (day < 23) else 'Virgo'

    elif month == 'September':
        astro_sign = 'Virgo' if (day < 23) else 'Libra'

    elif month == 'October':
        astro_sign = 'Libra' if (day < 23) else 'Scorpio'

    elif month == 'November':
        astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'

    print(astro_sign)

# Driver code
if __name__ == '__main__':
    day = 21
    month = "July"
    zodiac_sign(day, month)