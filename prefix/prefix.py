def common_prefix(list1, list2):
    prefix = []
    for item1, item2 in zip(list1, list2):
        if item1 == item2:
            prefix.append(item1)
        else:
            break
    return prefix

# # Example usage
# list1 = [1, 2, 3, 4, 5]
# list2 = [1, 2, 3, 9, 10]
# result = common_prefix(list1, list2)
# print(result)