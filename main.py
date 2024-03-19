def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count = get_word_count(text)
  char_count = character_count(text)
  print(f"Total words: {word_count}")
  print(char_count)


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

main()