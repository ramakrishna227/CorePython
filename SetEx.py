def main():
    s = set(("hellooo", "hello"))  # double round braces for set of strings
    # single round brace expects single string as arguement and add the characters of sting to the set defined
    for x in s: print(x)
    s = sorted(set("helloooo"))
    for x in s: print(x, end='')  # end='' as an arguement will pring the values in same line

    # set can also be defined as below
    print()
    s = {'a', 'b', 'c'}
    for x in s: print(x)

    # we can perform different operations among set like -, |, ^ , & etc

if __name__ == '__main__': main()
