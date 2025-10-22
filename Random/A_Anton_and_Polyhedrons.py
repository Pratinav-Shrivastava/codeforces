# t = int(input())
# total = 0
# for i in range(t):
#     polygon = input()
#     if polygon == "Tetrahedron":
#         total += 4
#     elif polygon == "Cube":
#         total += 6
#     elif polygon == "Octahedron":
#         total += 8
#     elif polygon == "Dodecahedron":
#         total += 12
#     elif polygon == "Icosahedron":
#         total += 20
# print(total)

vals = {
	'Tetrahedron': 4,
	'Cube': 6,
	'Octahedron': 8,
	'Dodecahedron': 12,
	'Icosahedron': 20
}

n = int(input())
ans = 0
for i in range(n):
	ans += vals[input()]
print(ans)