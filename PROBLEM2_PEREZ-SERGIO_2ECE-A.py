#MACHINE PROBLEM 2, 2ECE-A , GROUP 3 : PEREZ, PIOLO -  SERGIO, RICHARD

#input value of 3 Xs separated by 'space'  x1,x2,x3 
x = [int(x) for x in input("Enter multiple x value: ").split()] 
print("Number of list is: ", x)  

#input value of 3 Y's separated by 'space' y1,y2,y3
y = [int(y) for y in input("Enter multiple y value: ").split()] 
print("Number of list is: ", y) 

#solving for D,E,F from the equation so we can use formula for center of the circle and to find the radius

D = (((x[0]**2 - x[2]**2) * (x[0]-x[1]) + (y[0]**2 - y[2]**2) * 
          (x[0]-x[1]) + (x[1]**2 - x[0]**2) * (x[0]-x[2]) + 
          (y[1]**2 - y[0]**2) * (x[0]-x[2])) // (2 * ((y[2]-y[0]) * (x[0]-x[1]) - (y[1]-y[0]) * (x[0]-x[2])))); 
          
E = (((x[0]**2 - x[2]**2) * (y[0]-y[1]) + (y[0]**2 - y[2]**2) * (y[0]-y[1]) + 
          (x[1]**2 - x[0]**2) * (y[0]-y[2]) + (x[1]**2 - x[0]**2) * (y[0]-y[2])) // 
          (2 * ((x[2]-x[0]) * (y[0]-y[1]) - (x[1]-x[0]) * (y[0]-y[2]))));
          
F = (-x[0]**2 - y[0]**2 - 2 * E * x[0] - 2 * D * y[0]) 

#finding the center of the circle
h = -E
k = -D

#radius of the circle
r = round(sqrt(h**2 + k**2), 5)

#print final output of values
print("The Center of the circle: (", h, ", ", k, ")");  
print("Radius of the Circle: ", r);
print("Vectors: ","D:",D,"E:",E,"F:",F)