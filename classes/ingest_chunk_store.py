import nltk
nltk.download('punk')

class TextModifier:
    def split_paragraphs(self, text: str) -> list[str]:
        return [p.strip() for p in text.split("\n\n") if p.strip()]

    def split_sentences(self, paragraph: str) -> list[str]:
        return nltk.sent_tokenize(paragraph)

    def chunk_text(self, file_path: str) -> list[dict]:
        """
        Function to ingest a text and return a list of objects, with each object containing a paragraph number and a tuple of ordered sentences.
        """
        text_structure = []

        with open(file_path, 'r') as file:
            file_contents = file.read()


        for i, paragraph in enumerate(self.split_paragraphs(file_contents)):
            sentences = self.split_sentences(paragraph)
            text_structure.append({
                "ID": i,
                "SENTENCES": sentences
            })

        return text_structure