import mapGlobal
import mapNode

def main():
    solution = False
    #create map
    our_map = mapGlobal.mapGlobal(33,33)

    #initialize map with text file
    input_file = "file.txt"
    our_map.initialize_map(input_file)

    while solution!=True:
        check_for_request()

if __name__ == "__main__":
    main()
