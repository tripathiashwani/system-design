from abc import ABC, abstractmethod

class DocumentElement(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class TextElement(DocumentElement):

    def __init__(self, text: str):
        self.text = text

    def render(self) -> str:
        return self.text 

class ImageElement(DocumentElement):
    def __init__(self, image_url):
        self.image_url = image_url

    def render(self) -> str:
        return f'<img src="{self.image_url}" alt="Image">'




# ===============================
# Decorator Base
# ===============================
class TextDecorator(DocumentElement):
    def __init__(self, element: DocumentElement):
        self.element = element

    @abstractmethod
    def render(self) -> str:
        pass


# ===============================
# Concrete Decorators
# ===============================
class BoldText(TextDecorator):
    def render(self) -> str:
        return f"<b>{self.element.render()}</b>"



class ItalicText(TextDecorator):
    def render(self) -> str:
        return f"<i>{self.element.render()}</i>"
    

class UnderlineText(TextDecorator):
    def render(self) -> str:
        return f"<u>{self.element.render()}</u>"


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
        text_element = TextElement(text)

        styled_text = ItalicText(
                        BoldText(
                            UnderlineText(text_element)
                        )
                     )

        self.document.add_element(styled_text)

    def add_image(self, image_url: str):
        image_element = ImageElement(image_url)
        self.document.add_element(image_element)

    def save_document(self, filename: str):
        self.persistence.save(self.document, filename)

    def render_document(self) -> str:
        return self.document.render() 
    

if __name__ == "__main__":
    docs = GoogleDocs(FilePersistence())

    docs.add_text("Ashwani")
    docs.add_image("image.png")

    print(docs.render_document())