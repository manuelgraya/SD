my_list = [1, "a", 3, 4, 5]

print(my_list[:]) #[START : END]
print(my_list[1:3]) # [1 : 3]

print(my_list[: :2]) # salto de dos en dos

index = [1, 2, 3]
languages = ["python", "c", "java"]

dictionary = dict(zip(index, languages))
print(dictionary)