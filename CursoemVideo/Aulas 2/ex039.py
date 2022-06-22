from datetime import date

user_data = input('Digite sua data de nascimente ex(01/01/2000): ').strip()
user_data = user_data.split('/')
user_data = list(map(int, user_data))
user_year = user_data[2]
# user_year = int(user_year)
user_month = user_data[1]
# user_month = int(user_data)
user_day = user_data[0]
# user_day = int(user_data)

# def calculateAge(birthDate):
#     today = date.today()
#     age = today.year - birthDate.year
#     ((today.month, today.day) <
#     (birthDate.month, birthDate.day))
#
#     return age
#
# # age_1 = calculateAge(date(user_year, user_month, user_day))
# print(age_1)

def calculate_data(years):
    today = date.today()
    age = today.year - years.year
    if today.month > user_month:
        pass
    elif years:
        age - 1
    return age

idade = calculate_data(date(user_year, user_month, user_day))

print(idade)