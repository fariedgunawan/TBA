def tokenRecognizer(word: str):
    word = word.lower()
    try:
        if isSubjek(word): return 'S'
        elif isPredikat(word): return 'P'
        elif isObjek(word): return 'O'
        elif isKeterangan(word): return 'K'
        else: raise Exception("TokenUnrecognizedError")
    except Exception as e: 
        print(f"ERROR: {e}")
        print(f"Word \"{word}\" tidak masuk ke kategori token manapun\n")
        return '?'

def isSubjek(word: str) -> bool:
    # Subjek = {'aku', 'anda', 'kamu', 'dia', 'saya'}
    currState = 0
    for letter in word:
        match currState:
            case -1: break
            case 0:
                if letter == 'a': currState = 1
                elif letter == 'k': currState = 2
                elif letter == 'd': currState = 3
                elif letter == 's': currState = 4
                else: currState = -1
            case 1:
                if letter == 'n': currState = 5
                elif letter == 'k': currState = 6
                else: currState = -1
            case 2: currState = 7 if letter == 'a' else -1
            case 7: currState = 11 if letter == 'm' else -1 
            case 11: currState = 10 if letter == 'u' else -1 #final state
            case 10: currState = 10 if letter == ' ' else -1 #final state
            case 3: currState = 8 if letter == 'i' else -1
            case 8: currState = 12 if letter == 'a' else -1 #final state
            case 12: currState = 12 if letter == ' ' else -1 #final state
            case 4: currState = 9 if letter == 'a' else -1
            case 9: currState = 13 if letter == 'y' else -1
            case 13: currState = 12 if letter == 'a' else -1 # FINAL STATE
            case 5: currState = 8 if letter == 'd' else -1
            case 8: currState = 12 if letter == 'a' else -1 #FINAL STATE
            case 6: currState = 10 if letter == 'u' else -1 #FINAL STATE
    return currState == 10 or currState == 12 

def isPredikat(word: str) -> bool:
    # Predikat = {'makan', 'minum', 'baca', 'tulis', 'lihat'}
    currState = 0
    for letter in word:
        match currState:
            case -1: break
            case 0:
                if letter == 'm': currState = 1
                elif letter == 'b': currState = 2
                elif letter == 't': currState = 3
                elif letter == 'l': currState = 4
                else: currState = -1
            case 1:
                if letter == 'a': currState = 5
                elif letter == 'i': currState = 6
                else: currState = -1
            case 2: currState = 7 if letter == 'a' else -1
            case 7: currState = 12 if letter == 'c' else -1
            case 12: currState = 17 if letter == 'a' else -1
            case 17: currState = 17 if letter == ' ' else -1 #Final State
            case 3: currState = 8 if letter == 'u' else -1
            case 8: currState = 13 if letter == 'l' else -1
            case 13: currState = 18 if letter == 'i' else -1
            case 18: currState = 22 if letter == 's' else -1
            case 22: currState = 22 if letter == ' ' else -1 #FINAL STATE
            case 4: currState = 9 if letter == 'i' else -1
            case 9: currState = 14 if letter == 'h' else -1
            case 14: currState = 19 if letter == 'a' else -1
            case 19: currState = 23 if letter == 't' else -1
            case 23: currState = 23 if letter == ' ' else -1 #FINAL STATE
            case 5: currState = 10 if letter == 'k' else -1 
            case 10: currState = 15 if letter == 'a' else -1 
            case 15: currState = 20 if letter == 'n' else -1 
            case 20: currState = 20 if letter == ' ' else -1 #Final state
            case 6: currState = 11 if letter == 'n' else -1 
            case 11: currState = 16 if letter == 'u' else -1 
            case 16: currState = 21 if letter == 'm' else -1 
            case 21: currState = 21 if letter == ' ' else -1 #Final State
    return currState == 17 or currState == 22 or currState == 23 or currState == 20 or currState == 21

def isObjek(word: str) -> bool:
    # Objek = {'nasi', 'air', 'buku', 'surat', 'gambar'}
    currState = 0
    for letter in word:
        match currState:
            case -1: break
            case 0:
                if letter == 'n': currState = 1
                elif letter == 'a': currState = 2
                elif letter == 'b': currState = 3
                elif letter == 's': currState = 4
                elif letter == 'g': currState = 5
                else: currState = -1
            case 1: currState = 6 if letter == 'a' else -1
            case 6: currState = 11 if letter == 's' else -1
            case 11: currState = 15 if letter == 'i' else -1 #Final state
            case 15: currState = 15 if letter == ' ' else -1 #Final state
            case 2: currState = 7 if letter == 'i' else -1
            case 7: currState = 16 if letter == 'r' else -1 #Final state
            case 16: currState = 16 if letter == ' ' else -1 #Final state
            case 3: currState = 8 if letter == 'u' else -1
            case 8: currState = 12 if letter == 'k' else -1
            case 12: currState = 17 if letter == 'u' else -1 #Final state
            case 17: currState = 17 if letter == ' ' else -1 #Final state
            case 4: currState = 9 if letter == 'u' else -1
            case 9: currState = 13 if letter == 'r' else -1
            case 13: currState = 20 if letter == 'a' else -1
            case 20: currState = 18 if letter == 't' else -1 #Final State
            case 18: currState = 18 if letter == ' ' else -1 #Final State
            case 5: currState = 10 if letter == 'a' else -1
            case 10: currState = 14 if letter == 'm' else -1
            case 14: currState = 21 if letter == 'b' else -1
            case 21: currState = 19 if letter == 'a' else -1
            case 19: currState = 16 if letter == 'r' else -1 #Final state
    return currState == 15 or currState == 16 or currState == 17 or currState == 18
    
