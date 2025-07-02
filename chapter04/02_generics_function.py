from typing import Sequence, TypeVar, List, Any, Optional

# A generic type variable
T = TypeVar('T')

Number = TypeVar('Number', int, float)

print(type(Number))

# first element of a sequence
def first(seq: Sequence[T]) -> T:
    """
    Returns the first element of a sequence.
    if sequence is empty, raises a ValueError

    Args:
        seq (Sequence[T]): The sequence from which to get the first element.

    Returns:
        T: The first element of the sequence.
    """

    if not seq:
        raise ValueError("Sequence is empty")
    return seq[0]

# the last element of a sequence
def last(seq: Sequence[T]) -> T:
    if not seq:
        raise ValueError("Sequence is empty")
    return seq[-1]    

# the number of elements that are truthy in a list
def count_truthy(elements: List[Any]) -> int:
    """
    Counts how many elements in the list are truthy
    
    Args:
        elements (List[Any]): A list of elements.

    Returns:
        int: The number of elements that are truthy.
    """
    return sum(1 for element in elements if element)

def len_str(s: Optional[str] = None) -> int:
    return len(s) if s is not None else 0

def main():
    numbers = [10, 20 , 30 , 40 , 50]
    print(f"First number: {first(numbers)}")
    print(f"Last number: {last(numbers)}")

    try:
        print("First element of []:", first([]))
    except ValueError as e:
        print(e)
    
    mixed_values = [0 ,True, False, "hello", "", None, 17]
    print(f"Truthy values are: {count_truthy(mixed_values)}")

    print("Length of 'Hello there':", len_str('Hello there'))
    print("Length of 'None':", len_str(None))

    print(first("Hello CF!"))



if __name__ == "__main__":
    main()