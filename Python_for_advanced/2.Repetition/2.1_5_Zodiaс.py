dic = {
    2000: "Дракон",
    2001: "Змея",
    2002: "Лошадь",
    2003: "Овца",
    2004: "Обезьяна",
    2005: "Петух",
    2006: "Собака",
    2007: "Свинья",
    2008: "Крыса",
    2009: "Бык",
    2010: "Тигр",
    2011: "Заяц"
    }
year_input = int(input())
while year_input < 2000:
    year_input = year_input + 12
while year_input > 2011:
    year_input = year_input - 12
print(dic[year_input])
