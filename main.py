from aiogram.utils import executor

from src.tg_funcs import dp

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
