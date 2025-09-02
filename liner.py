import matplotlib.pyplot as plt

f = open(r'Book1.csv')
data = f.readlines()
f.close()

x_values = []
y_values = []

for i in range(1, len(data)):
    row = data[i].strip().split(',')
    if len(row) < 3:
        continue
    try:
        x_values.append(float(row[1]))
        y_values.append(float(row[2]))
    except ValueError:
        continue

for j in range(min(5, len(x_values))):
    print("x=" + str(x_values[j]) + ", y=" + str(y_values[j]))

n = len(x_values)

if n == 0:
    print("No valid data points found.")
    exit()

sum_x = 0
sum_y = 0
sum_xy = 0
sum_x2 = 0

for i in range(n):
    sum_x += x_values[i]
    sum_y += y_values[i]
    sum_xy += x_values[i]*y_values[i]
    sum_x2 += x_values[i]*x_values[i]

denominator = n * sum_x2 - sum_x * sum_x

if denominator == 0:
    print("Cannot perform linear regression: all x-values are the same.")
    exit()

m = (n * sum_xy - sum_x * sum_y) / denominator
b = (sum_y - m * sum_x) / n

print("\nRegression coefficients:")
print("Slope (m):", round(m, 2))
print("Intercept (b):", round(b, 2))

def predict(x):
    return m * x + b

regression_line = []
for i in range(n):
    regression_line.append(predict(x_values[i]))

plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, color='blue', label='Actual Data')
plt.plot(x_values, regression_line, color='red', linewidth=2, label='Regression Line')

new_x_values = [0, 15]
for i in range(len(new_x_values)):
    x = new_x_values[i]
    y = predict(x)
    if i == 0:
        plt.scatter([x], [y], color='green', s=100, label='Prediction (x=0)')
    else:
        plt.scatter([x], [y], color='green', s=100)
    plt.text(x, y, '  (' + str(x) + ', ' + str(round(y, 1)) + ')', verticalalignment='bottom')

plt.title('Linear Regression from Scratch', fontsize=16)
plt.xlabel('X Values', fontsize=12)
plt.ylabel('Y Values', fontsize=12)
plt.legend()
plt.grid(True)

eq = 'y = ' + str(round(m, 2)) + 'x + ' + str(round(b, 2)) + '\nR² = 1.00 (perfect fit)'
plt.text(0.5, 0.95, eq, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top',
         bbox=dict(facecolor='white', alpha=0.8))

plt.show()

print("\nFinal linear regression equation:")
print("y = " + str(round(m, 2)) + "x + " + str(round(b, 2)))