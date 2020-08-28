temp_in_c = float(input("Enter temperature in celsius: "))

#(0°C × 9/5) + 32 from Google
temp_in_f = (temp_in_c *9/5) + 32
temp_in_f = str(temp_in_f)
temp_in_c = str(temp_in_c)
print(temp_in_c + "° in Celsius is equivelant to " + temp_in_f + " ° in Fahrenheit.")