def fx():
    print("fy")
    def fy():
        print("fz")
        def fz():
            print("fx")
        fz()
    fy()
fx()