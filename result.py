def main():
    dollars = dollars_to_float(input("How much was the meal? ").rstrip())
    percent = percent_to_float(input("What percentage would you like to tip? ").rstrip())
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    x= d.strip()
    y=x.replace("$","")
    w=float(y)
    return(w)
    pass

def percent_to_float(p):
    x=p.strip()
    y=x.replace("%","")
    w=(float(y)/100) 
    return(w) 
    pass

main()
