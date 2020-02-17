
# Reads the .txt and converts its every line in arrays
def txtToArray(text):
    
    file = open(str(text),errors='ignore')
    my_list = file.readlines()
    file.close()

    return my_list

# Joins all the arrays into a string
def listToString(my_array):  
    
    my_string = ""   

    for element in my_array:  
        my_string += element   
     
    return my_string  

# Gets all the specified digits numbers of the text and saves it into a text file
def getNumbers(file_text, name_number_text, number_of_digits):

  new_string = ''.join((character if character in '0123456789' else ' ') for character in file_text)

  list_of_numbers = [int(i) for i in new_string.split()]

  for i in range(len(list_of_numbers)):
    if len(str(list_of_numbers[i])) == number_of_digits:
      numbers = open(str(name_number_text), "a")
      numbers.write(str(list_of_numbers[i]) + "\n")
      numbers.close()

  return str(name_number_text)

# Compare the two text files with the numbers and returns the similar ones
def compareNumbers(first_numbers_file, second_numbers_file):
  
  numbers1 = open(str(first_numbers_file), "r")
  lista1 = numbers1.readlines()

  numbers2 = open(str(second_numbers_file), "r")
  lista2 = numbers2.readlines()

  result = list(set(lista1) & set(lista2))

  my_file = open("similar_numbers.txt", "w")
  my_file.writelines(result)
  my_file.close()



text_file1 = str(input("The first .txt file: "))
text_file2 = str(input("The second .txt file: "))

name_numbers_text_file1 = str(input("Text file which saves the first list of numbers: "))
name_numbers_text_file2 = str(input("Text file which saves the second list of numbers: "))

number_digits = int(input("Length of the number in digits you want to search for: "))

array1 = txtToArray(text_file1)
array2 = txtToArray(text_file2)

string1 = listToString(array1)
string2 = listToString(array2)

numbers_file1 = getNumbers(string1, name_numbers_text_file1, number_digits)
numbers_file2 = getNumbers(string2, name_numbers_text_file2, number_digits)

compareNumbers(numbers_file1, numbers_file2)
