aCount, bCount, cCount  =0,0,0
for i in range(5):
    grade = input("Enter student grade: ")
    match grade:
        case "A":
            aCount += 1
        case "B":
            bCount += 1
        case "C":
            cCount+=1

print("A", aCount)
print("B", bCount)
print("C", cCount)

