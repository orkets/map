

def calculate_map(systolic, diastolic):
    """
    Calculate Mean Arterial Pressure (MAP) using systolic and diastolic blood pressure readings.
    Formula: MAP = ((2 * diastolic) + systolic) / 3
    """
    map_value = ((2 * diastolic) + systolic) / 3
    return map_value

def get_blood_pressure():
    """
    Get systolic and diastolic blood pressure readings from the user.
    """
    systolic = float(input("Enter systolic blood pressure (mmHg): "))
    diastolic = float(input("Enter diastolic blood pressure (mmHg): "))
    return systolic, diastolic

def main():
    print("Mean Arterial Pressure (MAP) Calculator")
    systolic, diastolic = get_blood_pressure()
    map_value = calculate_map(systolic, diastolic)
    print(f"Mean Arterial Pressure (MAP): {map_value:.2f} mmHg")

if __name__ == "__main__":
    main()
