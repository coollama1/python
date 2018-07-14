def anagram(string_1,string_2):
    if len(string_1) != len(string_2):
        return False
    for i in string_1:
        char_is_in_string = False #matching char isn't found yet
        for j in string_2:
            if i == j:
                char_is_in_string = True #matching char is found

        if char_is_in_string == False:
            return False

    return True
    
print("\n - Part 1 - \n")

input_string = input("Enter both words seperated by a space and I will \ntell you if they are anagrams of each other\n")
input_list = input_string.split()

if len(input_list) == 2:
    if anagram(input_list[0], input_list[1]):
        print("Hooray, both words are an anagram of each other :)")
    else:
        print("Sorry, the words you provided aren't anagrams :(")
else:
    print("Sorry, input must be entered in the correct format (exp: input1 input2)")

print("\n - Part 2 - \n")

Letters_LC = "abcdefghijklmnopqrstuvwxyz"
Letters_UC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

All_Letters = Letters_LC + Letters_UC
All_Letters_Dictionary = dict()
count = 0

for i in All_Letters:
    All_Letters_Dictionary[i] = count
    count = count + 1

print(All_Letters_Dictionary)