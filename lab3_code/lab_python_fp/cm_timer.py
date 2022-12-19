import time
from contextlib import contextmanager
class cm_timer_1:
    def __init__(self):
        self.t = 0
    def __enter__(self):
        self.t=time.time()
    def __exit__(self, exp_type, exp_value, traceback):
        print(f'''time: {time.time()-self.t}''')

@contextmanager
def cm_timer_2():
    t=time.time()
    yield
    print(f'''time: {time.time()-t}''')

if __name__=='__main__':
    with cm_timer_1():
        time.sleep(0.5)
    with cm_timer_2():
        time.sleep(0.5)
