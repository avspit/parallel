from util import orchestrator as orch
import time


def multithreading():
    print('Многопоточность с помощью multithreading.')

    timer = time.time()
    orch.shoot_multithreading()

    print('Затраченное время: %.6f сек' % (time.time() - timer))


def multiprocessing():
    print('Многопоточность с помощью multiprocessing.')

    timer = time.time()
    orch.shoot_multiprocessing()

    print('Затраченное время: %.6f сек' % (time.time() - timer))