def q6():
    fahrenheit = [32, 68, 104, 212, 50]  # Example temperatures
    celsius = []

    for f in fahrenheit:
        celsius.append((f - 32) * 5 / 9)

    print(celsius)
