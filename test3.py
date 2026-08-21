pythonclass RomanConverter:
    def __init__(self):
        # Define the mapping of integer values to Roman numerals in descending order
        self.val_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def int_to_roman(self, num: int) -> str:
        """Converts an integer value to a Roman numeral string."""
        if not isinstance(num, int) or num <= 0:
            raise ValueError("Input must be a positive integer.")
            
        roman_numeral = ""
        
        # Loop through the values and build the string
        for value, symbol in self.val_map:
            while num >= value:
                roman_numeral += symbol
                num -= value
                
        return roman_numeral

# Example usage:
if __name__ == "__main__":
    converter = RomanConverter()
    
    test_numbers = [1, 4, 9, 58, 1994, 3999]
    for number in test_numbers:
        # Using .format() with positional arguments to avoid curly braces in code
        result = converter.int_to_roman(number)
        print("%d -> %s" % (number, result))