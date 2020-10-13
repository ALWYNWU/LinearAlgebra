from PlayLinearAlgebra.Vector import Vector

if __name__ == "__main__":

    vec = Vector([5, 2])
    print(vec)
    print(len(vec))
    print("vec[0] = {}".format(vec[0]))

    vec2 = Vector([4, 6])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} + {} = {}".format(vec, vec2, vec - vec2))

    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(3, vec, 3 * vec))

    print("-{} = {}".format(vec, -vec))

    zero_2 = Vector.zero(2)
    print(zero_2)

    print("normalize {} is {}".format(vec, vec.normalize()))
    try:
        zero_2.normalize()
    except ZeroDivisionError:
        print("Cannot normalize zero vector {}".format(zero_2))

    print(vec.dot(vec2))

    print(vec.projection_coordinate(vec2))