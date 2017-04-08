import mapGlobal
import mapNode

def main():
    solution = False
    #create map
    our_map = mapGlobal.mapGlobal(33,33)

    #initialize map with text file
    input_file = "file.txt"
    our_map.initialize_map(input_file)

    second_map = our_map
    second_map.getNode(10,10).options = 7

    our_map.blend_map(second_map)
    our_map.print_map()

    #while solution!=True:
    #    check_for_request()

if __name__ == "__main__":
    main()
