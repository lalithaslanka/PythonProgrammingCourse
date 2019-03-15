'''
A graph consists of vertices and edges that connect vertices. Write a program
that reads a graph from a file and displays it on a panel. The first line in
the file contains a number that indicates the number of vertices (n). The
vertices are labeled as 0, 1, ..., n-1. Each subsequent line, with the
format u x y v1, v2, ..., describes that the vertex u is located at
position (x, y) with the edges (u, v1), (u, v2), and so on. Figure a
gives an example of the file for a graph. Your program prompts the user
to enter the name of the file, reads data from the file, and displays the
graph on a panel, as shown in Figure b.
'''
from tkinter import *
import os
 #Vertex class to save all the properties of a vertex
class Vertex:
    def __init__(self,data_list):
        print(data_list)
        self.vertex_no = data_list[0]
        self.x_coordinate = int(data_list[1])
        self.y_coordinate = int(data_list[2])
        self.vertices_connected = data_list[3:]
        print(" self.vertices_connected ", self.vertices_connected[-1])
fname = "file.txt"

if os.path.exists(fname):
    print("File found")
else:
    raise Exception("The file doesn't exist. Copy the file.txt in the current directory")

infile = open(fname,'r')
file_contents = infile.readlines()
# The first element is the  number of vertices
no_of_vertices = int(file_contents[0][0])
print(no_of_vertices)
del file_contents[0]
#print(file_contents[0])
vertices_list = []
for i in range(0,no_of_vertices):
    vertices_list.append(Vertex(file_contents[i].split(" ")))
    
infile.close()

#Draw a conavas and create the vertices
#Create a window

window = Tk()
window.title("Display a graph")

#create a canvas
w = Canvas(window, width = 500, height = 500)
w.pack()
for i in range(0,no_of_vertices):
    w.create_text(vertices_list[i].x_coordinate-5,
                  vertices_list[i].y_coordinate-5,
                  text = vertices_list[i].vertex_no)
    w.create_oval(vertices_list[i].x_coordinate,
                  vertices_list[i].y_coordinate,
                  vertices_list[i].x_coordinate,
                  vertices_list[i].y_coordinate,
                  fill = 'black', width = 4)
    #Draw the lines from the vertices, as mentioned in the file
    print("len(vertices_list[i].vertices_connected) ", len(vertices_list[i].vertices_connected))
    for j in range(0,len(vertices_list[i].vertices_connected)): #loop that iterates the connected vertices
        pointA= vertices_list[i]
        for num, vertices in enumerate(vertices_list, start=0): #loop to go thru all the vertices to match the connected vertex
            print("vertices_list[i].vertices_connected[j]=",vertices_list[i].vertices_connected[j],
                  "vertices_list[num].vertex_no=", vertices_list[num].vertex_no)
            if(vertices_list[i].vertices_connected[j] == vertices_list[num].vertex_no):
                pointB = vertices_list[num]
                w.create_line(pointA.x_coordinate,pointA.y_coordinate,
                              pointB.x_coordinate,pointB.y_coordinate)
                print(pointA.vertex_no, pointB.vertex_no)
    








    
    

        
    
    


