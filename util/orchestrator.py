from constants import variables as conts
import threading
import multiprocessing
import numpy as np
import shoot as sh


def shoot_multiple():
    '''
    Однопоточный запуск метода в цикле N раз
    '''
    for i in np.arange(conts.ALFAS_INCREMENT, conts.ALFAS_COUNT, conts.ALFAS_INCREMENT):
        sh.shoot_func(i)


def shoot_multithreading():
    '''
    Запуск метода, используя multithreading
    '''
    processes = []
    for i in np.arange(conts.ALFAS_INCREMENT, conts.ALFAS_COUNT, conts.ALFAS_INCREMENT):
        t = threading.Thread(target=sh.shoot_func, args=(i,))
        processes.append(t)

    for t in processes:
        t.start()
        t.join()

    processes.clear()


def shoot_multiprocessing():
    '''
    Запуск метода, используя multiprocessing
    '''
    pool = multiprocessing.Pool(processes=7)
    pool.map(sh.shoot_func, np.arange(conts.ALFAS_INCREMENT, conts.ALFAS_COUNT, conts.ALFAS_INCREMENT))
    pool.terminate()