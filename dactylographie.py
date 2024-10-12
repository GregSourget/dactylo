import random as rdm

#length of the final text
MIN = 5
MAX = 20

def open_file() :
    with open('D:\\Programmation\\python\\dactylo\\francais.txt', 'r') as f:
        content = f.read()
    return content

def generate_text(text): 
    length_final_text = int(rdm.randint(MIN,MAX))
    print(f'Longueur du texte généré : {length_final_text}')

    words_list = []
    words_list = text.split()
    rdm_word = rdm.choices(words_list, k=length_final_text)
    final_text =  ' '.join(str(_) for _ in rdm_word)
    print(final_text)


content_file = open_file()
generate_text(content_file)