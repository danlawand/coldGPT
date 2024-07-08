from web_scrapping import extract_text_from_url
from vectordb import Memory

class ProcessedText:
    def __init__(self, url: str):
        self.extracted_text = extract_text_from_url(url)
        self.memory = Memory()

    def update_extracted_text(self, url: str):
        self.extrected_text = extract_text_from_url(url)

    def memorize_text(self):
        self.memory.save(["apples are green", "oranges are orange"])

    def query_answer(self, text: str):
        query_response = self.memory.search(text, top_n = 1)
        return  str(query_response)

def initialize_processed_text(url: str) -> ProcessedText:
    return ProcessedText(url)
