from typing import List


def test1():
    txt = "from test1"
    print(txt)

    def test2():
        txt = "from test2"
        print(txt)

    test2()


def mul1(a):
    def mul2(b):
        return a * b

    return mul2


def choose_func(nums: List[int], func1, func2):
    return func2(nums) if any(num < 0 for num in nums) else func1(nums)


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


if __name__ == '__main__':
    """
    Task 1
    Write a Python program to detect the number of local variables declared in a function.
    """
    print("Count variable: ", test1.__code__.co_nlocals)
    """
    Task 2
    Write a Python program to access a function inside a function (Tips: use function, which returns another function)
    """

    test1()
    res = mul1(5)
    print(res(5))

    """
    Task 3
    Write a function called `choose_func` which takes a list of nums and 2 callback functions. 
    If all nums inside the list are positive, execute the first function on that list and return the result of it. 
    Otherwise, return the result of the second one     
    
    def choose_func(nums: list, func1, func2):    
        pass             
    # Assertions
    nums1 = [1, 2, 3, 4, 5]    
    nums2 = [1, -2, 3, -4, 5]
    """
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]
    print(choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25])
    print(choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5])
