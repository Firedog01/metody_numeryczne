import util


if __name__ == '__main__':
    files = util.get_files()
    print(files)
    matrix = util.get_matrix(files[0])
    print(matrix)