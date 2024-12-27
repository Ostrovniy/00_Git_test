""" 
МОСТ
Представьте, что у вас есть устройство, например пульт управления. Этот пульт может управлять разными устройствами: 
телевизором, радио, кондиционером и т.д. При этом пульт можно сделать универсальным, чтобы не привязывать его жестко к каждому типу устройства.

Абстракция — это ваш пульт. Он определяет основные действия, такие как включение, выключение, переключение каналов.
Реализация — это конкретные устройства, такие как телевизор или радио, которые могут быть включены, выключены или переключены.
Таким образом, пульт (абстракция) можно использовать с любым устройством (реализация), не меняя его код.
"""

from abc import ABC, abstractmethod

# Интерфейс для провайдера
class AOuthProvider(ABC):
    @abstractmethod
    def get_aunt_url(self):
        pass

    @abstractmethod
    def get_access_token(self, code: str):
        pass

# Реализация провайдеров (1)
class GoogleAOuth(AOuthProvider):
    def get_aunt_url(self):
        return 'https://accounts.google.com/o/oauth2/auth'
    
    def get_access_token(self, code):
        return f'Google access token for code {code}'
    
# Реализация провайдеров (2)
class TelegramAOnth(AOuthProvider):
    def get_aunt_url(self):
        return 'https://accounts.telegram.com/o/oauth2/auth'
    
    def get_access_token(self, code):
        return f'Telegram access token for code {code}'
    
# Интерфейс для клиента
class AOuthClient:
    def __init__(self, provider: AOuthProvider):
        self.provider = provider

    def authenticate(self):
        # Получения ссылки
        aouth_url = self.provider.get_aunt_url()
        print(f"aouth_url: {aouth_url}")

        code = '555'
        access_token = self.provider.get_access_token(code)
        print(f"access_token: {access_token}")


test = AOuthClient(GoogleAOuth())
test2 = AOuthClient(TelegramAOnth())

test.authenticate()
test2.authenticate()

"""
1. Создали интерфейс, это общие плавила для любой авторизации
2. Создаем авторизацию, гугл, телеграм и любые другие, на основе интерфейса, что бы все было под шаблон
3. Есть Класс для работы с авторизацией, мы уже манипулирует данными в не зависимости того через какую авторизацию работает
"""