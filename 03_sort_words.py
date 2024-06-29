def sort_words(phrase):
  phrase_to_sort = phrase.split(" ")
  phrase_to_sort.sort(key = lambda word : word.lower())
  return phrase_to_sort

print(sort_words("BANANA apple ChErRy"))
print(sort_words("string of Words"))