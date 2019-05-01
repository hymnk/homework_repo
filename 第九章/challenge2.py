string = input("あなたの好きな食べものは？: ")

with open("answer.txt", "w", encoding="utf-8") as f:
    f.write(string)

    