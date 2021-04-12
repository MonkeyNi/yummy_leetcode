class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        res = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            0: "Sunday"
        }
        
        days = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 31,
            12: 30
        }

        if (year%400==0) or (year%4==0 and year%100!=0):
            days[2] = 29
        print(days[2])
        
        n_days = list(days.values())
        for i in range(1, 12):
            n_days[i] += n_days[i-1]
        
        this_days = n_days[month-2] + day
        mod = year-1+(year-1)/4-(year-1)/100+(year-1)/400+this_days - 1
        return res[int(mod%7)]

test = Solution()
day = 31
month = 8
year = 2019
day = 18
month = 7
year = 1999
day = 21
month = 12
year = 1980
res = test.dayOfTheWeek(day, month, year)
print(res)