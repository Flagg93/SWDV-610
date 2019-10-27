def writelines(times, line):
    for time in range(times):
        print(line)
        
def main():
    numTimes = 100
    lineToWrite = input("Enter a line to write: ")
    writelines(numTimes, lineToWrite)

main()