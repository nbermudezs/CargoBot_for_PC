class Icon:
    @staticmethod
    def window_icon():
        f = open("images/icon.txt","r")
        return f.read()

if  __name__ == "__main__":
    Icon.window_icon()
