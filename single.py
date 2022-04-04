from util import orchestrator as orch
import time

def method():
    print('Однопоточность.')

    timer = time.time()
    orch.shoot_multiple()

    print('Затраченное время: %.6f сек' % (time.time() - timer))