def decorr(result):
    def dist(*mark):
        for m in mark:
            if m>=75:
                print("DISTINCTION")
        result(*mark)
    return dist
@decorr
def result(*mark):
    for m in mark:
        if m>=33:
            pass
        else:
            print("fail")
            break
    else:
        print("pass")
result(35,74,43,39,38)
