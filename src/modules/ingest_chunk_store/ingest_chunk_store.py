import nltk
from pathlib import Path

nltk.download('punkt', quiet='true')

class IngestChunkStore:
    def split_paragraphs(self, text: str) -> list[str]:
        # Split text into paragraphs based on doubled new lines
        return [p.strip() for p in text.split("\n\n") if p.strip()]

    def split_sentences(self, paragraph: str) -> list[str]:
        # Split paragraphs into sentences
        return nltk.sent_tokenize(paragraph)

    def chunk_text(self, file_path: str) -> list[dict]:
        """
        Function to ingest a text and return a list of objects, with each object containing a paragraph number and a tuple of ordered sentences.
        """

        file_path = Path(file_path)
        if not file_path:
            raise FileNotFoundError(f"File not found at {file_path}")

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