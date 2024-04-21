import random
import requests
from django.conf import settings



def send_otp_to_phone(phone_number):
    try:
        otp = random.randint(1000, 9999)
        # вопрос нужно разобрать (7:40) https://www.youtube.com/watch?v=yjBIBDk81dg&t=12s
        url = f'https://smsc.ru/sys/send.php?login=<login>&psw=<password>&phones=<phones>&mes=<message>'
        response = requests.get(url)
        return otp
    except Exception as e:
        return None

