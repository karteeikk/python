def greet(fx):
    def mfx():
        print("before decor")
        fx()
        print("after decor")
    return mfx
@greet
def hello():
    print("hello world")
hello()