# problem 10

def bmi(weight, height):
    value = weight / height ** 2

    if value >= 30.0:
        print("This patient has obesity")
    elif value >= 25.0:
        print("This patient is overweight")
    elif value >= 18.5:
        print("This patient has a normal weight")
    else:
        print("This patient is underweight")

bmi(80, 1.73)

people = [[80, 1.73], [55, 1.58], [49, 1.91]]
list(map(lambda x: bmi(x[0], x[1]), people))