def isKeterangan(word: str) -> bool:
    # Ket = {'dikapal', 'dikantor', 'dikampung', 'dipasar', 'ditelyu'}
    currState = 0
    for letter in word:
        match currState:
            case -1: break
            case 0: currState = 2 if letter == 'd' else -1
            case 2: currState = 3 if letter == 'i' else -1
            case 3:
                if letter == 'k': currState = 4
                elif letter == 'p': currState = 5
                elif letter == 't': currState = 6
                else: currState = -1
            case 4: currState = 7 if letter == 'a' else -1
            case 7:
                if letter == 'p': currState = 10
                elif letter == 'n': currState = 11
                elif letter == 'm': currState = 12
                else: currState = -1
            case 10: currState = 15 if letter == 'a' else -1
            case 15: currState = 18 if letter == 'l' else -1 #Final State
            case 11: currState = 16 if letter == 't' else -1
            case 16: currState = 19 if letter == 'o' else -1
            case 19: currState = 23 if letter == 'r' else -1 #Final state
            case 12: currState = 17 if letter == 'p' else -1
            case 17: currState = 20 if letter == 'u' else -1
            case 20: currState = 24 if letter == 'n' else -1
            case 24: currState = 25 if letter == 'g' else -1 #Final State
            case 5: currState = 8 if letter == 'a' else -1
            case 8: currState = 13 if letter == 's' else -1
            case 13: currState = 21 if letter == 'a' else -1
            case 21: currState = 26 if letter == 'r' else -1 #final state
            case 6: currState = 9 if letter == 'e' else -1
            case 9: currState = 14 if letter == 'l' else -1
            case 14: currState = 22 if letter == 'y' else -1
            case 22: currState = 27 if letter == 'u' else -1 #Final State
    return currState == 18 or currState == 23 or currState == 25 or currState == 26 or currState == 27

def parser(sentence):
    # Definisikan jenis kesalahan yang akan digunakan untuk menandai kesalahan parsing
    ERR = Exception('ParsingError')
    
    # Memecah kalimat menjadi kata-kata individu dan menambahkan string kosong di akhir
    words = sentence.split()
    words.append('')
    
    # List untuk menyimpan hasil parsing
    res = []
    
    # Stack untuk menyimpan status parsing
    stack = []
    
    # State awal
    state = 0
    print("Stack:")
    print(stack)
    
    # Mulai dengan '#' sebagai penanda akhir stack
    stack.append('#')
    state = 1
    print(stack)
    
    # Tambahkan 'X' ke stack untuk mulai parsing dari non-terminal 'X'
    stack.append('X')
    state = 2
    
    # Indeks untuk iterasi melalui kata-kata
    i = 0
    
    try:
        # Lakukan parsing sampai stack hanya berisi '#'
        while stack[-1] != '#':
            print(stack)
            
            # Ambil kata saat ini
            word = words[i]
            
            # Dapatkan token dari kata saat ini jika kata tidak kosong
            if word != '': 
                token = tokenRecognizer(word)
            
            # Tentukan tindakan berdasarkan elemen teratas dari stack
            match stack[-1]:
                case 'X':
                    if token == 'S':
                        stack.pop()
                        stack.append('Y')
                        stack.append('P')
                        stack.append('S')
                    else: 
                        raise ERR
                case 'Y':
                    if word == '':
                        stack.pop()
                    else:
                        if token == 'O':
                            stack.pop()
                            stack.append('Z')
                            stack.append('O')
                        elif token == 'K':
                            stack.pop()
                            stack.append('Z')
                        else: 
                            raise ERR
                case 'Z':
                    if word == '':
                        stack.pop()
                    elif token == 'K':
                        stack.pop()
                        stack.append('K')
                    else: 
                        raise ERR
                case 'S':
                    if token == 'S':
                        res.append(stack.pop())
                        stack.append(word)
                    else: 
                        raise ERR
                case 'P':
                    if token == 'P':
                        res.append(stack.pop())
                        stack.append(word)
                    else: 
                        raise ERR
                case 'O':
                    if token == 'O':
                        res.append(stack.pop())
                        stack.append(word)
                    else: 
                        raise ERR
                case 'K':
                    if token == 'K':
                        res.append(stack.pop())
                        stack.append(word)
                    else: 
                        raise ERR
                case _:
                    if token != '?':
                        stack.pop()
                        i += 1
                    else: 
                        raise ERR
        
        print(stack)
        stack.pop()
        print(stack)

        print("Struktur: ", end='')
        for i in res[:-1]:
            print(f"{i} - ", end='')
        print(res[-1], "\n")

        return True 
    except Exception as e:
        print(f"ERROR: {e}")
        print(f"Kalimat \"{sentence}\" struktur tidak sesuai\n")
        return False


if __name__ == '__main__':  
    sentence = input("Kalimat: ")
    print()
    print(f"String: {sentence}\nStatus: Diterima\n") if parser(sentence) else print(f"String: {sentence}\nStatus: Ditolak \n") # type: ignore