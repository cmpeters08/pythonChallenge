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
    string = "hat"
    length = len(string)
    permutation(string, 0, length)
    to_be_sorted = ", ".join(result)
    print(sorted(result))
if __name__ == "__main__":
    main()