import tiktoken 
tokenizer = tiktoken.get_encoding("gpt2")
encodings = tokenizer.encode("Afghanistan is near pakistan") # takes input in string and gives output as token_id in form of list
decoding = tokenizer.decode(encodings) # takes a list of token ids and return a sentence

print(encodings,"\n",decoding)