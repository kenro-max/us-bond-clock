# US Bond Clock

import datetime

# Get current UTC date and time
current_time = datetime.datetime.utcnow()
formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

print(f'Current Date and Time (UTC - YYYY-MM-DD HH:MM:SS formatted): {formatted_time}')