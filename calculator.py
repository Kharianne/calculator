import re


class Calculator:

    def add(self, numbers: str)-> int:
        if numbers.startswith('//'):
            delimiter, numbers = self.determine_delimiter(numbers)
            numbers = numbers.strip()
            numbers = numbers.replace('\n', ',').replace(delimiter, ',')
        else:
            numbers = numbers.strip()
            numbers = numbers.replace('\n', ',')
        if not numbers:
            result = 0
        else:
            digits = numbers.split(',')
            # Handling of exception due to invalid input is responsibility of calling code
            # Strip whitespaces to allow input like "1,,2" (empty string should be 0)
            digits = [int(digit) for digit in digits if digit.strip() and int(digit) <= 1000]
            negatives = [digit for digit in digits if digit < 0]
            if negatives:
                raise ValueError('negatives not allowed ' + ', '.join(str(x) for x in negatives))
            result = sum(digits)
        return result

    # I put it outside of add function to be clearer.
    def determine_delimiter(self, numbers: str)->tuple:
        regex = re.compile('\[(.*?)\]')
        delimiter = re.findall(regex, numbers)[0]
        numbers = numbers.split('\n')[1]
        return delimiter, numbers

