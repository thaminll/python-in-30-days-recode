from datetime import datetime, date

now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
sec = now.second
secs = now.timestamp()
print(f'today is {year} {month} {day} {hour} {minute} {sec}')
print(f'{secs} seconds passed from 1970')

print(f' {now.strftime("%d %m %Y, %H %M %S")}')
print(f' {now.strftime("%m/%d/%Y, %H:%M:%S")}')

#Today is 5 December, 2019. Change this time string to time
today = datetime.strptime("5 December, 2019", '%d %B, %Y')
print(today)

today = date(now.year, now.month, now.day)
new_year = date(2023, 1, 1)
sub = new_year - today
print(sub)

past = datetime.strptime(" 1 January 1970", "%d %B %Y")
pastt = date(past.year, past.month, past.day)
time = today - pastt
print(time)

# Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog