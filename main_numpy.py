import numpy as np

if __name__ == "__main__":

    print(np.__version__)

    vec = np.array([1, 2, 3])
    # print(vec)

    # numpy的创建
    print(np.zeros(5))
    print(np.ones(5))
    print(np.full(5, 666))

    # numpy的基本属性
    print("size =", vec.size)
    print("size =", len(vec))
    print(vec[0])
    print(vec[-1])
    print(vec[0: 2])
    print(type(vec[0: 2]))

    # numpy的基本运算
    vec2 = np.array([4, 5, 6])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} * {} = {}".format(2, vec, 2 * vec))
    print("{} * {} = {}".format(vec, vec2, vec * vec2))
    print("{}.dot({}) = {}".format(vec, vec2, vec.dot(vec2)))

    print(np.linalg.norm(vec))
    print(vec / np.linalg.norm(vec))

