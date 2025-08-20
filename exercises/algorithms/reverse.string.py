def reverse_string(s: str) -> str:
    return s[::-1]

if __name__ == "__main__":
    word = "security"
    print(f"Original: {word}, Reversed: {reverse_string(word)}")

