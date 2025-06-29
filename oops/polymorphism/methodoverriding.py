#runtime polymorphism
# Method overriding is a feature that allows a subclass to provide a specific implementation of a method that
# is already defined in its superclass. This is a key aspect of runtime polymorphism in object-oriented programming.

class FileProcessor:
    def process(self):
        print("Opening file")

class CsvProcessor(FileProcessor):
    def process(self):
        super().process()
        print("Processing CSV data")

processor = CsvProcessor()
processor.process()
