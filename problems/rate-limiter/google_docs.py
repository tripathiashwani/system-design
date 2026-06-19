from abc import ABC, abstractmethod

class DocumentElement(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class TextElement(DocumentElement):
    def render(self,text) -> str:
        return text

class ImageElement(DocumentElement):
    def render(self, image_url) -> str:
        return f'<img src="{image_url}" alt="Image">'
    

class Document:
    elements = []

    def add_element(self, element: DocumentElement):
        self.elements.append(element)

    def render(self) -> str:
        rendered_content = [element.render() for element in self.elements]
        return "\n".join(rendered_content)


class Persistanece(ABC):
    @abstractmethod
    def save(self, document: Document, filename: str):
        pass


class FilePersistence(Persistanece):
    def save(self, document: Document, filename: str):
        with open(filename, 'w') as file:
            file.write(document.render())

class DatabasePersistence(Persistanece):
    def save(self, document: Document, filename: str):
        # Simulate saving to a database
        print(f"Document saved to database with name: {filename}")

class GoogleDocs:
    
    def __init__(self, persistence: Persistanece):
        self.document = Document()
        self.persistence = persistence

    def add_text(self, text: str):
        text_element = TextElement()
        self.document.add_element(text_element) 
        text_element.render(text)

    def add_image(self, image_url: str):
        image_element = ImageElement()
        self.document.add_element(image_element)
        image_element.render(image_url)

    def save_document(self, filename: str):
        self.persistence.save(self.document, filename)

    def render_document(self) -> str:
        return self.document.render() 