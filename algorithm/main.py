result = list()
def permutation(string, start, stop):
    if start == stop - 1:
        if not string in result:
            result.append(string)
    else:
        for str_index in range(start, stop):
            listy = list(string)
            current_char = listy[start]
            listy[start]=listy[str_index]
            listy[str_index] = current_char
            permutation("".join(listy), start+1, stop)
            current_char=listy[str_index]
            listy[start] = listy[str_index]
            listy[str_index] = current_char



def main():
    entry_list = open("strings.txt", "r")
    if entry_list.mode == "r":
        contents = entry_list.read()
        content_list = contents.split()
        for word in content_list:
            string = word
            length = len(string)
            permutation(string, 0, length)
            result_sorted = sorted(result)
            result.clear()
            print(",".join(result_sorted))
if __name__ == "__main__":
    main()