complimentary = {'A':'T','T':'A',"G":"C","C":"G"}
strand = input()
complimentaryStrand = ""
for let in strand:
    complimentaryStrand += complimentary[let]
print(complimentaryStrand)