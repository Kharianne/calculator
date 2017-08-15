import re

class Calculator:

    def add(self, numbers: str)-> int:
        if numbers.startswith('//'):
            delimeter, numbers = self.determine_delimeter(numbers)
            numbers = numbers.strip()
            numbers = numbers.replace('\n', ',').replace(delimeter, ',')
        else:
            numbers = numbers.strip()
            numbers = numbers.replace('\n', ',')
        if not numbers:
            result = 0
        else:
            digits = numbers.split(',')
            result = 0
            for digit in digits:
                try:
                    result += int(digit)
                except ValueError:
                    result = result
                    continue
        return result

    def determine_delimeter(self, numbers: str)->tuple:
        regex = re.compile('\[(.*?)\]')
        delimeter = re.findall(regex, numbers)[0]
        numbers = numbers.split('\n')[1]
        return delimeter, numbers

