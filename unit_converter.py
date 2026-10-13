def number():
    while True:
        try: return float(input("Enter value: "))
        except ValueError: print("Please enter a number.")
def main():
    while True:
        print("\n=== UNIT CONVERTER ===\n1.Length  2.Weight  3.Temperature  4.Time  5.Exit")
        category = input("Choose category: ").strip()
        if category == "5": print("Goodbye!"); break
        if category not in {"1", "2", "3", "4"}: print("Invalid choice."); continue
        if category == "1":
            print("1.Km to m  2.m to km  3.m to cm  4.cm to m  5.Miles to km")
            choice = input("Choose: ").strip(); v = number()
            options = {"1": (v*1000,"m"), "2":(v/1000,"km"), "3":(v*100,"cm"), "4":(v/100,"m"), "5":(v*1.609344,"km")}
        elif category == "2":
            print("1.Kg to g  2.g to kg  3.Kg to pounds  4.Pounds to kg")
            choice = input("Choose: ").strip(); v = number()
            options = {"1":(v*1000,"g"), "2":(v/1000,"kg"), "3":(v*2.20462262,"pounds"), "4":(v/2.20462262,"kg")}
        elif category == "3":
            print("1.Celsius to Fahrenheit  2.Fahrenheit to Celsius  3.Celsius to Kelvin")
            choice = input("Choose: ").strip(); v = number()
            options = {"1":(v*9/5+32,"°F"), "2":((v-32)*5/9,"°C"), "3":(v+273.15,"K")}
        else:
            print("1.Hours to minutes  2.Minutes to seconds  3.Seconds to minutes  4.Days to hours")
            choice = input("Choose: ").strip(); v = number()
            options = {"1":(v*60,"minutes"), "2":(v*60,"seconds"), "3":(v/60,"minutes"), "4":(v*24,"hours")}
        if choice in options: print(f"Result: {options[choice][0]:g} {options[choice][1]}")
        else: print("Invalid conversion choice.")
if __name__ == "__main__": main()
