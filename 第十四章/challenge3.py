class CheckParam:
    def __init__(self):
        self.name = 'Kel'

check_param = CheckParam()
same_check_param = check_param
print(same_check_param is check_param)

other_check_param = CheckParam()
print(other_check_param is check_param)