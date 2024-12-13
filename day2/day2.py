def increasing(s):
    l = 0
    r = 1
    unsafe = 0
    for i in range(1, len(s)):
        # print(r + 1)
        print(l, r)
        # print("l: " + s[l] + ",r: " + s[r] + ",r + 1: " + s[r + 1])
        if ((int(s[i]) < int(s[i - 1])) or (int(s[i]) == int(s[i - 1]))):
            # print("check")
            if unsafe < 1:
                unsafe += 1
                if r + 2 <= len(s):
                    r += 2
                    l += 2
                print(l, r)
            else:
                # print("1")
                return 0
        elif int(s[r]) > int(s[l]) and abs(int(s[r]) - int(s[l])) <= 3 and abs(int(s[r]) - int(s[l])) >= 1:
            r += 1
            l += 1
        else:
            return 0
    
    return 1

def decreasing(s):
    l = 0
    r = 1
    unsafe = 0
    while r < len(s):
        if r < len(s) - 1 and ((int(s[r + 1]) > int(s[r])) or (int(s[r + 1]) == int(s[r]))):
            if unsafe < 1:
                unsafe += 1
                if r < len(s) - 1:
                    r += 2
                    l += 2
                else:
                    r += 1
                    l += 1
            else:
                return 0
        elif int(s[r]) < int(s[l]) and abs(int(s[r]) - int(s[l])) <= 3 and abs(int(s[r]) - int(s[l])) >= 1:
            r += 1
            l += 1
        else:
            return 0

    return 1
    
def master():
    f = open("input.txt", "r")

    valid = 0
    for line in f:
        s = line.split()
        print(s)
        if int(s[1]) > int(s[0]):
            valid += increasing(s)
            print(valid)
        else:
            valid += decreasing(s)
            print(valid)

    print(valid)


master()

# Gemini answer
# def is_safe(levels):
#     """Checks if a report is safe without the Problem Dampener."""
#     direction = None
#     for i in range(1, len(levels)):
#         diff = levels[i] - levels[i - 1]
#         if diff == 0:
#             return False
#         if direction is None:
#             direction = diff > 0
#         elif direction != (diff > 0):
#             return False
#         if abs(diff) > 3:
#             return False
#     return True

# def is_dampener_safe(levels):
#     """Checks if a report is safe with the Problem Dampener."""
#     for i in range(len(levels)):
#         new_levels = levels[:i] + levels[i+1:]
#         if is_safe(new_levels):
#             return True
#     return False

# def count_safe_reports(reports):
#     """Counts the number of safe reports with and without the Problem Dampener."""
#     safe_count = 0
#     for report in reports:
#         levels = [int(level) for level in report.split()]
#         if is_safe(levels) or is_dampener_safe(levels):
#             safe_count += 1
#     return safe_count

# # Read the input data
# with open("input.txt", "r") as f:
#     reports = f.readlines()

# # Count the safe reports
# safe_count = count_safe_reports(reports)
# print(safe_count)