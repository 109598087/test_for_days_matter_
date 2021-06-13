import datetime

today = datetime.datetime.today()
target_date = today - datetime.timedelta(397)  # 397天之前
target_date_str = target_date.strftime("%Y-%m-%d")
target_date_list = target_date_str.split('-')
countdown_day_target_year = target_date_list[0]
countdown_day_target_month = target_date_list[1]
countdown_day_target_day = target_date_list[2]

print(countdown_day_target_year)
print(countdown_day_target_month)
print(countdown_day_target_day)
