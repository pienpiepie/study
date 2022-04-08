from tkinter.tix import Y_REGION


X = input()
Y = input()
print(int(X) + int(Y) if X.isdecimal() and Y.isdecimal() else X + Y)