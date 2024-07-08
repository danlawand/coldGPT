from web_scrapping import extract_text_from_url
from vectordb import Memory

class ProcessedText:
    def __init__(self, url: str):
        self.extracted_text = extract_text_from_url(url)

    def update_extracted_text(self, url: str):
        self.extrected_text = extract_text_from_url(url)

    def memorize_text(self):
        self.memory = Memory()
        memory.save(
        ["apples are green", "oranges are orange"],  # save your text content. for long text we will automatically chunk it
        [{"url": "https://apples.com"}, {"url": "https://oranges.com"}], # associate any kind of metadata with it (optional)
        )

    def query_answer(self, query: str):
        print("--query--")
        return self.memory.search(query, top_n = 1)

def initialize_processed_text(url: str) -> ProcessedText:
    return ProcessedText(url)
