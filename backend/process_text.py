from web_scrapping import extract_text_from_url

class ProcessedText:
    def __init__(self, url: str):
        self.extrected_text = extract_text_from_url(url)

    def update_extracted_text(self, url: str):
        self.extrected_text = extract_text_from_url(url)

def initialize_processed_text(url: str) -> ProcessedText:
    return ProcessedText(url)
