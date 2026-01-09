# Last updated: 2026-01-09 17:48:57

import datetimedef get_current_time():    now = datetime.datetime.now()    print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")    return nowif __name__ == "__main__":    get_current_time()
