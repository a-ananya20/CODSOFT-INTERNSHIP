def calculate_bmi(weight, height):
    """Calculate the BMI given weight in kg and height in meters."""
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    """Classify the BMI value into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")

    try:
        # Prompt for weight and height
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        # Calculate BMI and get classification
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        # Display result
        print(f"\nYour BMI is: {bmi}")
        print(f"BMI Category: {category}")
    except ValueError:
        print("Invalid input. Please enter numerical values for weight and height.")

if __name__ == "__main__":
    main()
