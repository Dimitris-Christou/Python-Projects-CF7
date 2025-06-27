def compare_lists(list1, list2):
    """
    Compares two lists for identity and equality.

    Args: 
        list1 (list): The fisrt list to compare
        list2 (list): The second list to compare.

    Return:
        None   
    """
    # identity check -> list1 is list2
    print(f"{list1} is {list2}: {list1 is list2}")

    # equality check -> list1 == list2
    print(f"{list1} == {list2}: {list1 == list2}")

def main():
    my_list = [1, 2, 3]
    your_list = [1, 2, 3]
    new_list = my_list

    # compare lists
    compare_lists(my_list, your_list)
    print(id(my_list))
    print(id(your_list))

    compare_lists(my_list, new_list)


if __name__ == "__main__":
    main()