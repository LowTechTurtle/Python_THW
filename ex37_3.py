##
class FileReader:
    def __init__(self, file, mode):
        self.file = file
        self.mode = mode
    def __enter__(banana):
        banana.fileobj = open(banana.file, banana.mode)
        return banana.fileobj
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fileobj.close()


filename = input('File you need to open and read/append: ')
mode = input('What mode file should be opened? ')
with FileReader(filename, mode) as fileobj:
    try:
        file_content = fileobj.read()
        fileobj.write('coding is dope')
    except:
        fileobj.write('Coding is dope')
print('File is closed: ',fileobj.closed)
print('Operation compeleted')

