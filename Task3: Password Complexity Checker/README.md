This is a Python program that assesses the strength of a password based on several criteria, 
such as its length, and the presence of uppercase and lowercase letters, numbers, and special characters. 
The tool will also provide feedback to users about the password's strength and suggest improvements if necessary.

How the program works:

Criteria for password strength:

1. Length: The password must be at least 8 characters long.
2. Uppercase letters: There should be at least one uppercase letter.
3. Lowercase letters: There should be at least one lowercase letter.
4. Digits: The password must contain at least one digit.
5. Special characters: The password should include at least one special character (non-alphanumeric symbol like @, #, !, etc.).

Password Strength Feedback:

1. The password is evaluated against the five criteria mentioned above.
2. The total score is calculated by summing up the criteria met by the password.
3. Based on the score, the program provides one of the following feedbacks:
   
    a. Strong password: All criteria are met.
  
    b. Good password: The password meets most criteria but lacks a special character or could be longer.
  
    c. Medium strength: Some important criteria are missing (e.g., no numbers or special characters).
  
    d. Weak password: The password only meets a couple of criteria and is not considered secure.
  
    e. Very weak password: The password fails to meet essential security requirements, such as minimum length or the presence of different character types.
