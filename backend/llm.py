from transformers import GPT2LMHeadModel, GPT2Tokenizer, AutoTokenizer, AutoModelForCausalLM
import torch

class LLMModel:
    def __init__(self):

        model_name = "neuralmind/bert-base-portuguese-cased"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.tokenizer.model_max_length=1024 
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

        self.tokenizer2 = AutoTokenizer.from_pretrained("pierreguillou/gpt2-small-portuguese")
        self.model2 = AutoModelForCausalLM.from_pretrained("pierreguillou/gpt2-small-portuguese")
        self.tokenizer2.add_special_tokens({'pad_token': '[PAD]'})
        # Get sequence length max of 1024
        self.tokenizer2.model_max_length=1024 


    def generate_answer(self, context):
        input_ids = self.tokenizer.encode(context, return_tensors='pt')
        output = self.model.generate(input_ids, max_length=500, num_return_sequences=1, no_repeat_ngram_size=2)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

    def generate_2nd(self, context):
        inputs = self.tokenizer2(context, return_tensors="pt")
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']
        sample_outputs = self.model2.generate(
            input_ids,  
            attention_mask=attention_mask, 
            top_k=40,
            max_length=500, 
            num_return_sequences=1, 
            pad_token_id=self.tokenizer2.eos_token_id
        )
        return sample_outputs

#     def __init__(self):
#         self.model_name = 'gpt2'
#         self.model = GPT2LMHeadModel.from_pretrained(self.model_name)
#         self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
#         self.tokenizer.add_special_tokens({'pad_token': '[PAD]'})

#     def generate_answer(self, source_text, question):
#         input_text = f"Source text: {source_text}\n\nQuestion: {question}\nAnswer:"
#         inputs = tokenizer(input_text, return_tensors='pt', padding=True)

#         input_ids = inputs['input_ids']
#         attention_mask = inputs['attention_mask']

#         # Generate the output
#         output = model.generate(
#             input_ids, 
#             attention_mask=attention_mask, 
#             max_length=500, 
#             num_return_sequences=1, 
#             pad_token_id=tokenizer.eos_token_id
#         )
        
#         answer = tokenizer.decode(output[0], skip_special_tokens=True)
#         answer_start = answer.find("Answer:") + len("Answer:")
#         return answer[answer_start:].strip()



def initialize_llm_model():
    return LLMModel()
