import util
from jordan import jordan


def user_input():
    files = util.get_files()
    for idx, file in enumerate(files):
        print(idx, file)
    chosen_idx = input("enter number of chosen file: ")
    return util.get_matrices(files[int(chosen_idx)])


# TODO: list zamiast np.array
if __name__ == '__main__':
    A, b = user_input()
    A = A.tolist()
    b = b.tolist()
    for i in range(0, len(b)):
        b[i] = b[i][0]
    print("A:", A)
    print("b:", b)
    x = jordan(A, b)
    print("x:", x)

