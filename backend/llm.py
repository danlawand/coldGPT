from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class LLMModel:
    def __init__(self):
        self.model_name = 'gpt2'
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name)
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
        self.tokenizer.add_special_tokens({'pad_token': '[PAD]'})

    def generate_answer(self, source_text, question):
        input_text = f"Source text: {source_text}\n\nQuestion: {question}\nAnswer:"
        inputs = self.tokenizer(input_text, return_tensors='pt', padding=True)

        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']

        output = self.model.generate(
            input_ids, 
            attention_mask=attention_mask, 
            max_length=150, 
            num_return_sequences=1, 
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        answer = self.tokenizer.decode(output[0], skip_special_tokens=True)
        answer_start = answer.find("Answer:") + len("Answer:")
        return answer[answer_start:].strip()


    # def generate_answer(self, source_text, question):
    #     input_text = f"Source text: {source_text}\n\nQuestion: {question}\nAnswer:"
    #     inputs = self.tokenizer.encode(input_text, return_tensors='pt', padding=True)
        
    #     input_ids = inputs['input_ids']
    #     attention_mask = inputs['attention_mask']

    #     output = self.model.generate(
    #         input_ids, 
    #         attention_mask=attention_mask, 
    #         max_length=500, 
    #         num_return_sequences=1, 
    #         pad_token_id=self.tokenizer.eos_token_id
    #     )

    #     answer = self.tokenizer.decode(output[0], skip_special_tokens=True)

    #     answer_start = answer.find("Answer:") + len("Answer:")
    #     return answer[answer_start:].strip()


def initialize_llm_model():
    return LLMModel()
