"""
12. Integer to Roman

"""

class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            'I': '1',
            'V': '5',
            'X': '10',
            'L': '50',
            'C': '100',
            'D': '500',
            'M': '1000'
        }


        nums = list(str(num))
        result = ""
        length = len(nums)


        for i in range(length):
            integer = int(nums[i])
            decimal = length - i
            print(decimal)

            # upper limit is 3999 inclusive so don't need to handle other cases
            if decimal == 4:
                result += 'M' * integer

            elif decimal == 3:
                if 1 <= integer <= 3:
                    result += 'C' * integer
                elif 5 <= integer <= 8:
                    result += 'D'
                    result += 'C' * (integer - 5)
                elif integer == 4:
                    result += 'CD'
                else:
                    result += 'CM'
            
            elif decimal == 2:
                if 1 <= integer <= 3:
                    result += 'X' * integer
                elif 5 <= integer <= 8:
                    result += 'L'
                    result += 'X' * (integer - 5)
                elif integer == 4:
                    result += 'XL'
                else:
                    result += 'XC'

            elif decimal == 1:
                if 1 <= integer <= 3:
                    result += 'I' * integer
                elif 5 <= integer <= 8:
                    result += 'V'
                    result += 'I' * (integer - 5)
                elif integer == 4:
                    result += 'IV'
                else:
                    result += 'IX' 



        return result




if __name__ == "__main__":
    s = Solution()
    s.intToRoman(3749)