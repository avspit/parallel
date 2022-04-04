import multi as mlt
import single as sgl

if __name__ == '__main__':
    # Без распараллеливания
    sgl.method()
    # Параллельное вычисление. Метод 1, с помощью multithreading
    mlt.multithreading()
    # Параллельное вычисление. Метод 2, с помощью multiprocessing
    mlt.multiprocessing()

