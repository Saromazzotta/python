day = 1
month = 1
year = 1994

# typecasting
year_end = int(str(year)[-2:])
year_end_mod = year % 100  # modulus

def find_day_of_week(year_end_mod):
    num1 = year_end_mod + year_end_mod % 4
    num2 = num1 + year_end_mod
    print(num1)
    print(num2)


find_day_of_week(year_end_mod)
