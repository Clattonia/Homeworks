def all_variants(text):
    n = len(text)
    
    for start in range(n):
        
        for end in range(start + 1, n + 1):
            yield text[start:end]


a = all_variants("abc")
for i in a:
    print(i)
