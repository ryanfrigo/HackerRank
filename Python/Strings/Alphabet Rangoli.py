def print_rangoli(size):
    az = 'abcdefghijklmnopqrstuvwxyz'

    id = size
    row_id = []
    while id > 0:
        id -= 1
        row_id.append(id)
    while id < size - 1:
        id += 1
        row_id.append(id)

    for i in row_id:
        letters = az[i:size][::-1] + az[i:size][1:]
        row = '-'.join(letters).center(4*size-3, '-')
        print(row)

