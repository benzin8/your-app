import psutil

def check_cpu():
    usage = psutil.cpu_percent(interval=1)
    return f"CPU: {usage}"

def check_ram():
    memory = psutil.virtual_memory()
    return (
        f"RAM Использованно: {memory.used / (2 ** 30):.2f} GB \n"
        f"RAM Осталось: {memory.available / (2 ** 30):.2f} GB \n"
    )

def hardware_test():
    return f"{check_cpu()}\n{check_ram()}\n"