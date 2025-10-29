# There is a large pile of socks that must be paired by color. 
# Given an array of integers representing the color of each sock, 
# determine how many pairs of socks with matching colors there are.
def count_matching_pairs(socks):
    color_count = {}
    for sock in socks:
        color_count[sock] = color_count.get(sock, 0) + 1
    pairs = 0
    for count in color_count.values():
        pairs += count // 2
    return pairs


def main():
    socks = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    result = count_matching_pairs(socks)
    print(f"Number of matching pairs: {result}")
    
if __name__ == "__main__":
    main()