def same_chars(text: str, num1, num2):
    if 0 <= num1 < len(text) and 0 <= num2 < len(text):
        return text[num1] == text[num2]
    else:
        return False
    
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))