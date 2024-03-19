def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count = get_word_count(text)
  char_count = convert_dict_to_list(character_count(text))
  char_count.sort(reverse=True, key=sort_on)
  
  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count} words found in the document. \n")
  return format_output(char_count)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_word_count(text):
  words = text.split()
  return len(words)

def character_count(text):
  lowered_text = text.lower()
  count_dict = {}
  for t in lowered_text:
    if t in count_dict:
      count_dict[t] += 1
    else:
      count_dict[t] = 1
  return count_dict

def convert_dict_to_list(dict):
  dict_list = []
  for key, value in dict.items():
    if key.isalpha():
      new_dict = {"char": key, "count": value}
      dict_list.append(new_dict)
  return dict_list

def sort_on(dict):
  return dict["count"]

def format_output(list):
  for dict in list:
    char = dict["char"]
    count = dict["count"]
    print(f"The '{char}' character was found {count} times")
  return print("--- End Report ---")


main()