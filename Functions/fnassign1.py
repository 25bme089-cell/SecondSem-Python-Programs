# Function to create intersection of two lists
def create_list(list1, list2):
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result

# Example usage
l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
print("Intersection:", create_list(l1, l2))
