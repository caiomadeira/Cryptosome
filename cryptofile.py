from functionalities import Functionalities

class MainApplication(Functionalities):

    def __init__(self):
        self.key = int(input("Escreva uma chave de 1 á 255:"))
        self.filename = input("Digite o nome do arquivo:")
        self.remove_extension(filename=self.filename)
        #self.encrypt_file(filename=self.filename, key=self.key)
        self.decrypt_file(filename=self.filename, key=self.key)


if __name__ == '__main__':
    MainApplication()
