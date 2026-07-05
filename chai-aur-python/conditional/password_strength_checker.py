# Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = "123456"

match password:
    case p if len(p) < 6:
        print(len(p),":", "weak")

    # case p if len(p) >= 6 and len(p) <= 10:

    case p if 6 <= len(p) <= 10:
        print(len(p),":", "medium")
    case p_:
        print(len(p),":", "strong")


# 6 <= len(p) <= 10