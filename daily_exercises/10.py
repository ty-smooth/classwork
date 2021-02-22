# problem 10

def get_data():
    """Takes user input and extracts values

    Parameters
    ----------
    None

    Returns
    ----------
    (weight, height) : tuple
        Tuple of weight (int) and height (float)
    """

    raw_input = input("What is the person's weight in kilograms and height in meters? \
    (Please enter with a space like 80 1.73)  ")
    raw_values = raw_input.split(' ')
    weight = int(raw_values[0])
    height = float(raw_values[1])
    return (weight, height)

def bmi(weight, height):
    """Calculates BMI based on inputs

    Parameters
    ----------
    weight : int
        The weight in kilograms
    height : float
        The height in meters

    Returns
    ----------
    '' : str
        The BMI classification as a text value
    """

    value = weight / height ** 2
    if value >= 30.0:
        return "obese"
    elif value >= 25.0:
        return "over"
    elif value >= 18.5:
        return "normal"
    else:
        return "under"

def main():
    num_people = int(input('How many people are there? (Use a numeric value like 2 or 7) '))
    people_stats = [get_data() for i in range(num_people)]
    output_list = [bmi(i[0], i[1]) for i in people_stats]
    output_string = ' '.join(output_list)
    print(output_string)

if __name__ == "__main__":
    main()
