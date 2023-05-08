class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'w')

    def log(self, message):
        print(message)
        self.file.write(message + '\n')

    def close(self):
        self.file.close()
