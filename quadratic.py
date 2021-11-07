import math

def input_float(prompt):
    while True:
        s = input(prompt)
        try:
            return float(s)
        except ValueError:
            print(f"{s} is not a number!")

print("Quadratic equation solver.")
print("Enter coefficients for ax²+bx+c = 0")
a = input_float("a: ")
b = input_float("b: ")
c = input_float("c: ")
print(f"{a}x²{b:+}x{c:+} = 0")

det = b**2-4*a*c
print(f"Determinant: det = b²-4ac = {det}")
if abs(det) < 1e-6:
    x = -b/2*a
    print("(x{:+})² = 0".format(-x))
    print(f"x = {x}")
elif det < 0:
    real = -b/(2*a)
    imag = abs(math.sqrt(-det)/(2*a))
    print(f"x₁,x₂ = {real}±{imag}i")
else:
    vdet = math.sqrt(det)
    x1 = (-b+vdet)/(2*a)
    x2 = (-b-vdet)/(2*a)
    print("(x{:+})(x{:+}) = 0".format(-x1, -x2))
    print(f"x₁ = {x1}; x₂ = {x2}")

# ax²+bx+c = 0
# (x+p)(x+q) = 0
# p = ?
# q = ?
# (x-x₁)(x-x₂) = 0