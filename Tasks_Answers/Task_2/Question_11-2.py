#Assignment 11
Amount_in_Naira = float(input("What is the amount in Naira(₦)?: "))
US_Dollars = float(input("What is the exchange rate of US Dollars($) in Naira?: "))
British_Pounds = float(input("What is the exchange rate of British Pounds(£) in Naira?: "))
Converted_US_Dollars = Amount_in_Naira / US_Dollars
Converted_British_Pounds = Amount_in_Naira / British_Pounds
Converted_US_Dollars_in_thousands = f"{Converted_US_Dollars:,}"
Converted_British_Pounds_in_thousands = f"{Converted_British_Pounds:,}"
print(f"Therefore,\nUS Dollars amount = ${Converted_US_Dollars_in_thousands}\nBritish Pounds amount = £{Converted_British_Pounds_in_thousands}")