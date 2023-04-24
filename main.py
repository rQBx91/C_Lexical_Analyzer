from lexer import CLexer
import utils
import gui
import os
from sys import platform

def Main():

# File and script path for windows platform
    if platform == "win64" or platform == "win32":
        script_dir = os.path.dirname(__file__) # get script execution path
        inPath  = f'{script_dir}\\resources\\input.c'  # absolute file path for input file 
        txtPath = f'{script_dir}\\resources\\output.txt' # absolute file path for text file
        prettytxtPath = f'{script_dir}\\resources\\output-pretty.txt' # absolute file path for formatted text file

# File and script path for GNU/Linux palatform
    if platform == "linux" or platform == "linux2": # check for platform
        script_dir = os.getcwd() # get script execution path
        inPath  = f'{script_dir}/resources/input.c'  # absolute file path for input file 
        txtPath = f'{script_dir}/resources/output.txt' # absolute file path for text file
        prettytxtPath = f'{script_dir}/resources/output-pretty.txt' # absolute file path for formatted text file


    lines = []
    with open(inPath) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    lexed = []
    lexer = CLexer()
    for line in lines:
        lexed.append(lexer.tokenize(line))

    allTokens = []
    for index, line in enumerate(lexed):
        for tuple in line:
            allTokens.append(tuple+(index+1,))

    skip = False
    block = 0
    tokens = []
    for token in allTokens:
        if token[1] == 'SYMBOL_LCB':
            if not skip:
                tokens.append(token+(block,))
            block += 1
            continue

        if token[1] == 'SYMBOL_RCB':
            block -= 1
            if not skip:
                tokens.append(token+(block,))
            continue

        if token[1] == 'MULTILINE_COMMENT_START':
            tokens.append(token+(block,))
            skip = True
            continue

        if token[1] == 'MULTILINE_COMMENT_END':
            tokens.append(token+(block,))
            skip = False
            continue

        if skip:
            continue

        tokens.append(token+(block,))

    utils.writeTxt(tokens, txtPath, True)
    utils.printPretty(tokens, prettytxtPath , True)
    gui.run(tokens, True)


if __name__ == "__main__":
    Main()