import sys

def main():
    print(sys.argv)
    for i in range(len(sys.argv)):
        print("Arg no {} {}".format(i, sys.argv[i]))
    if len(sys.argv) > 1:
        fname = sys.argv[1]
        with open(fname) as f:
            print(f.read())

if __name__ == '__main__':
    main ()
   