import re
refrence_text = "../assets/the-verdict.txt"

# to get token_id from tokens and vice-versa
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
        sentence = " ".join([self.int_to_str[token_id] for token_id in token_ids])
        sentence = re.sub(r'\s+([,.?!"()\'])', r'\1',sentence) 
        return sentence

# To create a refrence vocab   
class vocab_list:
    def __init__(self,refrence_text):
        with open(refrence_text,"r") as f:
            self.sample_text = f.read()
    def generate_vocab(self):
        tokens = re.split(r'([,.:;?_!"()\']|--|\s)', self.sample_text)
        tokens = [token.strip() for token in tokens if token.strip()]
        tokens.extend(["<|endoftext|>","<|unk|>"]) #to handle end of text and unknown words
        tokens = {token:index for index,token in enumerate(tokens)}
        return tokens
            
        
vocab = vocab_list(refrence_text)
refrence_vocab = vocab.generate_vocab()
tokenizer = simple_tokenizer_v1(refrence_vocab)
# print(len(refrence_vocab))
token_id_list = tokenizer.encode("let her go")
# print(len(token_id_list))
generated_sentence = tokenizer.decode(token_id_list)
# print(generated_sentence)

# Note: If you write a text other thanpresent in the story it will give keyerror, vocab doen't contain all the words