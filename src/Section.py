# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import OpenGL.GL as gl

class Section:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color1' not in self.parameters:
            self.parameters['color1'] = [0.5, 0.5, 0.5]  
        if 'color2' not in self.parameters:
            self.parameters['color2'] = [0.2, 0.2, 0.2]  
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False             
            
        # Objects list
        self.objects = []

        # Generates the wall from parameters
        self.generate()   
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self     

    # Defines the vertices and faces 
    def generate(self):
        self.vertices = [ 
                [0, 0, 0 ], 
                [0, 0, self.parameters['height']], 
                [self.parameters['width'], 0, self.parameters['height']],
                [self.parameters['width'], 0, 0],
                [0, self.parameters['thickness'], 0 ], 
                [0, self.parameters['thickness'], self.parameters['height']], 
                [self.parameters['width'], self.parameters['thickness'], self.parameters['height']],
                [self.parameters['width'], self.parameters['thickness'], 0],
                ]
        self.faces = [
                [0, 3, 2, 1],
                [4, 7, 6, 5],
                [3, 7, 6, 2],
                [0, 4, 5, 1],
                [1, 2, 6, 5],
                [0, 3, 7, 4]
                ]   

    # Checks if the opening can be created for the object x
    def canCreateOpening(self, x):
        # A compléter en remplaçant pass par votre code
        pass      
        
    # Creates the new sections for the object x
    def createNewSections(self, x):
        # A compléter en remplaçant pass par votre code
        pass              
        
    # Draws the edges
    def drawEdges(self):
    
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_LINE)

        gl.glBegin(gl.GL_LINES)

        gl.glColor3fv(self.parameters['color2'])
        gl.glVertex3fv(self.vertices[0])
        gl.glVertex3fv(self.vertices[1])
           
        gl.glColor3fv(self.parameters['color2'])
        gl.glVertex3fv(self.vertices[1])
        gl.glVertex3fv(self.vertices[2]) 
         
        gl.glColor3fv(self.parameters['color2'])
        gl.glVertex3fv(self.vertices[2])
        gl.glVertex3fv(self.vertices[3]) 
           
        gl.glColor3fv(self.parameters['color2'])
        gl.glVertex3fv(self.vertices[3])
        gl.glVertex3fv(self.vertices[0]) 
           
        gl.glColor3fv(self.parameters['color2'])
        gl.glVertex3fv(self.vertices[5])
        gl.glVertex3fv(self.vertices[6]) 
           
        gl.glColor3fv(self.parameters['color2'])
        gl.glVertex3fv(self.vertices[6])
        gl.glVertex3fv(self.vertices[7]) 
           
        gl.glColor3fv(self.parameters['color2'])
        gl.glVertex3fv(self.vertices[7])
        gl.glVertex3fv(self.vertices[4]) 
           
        gl.glColor3fv(self.parameters['color2'])
        gl.glVertex3fv(self.vertices[4])
        gl.glVertex3fv(self.vertices[5]) 
           
        gl.glColor3fv(self.parameters['color2'])
        gl.glVertex3fv(self.vertices[1])
        gl.glVertex3fv(self.vertices[5]) 
           
        gl.glColor3fv(self.parameters['color2'])
        gl.glVertex3fv(self.vertices[2])    
        gl.glVertex3fv(self.vertices[6]) 
           
        gl.glColor3fv(self.parameters['color2'])
        gl.glVertex3fv(self.vertices[3])
        gl.glVertex3fv(self.vertices[7]) 
           
        gl.glColor3fv(self.parameters['color2'])
        gl.glVertex3fv(self.vertices[0])
        gl.glVertex3fv(self.vertices[4]) 
         
        gl.glEnd() 
        
        
                 
    # Draws the faces
    
    def draw(self):
        
        gl.glPushMatrix()
        gl.glTranslate(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])
        gl.glRotate(self.parameters['orientation'],0,0,1)
        
        if self.parameters['edges']:
            self.drawEdges()
        
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK,gl.GL_FILL)
        gl.glBegin(gl.GL_QUADS)
        gl.glColor3fv(self.parameters['color1'])
        
        for face in self.faces:
            for i in range (0,4):
                gl.glVertex3fv(self.vertices[face[i]]) 
                
        gl.glEnd() 
        
        
        gl.glPopMatrix()