import re

def check_password_strength(password):
    feedback = []
    
    if len(password) < 8:
        feedback.append("- Must be at least 8 characters long.")
    
    if not re.search(r"\d", password):
        feedback.append("- Add at least one number (0-9).")
    
    if not re.search(r"[A-Z]", password):
        feedback.append("- Add at least one uppercase letter (A-Z).")
    
    if not re.search(r"[a-z]", password):
        feedback.append("- Add at least one lowercase letter (a-z).")
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("- Add at least one special character (e.g., @, #, $).")

    if not feedback:
        return "Strong Password!"
    else:
        return "Weak Password. Missing:\n" + "\n".join(feedback)

print("--- Password Strength Checker ---")
print("Note: please make sure to enter ur password inside double quotes, example:\"Mypass12@\"")
user_input = input("Enter password: ")
result = check_password_strength(user_input)
print(result)
