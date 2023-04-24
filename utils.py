from tabulate import tabulate

def printPretty(tokens, path, delim):
    table = []
    table.append(['token', 'type', 'row', 'column', 'block'])
    for token in tokens:
        if not delim:
            if 'SYMBOL' in token[1]:
                continue
        temp = [token[0], token[1], token[3], token[2], token[4]]
        table.append(temp)
    txt = tabulate(table, headers=("firstrow"), tablefmt="grid")
    with open(path, 'w') as file:
        file.write(txt)

def writeTxt(tokens, path, delim):
    with open(path, 'w') as file:
        for token in tokens:
            if not delim:
                if 'SYMBOL' in token[1]:
                    continue
            file.write(f'{token[0]}, {token[1]}, {token[3]}, {token[2]}, {token[4]}\n')
