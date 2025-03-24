def q13():
    number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    num=int(input("Enter the number:"))
    if 0 <= num <= 19:
        print(number_words[num])
    else:
        print("Number out of range!")
q13()
