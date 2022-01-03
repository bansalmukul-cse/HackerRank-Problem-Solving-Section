import textwrap

def wrap(string, max_width):
    s = ""
    for c in range(0,len(string),max_width):
        s += string[c:c+max_width] + "\n"
    return s

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
