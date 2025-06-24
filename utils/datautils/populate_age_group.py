from datetime import datetime


def populate_age_group(dob_str):
    birth_year = int(str(dob_str).split("/")[2])
    birth_month = int(str(dob_str).split("/")[0])
    birth_day = int(str(dob_str).split("/")[1])
    today = datetime.today()
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))

    if age < 25:
        return "18-24"
    elif age < 35:
        return "25-34"
    elif age < 55:
        return "35-54"
    else:
        return "55+"