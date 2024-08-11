 #WRITE A FUNCTION HAT TAKES A LIST OF INTEGERS AND RETURNS THE SUM OF ALL THE ELEMENTS IN THE LIST.
def sum_of_list(lst):
    return sum(lst)
numbers=[1,2,3,4,5,]
result= sum_of_list(numbers)
print(result)
      
#WRITE A FUNCTION THAT TAKES A TUPLE OF NUMBERS AND RETURNS THE SMALLEST NUMBER IN THE TUPLE.
def find_smallest_number(numbers_tuple):
    return min(numbers_tuple)
numbers = (4,8,9,3,1)
smallest = find_smallest_number(numbers)
print(smallest)

#WRITE A FUNCTION THAT TAKES A SET OF NUMBERS AND RETURNS A NEW SET WITH EACH ELEMENT SQUARED.
def square_elements(num_set):
     return{x ** 2 for x in num_set}
original_set = {1,2,3,4}
squared_set= square_elements(original_set)
print(squared_set)
