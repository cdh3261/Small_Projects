def ff(year):
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        return '29'
    return '28'


def f(month, year):
    dict = {'1':'31', '3':'31', '5':'31', '7':'31', '9':'31', '11':'31',
            '4':'30', '6':'30', '8':'30', '10':'30', '12':'30',
            '2':ff(int(year))}
    return dict.get(month)


year, month = input().split()
days = f(month, year)

print(days + ' days for ' + year + '-' + month)