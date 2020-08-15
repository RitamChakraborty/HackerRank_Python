import numpy as np

if __name__ == '__main__':
    array = np.array(list(map(float, input().split())))
    np.set_printoptions(sign=" ")
    print(np.floor(array))
    print(np.ceil(array))
    print(np.rint(array))
