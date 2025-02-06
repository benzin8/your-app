import shutil
import subprocess

def check_disk_memory():
    disk = shutil.disk_usage('/')
    return(
        f"Cвободное место: {disk.free / (2**30):.2f} GB\n"
        f"Всего места: {disk.total / (2**30):.2f} GB"
    )

def check_system_file():
        result = subprocess.run(["fsck", "-n", "/"], capture_output=True, text=True)
        if "clean" in result.stdout:
            return "Файловая система в порядке \n"
        else:
            return "Файловая система нарушена \n"
        
def disk_test():
     return f"{check_disk_memory()} \n {check_system_file()}"

