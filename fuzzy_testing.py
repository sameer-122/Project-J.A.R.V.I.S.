from fuzzywuzzy import fuzz

def fuzzymatch(query, desired_phrase):
    q = query
    ln= len(desired_phrase)
    max_ratio=0
    for i in range(len(q)):
        if i+ln > len(q) and i!=0 : 
            print(f'max match : {max_ratio}')
            return False
        phrase= q[i:i+ln]
        similarity_ratio = fuzz.ratio(desired_phrase,phrase)
        max_ratio = max(max_ratio, similarity_ratio)
        if similarity_ratio > 55:
            print(f'fuzmatch: {similarity_ratio}')
            return True


if __name__ == '__main__' :
    query = 'javascript'
    phrase = 'jarvis quit'
    if fuzzymatch(query,'jarvis quit') :
        print('exitting')
        exit()