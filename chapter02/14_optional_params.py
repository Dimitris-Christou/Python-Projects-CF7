def get_fromatted_date(day: int = 1, month: int = 1, year:int = 2000) -> str:
    """
    Return a string representing a date in the format 'dd/mm/yyyy'
    
    Args:
        day (int) : The day of the month. Default to 1.
        month (int) : The month of the year. Defaults to 1.
        year (int) : The year. Defaults to 2000.

    Returns:
        str: The formatted date string. 
    """
    return f"{day:02d}/{month:02d}/{year:04d}"


def main():
    print(get_fromatted_date())     #01/01/2000
    print(get_fromatted_date(10))   #10/01/2000
    print(get_fromatted_date(14,2))     #14/02/2000
    print(get_fromatted_date(14,2,2025))    #14/02/2025

    print(get_fromatted_date(year = 2025))  #01/01/2025
    print(get_fromatted_date(year = 2020, day = 19, month = 4)) #19/04/2020

if __name__ == "__main__":
    main()
