def convert_temperature(value, unit):
    if unit.lower() == 'c':
        return (value * 9/5) + 32, 'F'
    elif unit.lower() == 'f':
        return (value - 32) * 5/9, 'C'
    else:
        return None, 'Invalid unit'

# Example
temp, unit = convert_temperature(100, 'C')
print(f"Converted temperature: {temp:.2f}°{unit}")
