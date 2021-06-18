articles = ["1. Name and territory of the Union",
"2. Admission or establishment of new States",

"3. Formation of new States and alteration of areas, boundaries or names of existing States",

"4. Laws made under articles 2 and 3 to provide for the amendment of the First and the Fourth Schedules and  supplemental, incidental and consequential matters",

"5. Citizenship at the commencement of the Constitution",

"6. Rights of citizenship of certain persons who have migrated to India from Pakistan"]



''' whenever you findout the string "1. Name and territory of the Union" in the file named articlesonly.txt search until "2. Admission or establishment of new States" and add everything in between to a
newly created file named "1. Name and territory of the Union.md" '''

for i in range(len(articles)):
    string1 = articles[i]

    file1 = open('articlesonly.txt', 'r')

    flag = 0
    index = 0

    for line in file1:
        index += 1

        #cheching string is present in line or not.
        if string1 in line:
            flag = 1
            break

    if flag == 0:
            print('Not foundda')
            print(i)
    else:
            print("found in line", index)

#closing the file1
file1.close()
