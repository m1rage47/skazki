from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

# 1. Создаем асинхронный движок
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# 2. Создаем фабрику сессий
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# 3. Базовый класс для всех будущих моделей
class Base(DeclarativeBase):
    pass

# 4. Зависимость для получения сессии в эндпоинтах
async def get_async_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session