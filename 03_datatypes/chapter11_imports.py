import arrow as arrow

print(arrow.now())
print(arrow.get(16250772800).format('YYYY-MM-DD HH:mm:ss'))

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)
print(p)  # Output: Point(x=10, y=20)
print(p[0], p[1])
