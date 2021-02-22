"""
filetype dependency: https://github.com/h2non/filetype.py

"""
import filetype, os

file_open = 'mystery.mp3'


def check_ex():
    check_ex = filetype.guess(file_open)
    if check_ex is None:
        print('Não identifiquei a extensão!')
        return

    print('File extension: %s' % check_ex.extension)
    print('File MIME type: %s' % check_ex.mime)


def read():
    destiny_path = './'
    re = os.rename('test.txt', 'test.cry')




if __name__ == '__main__':
    read()
