from cvxopt import solvers, matrix

P = 2 * matrix([[10., 2.], [2., 1.]])
q = matrix([-10., -25.])
G = matrix([[1., -1., -1., 0.], [2., -1., 0., -1.]])
h = matrix([10., -9., 0., 0.])

solvers.options['show_progress'] = False
sol = solvers.qp(P, q, G, h)['x']
print("Solution: {0:5.2f}, {1:5.2f}".format(sol[0], sol[1]))
