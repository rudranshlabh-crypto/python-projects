mport math

angle_degrees = 45

angle_radians = math.radians(angle_degrees)

sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)
tan_value = math.tan(angle_radians)

sin_rounded = round(sin_value, 4)
cos_rounded = round(cos_value, 4)
tan_rounded = round(tan_value, 4)

print("Trigonometric values for", angle_degrees, "degrees:")
print("Sin:", sin_rounded)
print("Cos:", cos_rounded)
print("Tan:", tan_rounded)