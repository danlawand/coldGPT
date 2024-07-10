from web_scrapping import extract_text_from_url
from vectordb import Memory

class ProcessedText:
    def __init__(self, url: str):
        self.extracted_text = extract_text_from_url(url)
        self.memory = Memory(chunking_strategy={'mode':'sliding_window', 'window_size': 128, 'overlap': 16})
        metadata = {"title": "Introdução a Hotmart", "url": f"{url}"}
        self.memory.save(self.extracted_text, metadata)

    def update_extracted_text(self, url: str):
        self.extrected_text = extract_text_from_url(url)

    def query_answer(self, text: str):
        query_response = self.memory.search(text, top_n = 3)
        
        if len(query_response) <= 0:
            return """ Not found information that might help you."""

        return query_response[0]["chunk"]

def initialize_processed_text(url: str) -> ProcessedText:
    return ProcessedText(url)

