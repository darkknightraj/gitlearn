an_letters = "aeficlmnorAEFICLMOR"
word = input("Give me word i will cheer of you ? ")
times = int(input("Enter the enthusisam level (1-10)  "))
for c in word:
    if c in an_letters:
        print(f"Give me an {c} : {c}")
    else:
        print(f"Give me a {c} : {c} ")
for i  in range(times):
    print(word,"!!!")
