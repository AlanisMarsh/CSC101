import data
import math

# Write your functions for each part in the space below.

# Part 1
# takes a word and returns the number of vowels within the word
def vowel_count(word:str)->int:
    count = 0
    for n in range(len(word)):
        if word[n] == 'a' or word[n] == 'e' or word[n] == 'i' or word[n] == 'o' or word[n] == 'u' or word[n] == 'A' or word[n] == 'E' or word[n] == 'I' or word[n] == 'O' or word[n] == 'U':
            count += 1

    return count

# Part 2
# takes a list of lists and returns all of the lists within the list that only have two indexes
def short_lists(L:list[list[int]])-> list[list[int]]:
    new_list = []
    for n in range(len(L)):
        if len(L[n]) == 2:
            new_list.append(L[n])
    return new_list


# Part 3
# takes a list of lists and rearranges all lists of 2 indexes so that they are in ascending order
# returns the list including the lists longer than 2 indexes
def ascending_pairs(L:list[list[int]])->list[list[int]]:
    new_list = []
    for n in range(len(L)):
        if len(L[n]) == 2:
            if L[n][0] > L[n][1]:
                temp = L[n][0]
                L[n][0] = L[n][1]
                L[n][1] = temp
            new_list.append(L[n])
        else:
            new_list.append(L[n])

    return new_list

# Part 4
# adds two types of Price making sure that cents remains at or below 99
# returns a type Price
def add_prices(P1:data.Price, P2:data.Price)-> data.Price:
    dollars = P1.dollars + P2.dollars
    cents = P1.cents + P2.cents
    if cents > 99:
        cents -= 100
        dollars += 1

    return data.Price(dollars,cents)

# Part 5
# takes in a type Rectangle and returns a float of the area of said rectangle
def rectangle_area(rect: data.Rectangle) -> float:
    width = rect.bottom_right.x - rect.top_left.x
    height = rect.top_left.y - rect.bottom_right.y
    return width*height

# Part 6
# takes a string of an author name and a list of type Book
# returns all book titles written by the author
def books_by_author(auth:str, bks:list[data.Book]) -> list[str]:
    book_with_author = []
    for idx in range(len(bks)):
        for idx2 in range(len(bks[idx].authors)):
            if bks[idx].authors[idx2] == auth:
                book_with_author.append(bks[idx].title)
    return book_with_author

# result = books_by_author('Sarah J Maas',[data.Book(['Sarah J Maas'], 'Throne of Glass'),  data.Book(['JK Rowling'], 'Harry Potter'), data.Book(['Sarah J Maas'], 'A Court of Thrones and Roses')])
# print(result)

# Part 7
# finds the smallest possible measurements to create a circle that surrounds the given type Rectangle
def circle_bound(rect:data.Rectangle) -> data.Circle:
    a = (rect.bottom_right.x + rect.top_left.x)/2
    b = (rect.bottom_right.y + rect.top_left.y)/2
    center = data.Point(a,b)
    radius = math.sqrt((a - rect.bottom_right.x)*(a - rect.bottom_right.x) + (b - rect.bottom_right.y)*(b - rect.bottom_right.y))
    return(data.Circle(center, radius))

# Part 8
# takes a list of type Employees including their names and pay
# computes the average pay of the employees and returns the names (in a list) of all the employees who are
# paid less than the average pay
def below_pay_average(employee:list[data.Employee])-> list[str]:
    new_list = []
    ave = 0
    for idx in range(len(employee)):
        ave += employee[idx].pay_rate
    ave = ave/len(employee)
    for idx1 in range(len(employee)):
        if ave > employee[idx1].pay_rate:
            new_list.append(employee[idx1].name)
    return new_list

