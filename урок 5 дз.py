import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # начало измерения

        result = func(*args, **kwargs)

        end = time.perf_counter()  # конец измерения
        print(f"Функция {func.__name__} работала {end - start:.2f} секунды")

        return result

    return wrapper


@timer
def calculate_sum(n):
    return sum(range(n))


result = calculate_sum(1_000_000)
print(result)


#доп задание
import time
import asyncio


def async_timer(func):
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = await func(*args, **kwargs)

        end = time.perf_counter()
        print(f"Функция {func.__name__} работала {end - start:.2f} секунды")

        return result

    return wrapper


@async_timer
async def download_data():
    await asyncio.sleep(2)
    return "Данные загружены"


async def main():
    result = await download_data()
    print(result)


asyncio.run(main())