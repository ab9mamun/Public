
def main():
    file=open("input1.txt","r+")
    wordcount=0
    lines = file.read().split('\n')
    #print(lines)
    for line in lines:
        words = line.split(',')
        #print(words)
        wordcount+= len(words)

    print('Word_count', wordcount)
    print('Hello')
    file.close();

if __name__ == "__main__":
    main()
