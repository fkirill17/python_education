# В файле, где нужно забрать данные из .env
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


TOKEN = os.getenv('TOKEN')  # Токен телеграм-бота

# # В файле .env
#
# TOKEN=7106066621:AAG4ZG7ze3vc30rioiyfO0nCilRXiQyzYXU
# DATABASE_URL=



