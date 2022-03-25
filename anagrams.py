# --- modules ---
import tryalgo

# --- function: remove the duplicates from data ---
def remove_duplicates(list_value):
        # --- return list without duplicates, set() handles this ---
	return list(set(list_value))            

# --- function: anagram ---
def anagrams(SET):
    anagrams = {}                               # placeholder for data
    SET = SET.split(" ")                        # break phrase into list
    SET = remove_duplicates(SET)                # remove duplicates, they trigger false anagrams

    for word in SET:                            # begin for loop through SET
        signature = "".join(sorted(word))       # signature is sorted word from set

        if signature in anagrams:               # if signature in data
            anagrams[signature].append(word)    # append iterated value to key in data

        else:
            anagrams[signature] = [word]        # iterated value binds as a list to key

    # --- return signature in data if value of the key is greater than 1, meaning it is an anagrams ---                                            
    return [anagrams[signature] for signature in anagrams if len(anagrams[signature]) > 1]

# --- on run / import ---    
if __name__ == "__main__":
    SET = str(input("enter a phrase to get anagrammed: "))
    print("--- anagrams in phrase ---")
    print(anagrams(SET))
