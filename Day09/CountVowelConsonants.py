text = "Hello World"
vowels = "aeiouAEIOU"
v_count = sum(1 for ch in text if ch in vowels)
c_count = sum(1 for ch in text if ch.isalpha() and ch not in vowels)
print("Vowels:", v_count, "Consonants:", c_count)
