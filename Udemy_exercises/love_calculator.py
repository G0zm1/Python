def calculate_love_score(name1, name2):
    count1 = 0
    count2 = 0
    word1 = "true"
    word2 = "love"


    for letter1 in word1:
        for letter2 in name1:
            if letter2 == letter1:
                count1 += 1
        for letter3 in name2:
            if letter3 == letter1:
                count1 += 1
                

    for letter4 in word2:
        for letter2 in name1:
            if letter2 == letter4:
                count2 += 1
        for letter3 in name2:
            if letter3 == letter4:
                count2 += 1
                
    print(f"{count1}{count2}")
    
calculate_love_score(name1 = "".lower(), name2 = "".lower())
