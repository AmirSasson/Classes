

# https://replit.com/languages/python3
    
# ששש... זאת הססמא
password = "87445"


def TryPassword(text)->bool: 
    """
    בודק אם הססמא תואמת
    """    
    return password == text



for מספר in range(100000):
    stringNumber = str(מספר) # להפוך מספר לטקסט
    passwordCandidate = stringNumber.zfill(5) # לרפד באפסים ,לדוגמא המספר 1 יהיה "00001" כמספר הספרות של הססמא
    print(passwordCandidate) # נדפיס למסך את הקוד שאנחנו רוצים לנסות
    if TryPassword(passwordCandidate): # ננסה את הססמא
        print(f'your code is : {passwordCandidate}') # הצלחנו!!
        break # לסיים את הניסיונות
    # לא הצלחנו.. ננסה את המספר הבא





