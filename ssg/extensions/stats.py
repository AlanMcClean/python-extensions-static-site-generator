from sqlite3 import Time
import time

from ssg import hooks

start_time = None
total_written = 0

@hooks.register("start_build")
def start_build():
    global start_time
    start_time = Time()


@hooks.register("start_build")
def written():
    global total_written
    total_written = total_written + 1

@hooks.register("stats")
def stats():
    final_time = Time() - start_time 
    average = final_time / total_written if total_written != 0 else 0
    report = "Converted: {} · Time: {:.2f} sec · Avg: {:.4f} sec/file"
    print(report.format(total_written,final_time,average))

