answer_list = [1, 4, 7]

while True:
    answer = input("Please Answer: ")
    if answer == "q":
        break

    answer = int(answer)
    if answer in answer_list:
        print("正解")
        break

    print("不正解")
