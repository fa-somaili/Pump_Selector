#Pump Product Selection Assistant! its fictional tho, ofc :D

print("PUMP PRODUCT SELECTION ASSISTANT")
print("Welcome:D")
print("This project will help you find pumps based on your requirements.> fictional ones ofc ofc :D")


#pump catalogue

pumps = [
    {
        "id": "P001",
        "name": "Pump Alpha",
        "flow_rate": 10.0,
        "head": 15.0
    },
    {
        "id": "P002",
        "name": "Pump Beta",
        "flow_rate": 20.0,
        "head": 25.0
    },
    {
        "id": "P003",
        "name": "Pump Gamma",
        "flow_rate": 8.0,
        "head": 12.0
    },
    {
        "id": "P004",
        "name": "Pump Delta",
        "flow_rate": 15.0,
        "head": 20.0
    },
    {
        "id": "P005",
        "name": "Pump Epsilon",
        "flow_rate": 5.0,
        "head": 8.0
    }
]

print(f"\nCatalogue loaded: {len(pumps)} pumps.")

# Ask u for the requirements

print("\nLet's find a pump for you :D")

while True:
    try:
        required_flow = float(input("Enter your flow rate (m3/h): "))
        required_head = float(input("Enter your pump head (m): "))
        
        if required_flow <= 0 or required_head <= 0:
            print("GREATER THEN ZERO MAN >:!!")
        else:
            break  
            
    except ValueError:
        print("NUMBERS ONLY >:!!!")

print("\nYour requirements:")
print(f"Flow rate: {required_flow} m3/h")
print(f"Pump head: {required_head} m")
print("\ngive me a sec I'm looking man...")



# Find pumps that meet both requirements

matching_pumps = []

for pump in pumps:
    if (
        pump["flow_rate"] >= required_flow
        and pump["head"] >= required_head
    ):
        matching_pumps.append(pump)



matching_pumps.sort(key=lambda pump: pump["flow_rate"])
print("\n— Matching Pumps:D —")
print(f"Found {len(matching_pumps)} matching pump(s)")

if matching_pumps:
    print("these ones will be a good fit: ")
    for pump in matching_pumps:
        print(
            f"{pump['id']} - {pump['name']}: "
            f"Flow {pump['flow_rate']} m3/h, "
            f"Head {pump['head']} m"
        )
else:
    print("No pumps match both requirements :b")

#



