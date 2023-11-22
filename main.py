from aiogram.utils import executor

from tg_funcs import dp

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
