class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"

        def three(num):
            below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
                        "Eighteen", "Nineteen"]
            tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

            if num < 20:
                return below_20[num]
            elif num < 100:
                return tens[num // 10] + (" " + below_20[num % 10] if num % 10 != 0 else "")
            else:
                return below_20[num // 100] + " Hundred" + (" " + three(num % 100) if num % 100 != 0 else "")

        def less_than_billion(num):
            billion = num // 1000000000
            million = (num // 1000000) % 1000
            thousand = (num // 1000) % 1000
            remainder = num % 1000

            result = ""
            if billion: result += three(billion) + " Billion"
            if million: result += " " + three(million) + " Million" if result else three(million) + " Million"
            if thousand: result += " " + three(thousand) + " Thousand" if result else three(thousand) + " Thousand"
            if remainder: result += " " + three(remainder) if result else three(remainder)
            return result.strip()

        return less_than_billion(num)
