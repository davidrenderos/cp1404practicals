word_count_dict = {}
text = input("Text: ")
text_list = text.split()
for word in text_list:
    count = word_count_dict.get(word, 0)
    word_count_dict[word] = count + 1

# Add sort capability
text_list = list(word_count_dict.keys())
text_list.sort()

for word in text_list:
    print("{} : {}".format(word, word_count_dict[word]))
