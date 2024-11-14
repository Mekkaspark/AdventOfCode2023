with open('input.txt', 'r') as file:
    total_sum = 0

    for line in file:
        # use isdigit() to filter out non numbers
        digits = [char for char in line if char.isdigit()]
        if digits:
            if len(digits) == 1:
                first_digit = last_digit = digits[0]
            else:
                # Slice first and last
                first_digit = digits[0]
                last_digit = digits[-1]

            two_digit_number = int(first_digit + last_digit)
            # print(two_digit_number)
            # C# equivalent
            # int twoDigitNumber = int.Parse(firstDigit.ToString() + lastDigit.ToString());

            total_sum += two_digit_number
        else:
            print("NO DIGITS FOUND!!")

    # Print sum
    print("Total Sum:", total_sum)