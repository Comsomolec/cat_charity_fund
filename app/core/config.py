from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    # Не проходит тесты на платформе без умолчательных значений
    app_title: str = 'QR_Kot'
    app_description: str = 'Приложение для Благотворительного фонда'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
