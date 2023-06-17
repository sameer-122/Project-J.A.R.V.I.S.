from fuzzywuzzy import fuzz

def fuzzmatch(desired_phrase, query, cutoff_ratio=60):
    q = query
    ln= len(desired_phrase)
    max_ratio=0
    for i in range(len(q)):
        if i+ln > len(q) and i!=0 : 
            print(f'fuzmatch failed : {max_ratio}')
            return False
        phrase= q[i:i+ln]
        similarity_ratio = fuzz.ratio(desired_phrase,phrase)
        max_ratio = max(max_ratio, similarity_ratio)
        if similarity_ratio > cutoff_ratio:
            print(f'fuzmatch passed: {similarity_ratio}')
            return True


if __name__ == '__main__' :
    query = 'using Iw'
    query.lower()
    phrase = 'using a i'
    if 'using a i' in query or fuzzmatch('using a i',query,cutoff_ratio=75) :
        print('exitting')
        exit()