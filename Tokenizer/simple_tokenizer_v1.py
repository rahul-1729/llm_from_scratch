import re
class simple_tokenizer_v1:
    def __init__(self,vocab):
        self.str_to_int = vocab #{"a":1,"b":2,...}
        self.int_to_str = {integer:string for string,integer in vocab.items()}  #{"1":a,"2":b,...}
    
    def encode(self,sentence):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)',sentence)
        tokens = [ token.strip() for token in preprocessed if token.strip()]
        token_ids = [self.str_to_int[token] for token in tokens]
        return token_ids

    def decode(self,token_ids):
        sentence = " ".join([self.int_to_str(token_id) for token_id in token_ids])
        sentence = re.sub(r'\s+([,.?!"()\'])', r'\1',sentence) 
        return sentence
        