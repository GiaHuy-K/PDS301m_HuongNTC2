# Unpacking a dictionary is a little bit more complicated but has an interesting application for functions. It does
# require that the dictionary use the variable names expected by the function. One advantage of this is in providing
# inputs in a different order:
# Since functions allow inputs to be provided in a different order by including their variable names, such as
# dist(x1=0, x2=1, y1=5, y2=5) working with the defined function where they are expected in a different
# order:
# def dist(x1,y1,x2,y2):
