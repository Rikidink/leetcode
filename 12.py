"""
12. Integer to Roman

"""

class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

        nums = list(str(num))
        result = ""
        length = len(nums)


        for i in range(length):
            integer = int(nums[i])
            decimal = length - i

            # upper limit is 3999 inclusive so don't need to handle other cases
            if decimal == 4:
                result += 'M' * integer
            
            elif 1 <= integer <= 3:
                result += symbols[10**(decimal-1)] * integer
            elif 5 <= integer <= 8:
                result += symbols[5 * (10**(decimal-1))]
                result += symbols[10**(decimal-1)] * (integer - 5)
            elif integer == 4:
                result += symbols[10**(decimal-1)] + symbols[5 * (10**(decimal-1))]
            elif integer == 9:
                result += symbols[10**(decimal-1)] + symbols[10**(decimal)]

        return result




if __name__ == "__main__":
    s = Solution()
    s.intToRoman(3749)