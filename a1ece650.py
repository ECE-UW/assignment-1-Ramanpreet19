import math
import sys 

'''
a "Weber Street" (2,-1) (2,2) (5,5) (5,6) (3,8)
a "King Street S" (4,2) (4,8) 
a "Davenport Road" (1,4) (5,8)
g
'''
street   = []
st_name = [] #to save all the unique street names
#vertices = [] 
coords = {} #Dictionary of {street name:2-d Coordinates}
EDGES  = [] #list of all the edges 
V      = [] #Global list of vertices
V_DICT = {}
LINE_INERSECT = []
E      = [] #global list of all the edges 
E_FINAL = []

def print_dictionary(coords):
    print("############ Printing the global dictionary ############")
    for x in coords:
        print (x,':',coords[x])

def str_2_coord(str_n):
    str_lst = str_n.split(',')
    #print("\n~~~~~~~~~~~~ str_lst i,j = "+str_lst[0][1:]+" , "+str_lst[1][:-1])
    i = int(str_lst[0][1:])
    j = int(str_lst[1][:-1])
    return i,j
    
def coords_2_list(vertices):
    coords = []
    for j in range(0, len(vertices)):
        i_list, j_list = str_2_coord(vertices[j])
        coords.append([i_list, j_list])
        #print(vertices[j])
    return coords

def add_street(street_name, vertices):
    print("-----------------adding street to global Dictionary-------------------")
    coords[street_name] = coords_2_list(vertices)
    #print(coords)
    print("calling print_dictionary")
    print_dictionary(coords)
    
def remove_street(street_name):
    print("----------------Removing street name of global Dictionary---------------")
    if street_name in coords:
        print("Removing the street")
        del coords [street_name]
    else:
        sys.stderr.write("Error: Street not present in data base so can't remove it")
        #print("Error: Street not present in data base so can't remove it")
    print_dictionary(coords)
    
def change_street(street_name, vertices):
    print("----------------Changing street name of global Dictionary---------------")
    if street_name in coords:
        print("Changing data base of street")
        coords[street_name] = coords_2_list(vertices)
    else:
        sys.stderr.write("Error: Street not present in data base so can't change it")
    print_dictionary(coords)
'''   
def find_intersection_of_colinar_lines():
    print("Finding the intersection of colinear point")
'''   
def list_to_dict(v):
    v_dict = {}
    for i in range(0, len(v)):
        v_dict[i+1] = v[i]
    return v_dict

# function to get unique values 
def unique_list (list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
            
    return unique_list
        
def process_intersect_matrix():
    #find number of times line is appearing in the matrix 
    #create a new list [line1, line2, I1, I2 .... In]
    #print("*********Inside Process _intersect Matrix***********")
    #print("Matrix of intersection")
    #for i in range (0, len(LINE_INERSECT)):  
    #    print(LINE_INERSECT[i])
    
    list1 = []
    unique_list1 = []
    line_intersect_matrix = []
    #element = LINE_INERSECT[0][0]
    #print(element)
    
    for i in range(0, len(LINE_INERSECT)):
        element = LINE_INERSECT[i][0]
        list1.append(element)
        
    #print("printing list1", list1)
    unique_list1 = unique_list(list1)
    #print("printing unique_list", unique_list1)
    
    list_index = -1
    for i in range(0, len(unique_list1)):
        primary_key = unique_list1[i]
        init_count = 0
        for j in range(0, len(LINE_INERSECT)):
            if(primary_key == LINE_INERSECT[j][0]):
                #Check if line is already there in the list then add only intersection
                #Otherwise add line and intersection 
                #print("Primary Key Matched")
                if (init_count == 0):
                    #print("Adding the element for the first time to matrix")
                    line_intersect_matrix.append(LINE_INERSECT[j])
                    #print("***********Print intersect matrix************")
                    #print(line_intersect_matrix)
                    init_count = init_count + 1
                    list_index = list_index + 1 
                else:
                    #for k in range(0, len(line_intersect_matrix)):
                    #if (init_count == 1):
                        #if(primary_key == line_intersect_matrix[k]):
                    #print("Adding intersect to the matrix")
                    element = LINE_INERSECT[j][2]
                    line_intersect_matrix[list_index].append(element)
                    #print("***********Print intersect matrix************")
                    #for k in range (0, len(line_intersect_matrix)):
                    #    print(line_intersect_matrix[k])

                #print("****************************")

    #print("***********Print intersect matrix************")
    #for k in range (0, len(line_intersect_matrix)):
    #    print(line_intersect_matrix[k])
    #print("****************************")
    return line_intersect_matrix
                
def find_intersection(c1, c2, c3, c4):
    #print("In find intersection of 2 lines")
    
    x1, y1 = c1[0], c1[1]
    x2, y2 = c2[0], c2[1]
    p1, q1 = c3[0], c3[1]
    p2, q2 = c4[0], c4[1]
    
    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = p2 - p1
    dy2 = q2 - q1
    
    #print (x1, y1, x2, y2)
    #print (p1, q1, p2, q2)
    det = ((-dx1)*dy2) + (dy1*dx2)
    #print('det, math.fabs(det)= ', det, math.fabs(det))
    ##if determinet is less than 0.00000001 then lines are parallel
    if(math.fabs(det) < 0.00000001):
        #print("colinear points")
        #lines are parallel check if they are colinear 
        #check the slope of 2 lines 
        slope_d1 = y2 - y1 
        slope_n1 = x2 - x1
        
        slope_n2 = p1 - x1
        slope_d2 = q1 - y1
        
        '''
        if(slope_n1 == 0 and slope_n2 == 0):
            print("lines are colinear")
            find_intersection_of_colinar_lines()
        elif((slope_n2 != 0 and slope_n2  == 0) or (slope_n2 == 0 and slope_n1 != 0)):
            print("lines are not colinear")
        elif((slope_d1/slope_n1) == (slope_d2/slope_n2)):
            print("lines are colinear")
            find_intersection_of_colinar_lines()
        else:
            print("lines are not colinear")
        '''  
    else: 
        #find intersection
        det_inv = 1.0/det
        m1 = det_inv*((-dy2)*(p1-x1) + (dx2)*(q1-y1))
        m2 = det_inv*((-dy1)*(p1-x1) + (dx1)*(q1-y1))
        
        int_x = (x1 + m1*dx1 + p1 + m2*dx2)/2.0
        int_y = (y1 + m1*dy1 + q1 + m2*dy2)/2.0
        
        if((int_x>= min(x1,x2)) and (int_x <= max(x1,x2)) and (int_x >= min(p1,p2)) and (int_x <= max(p1,p2)) \
              and (int_y >= min(y1,y2)) and (int_y <= max(y1,y2)) and (int_y >= min(q1,q2)) and (int_y <= max(q1,q2))):
            #need to update vertices
            #print("intesection point is in range")
            
            #append all the points of intersecting lines
            #check if points exist in the List 
            if c1 not in V:
                V.append(c1)
            if c2 not in V:
                V.append(c2)
            if c3 not in V:
                V.append(c3)
            if c4 not in V:
                V.append(c4)
            if [int_x, int_y] not in V:
                V.append([int_x, int_y])
            
            #c5 = [int_x,int_y]
            LINE_INERSECT.append([c1, c2, [int_x, int_y]])
            LINE_INERSECT.append([c3, c4, [int_x, int_y]])
            #print("~~intesection point of line is", int_x, int_y)
         
    #process_intesect_matrix()
            
   

##############----------------------------    
#def get_line_points(point_list_2d):
##############----------------------------    
def find_vertices():
    streets_list = list(coords.keys())
    total_streets = len(streets_list)
    for i in range (0, (total_streets-1)):
        primary_key   = streets_list[i]
        for j in range (i + 1, (total_streets)):
            secondary_key = streets_list[j]
            primary_key_points   = coords[primary_key]   
            for k in range (0, len(primary_key_points) -1):
                c1 =  primary_key_points[k]
                c2 =  primary_key_points[k+1]
                #c1 c2 are primary_line points. Now for each of primary_line calculate all secondary lines
                secondary_key_points = coords[secondary_key]
                for l in range (0, len(secondary_key_points) -1):
                    c3 =  secondary_key_points[l]
                    c4 =  secondary_key_points[l+1]
                    #print(str('*')*50)
                    #print(c1, c2, c3, c4)
                    find_intersection(c1, c2, c3, c4)
                    
    #process_intesect_matrix()

def edges_for_multi_intersect_lines(unique_list1):
    length = len(unique_list1)
    distance_list = [];
    x1 = unique_list1[0][0]
    y1 = unique_list1[0][1]
    
    for i in range(2, len(unique_list1)):
        element = unique_list1[i]
        x2 = element[0]
        y2 = element[1]
        d  = (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)
        distance_list.append([d, x2, y2])
        #distance
    
    #print(distance_list)
    sorted_list = sorted(distance_list, key=lambda l:l[0])
    #print("**print sorted distance Matrix**")
    #print(sorted_list)
    
    #create edge to the first point 
    E.append([unique_list1[0], [sorted_list[0][1], sorted_list[0][2]]])
    for i in range(0, len(sorted_list) -1):
        E.append([[sorted_list[i][1], sorted_list[i][2]], [sorted_list[i+1][1], sorted_list[i+1][2]]])
    
    last_index = len(sorted_list) - 1
    p1 = unique_list1[1][0]
    q1 = unique_list1[1][1]
    E.append([[sorted_list[last_index][1], sorted_list[last_index][2]],[p1, q1]])
    
#find the multiple entries of vertices in the edge list E 
#E is global list of edges 
def find_edges(line_intersect_matrix):
    unique_list1 = []
    for i in range (0, len(line_intersect_matrix)):
        unique_list1 = unique_list(line_intersect_matrix[i])
        #print(unique_list1)
        if (len(unique_list1)> 3):
            #find order of the points and find edge 
            #print("line has more than one intersection")
            edges_for_multi_intersect_lines(unique_list1)
        else:
            #there are 3 points on the line so directly find the intersections
            E.append([unique_list1[0], unique_list1[2]])
            E.append([unique_list1[1], unique_list1[2]])

def are_points_equal(p1,p2):
    result = False
    if p1[0] == p2[0]:
        #print('step1')
        if p1[1] == p2[1]:
            #print('step2')
            result = True
    return result

def get_key_V(value):
    #print("inside get_keey_V...........")
    #for key, val_ in V_DICT.items():
    for i in range (0, len(V)):  
        #print('for...................key,val')
        if are_points_equal(V[i],value):
            #print('YESSSSSSSSSSSSS')
            return i+1

def proper_edges(E):
    for i in range(0,len(E)):
        k1 = get_key_V(E[i][0])
        k2 = get_key_V(E[i][1])
        E_FINAL.append([k1,k2])
    
    print('E=')
    print(E_FINAL)
        

def create_graph():
    #print("--------------- Create Graph ------------------")
    
    #find_vertices
    #add all the coords to V
    find_vertices()
    V_DICT = list_to_dict(V)
    print("Printing vertices")
    print("V=")
    print(V_DICT)
    
    #finding edges 
    #print("--------------Finding Edges--------------------")
    line_intersect_matrix = process_intersect_matrix()
    find_edges(line_intersect_matrix)
    print("\nPrinting Edges")
    #for i in range(0, len(E)):
    #    print(E[i])
    
    proper_edges(E)
        
def process_input_data():
    print('Add input about streets: ')
    #find_intersection([3,0], [4,0], [0,5], [0,6])
    #find_intersection([3,0], [-3,0], [0,5], [0,-5])
    street_temp = []
    while True:
        line = raw_input()
        if line:
            street_temp.append(line)
        else:
            break

    i = 0
    while i < len (street_temp):
        
        #check for correct code
        temp_line = street_temp[i]
        code = temp_line[0]
        temp_line = temp_line[1:]
        #check count("(") == count(")")
        if temp_line.count("(") != temp_line.count(")"):
            sys.stderr.write("Error: Incorrect input format")
            i+=1
            continue
        
        if code not in ['a', 'r', 'c', 'g']:
            sys.stderr.write("ERROR::Not a valid input")
            i=i+1
            continue
        
        #check for non-redundant street name
        if code in ['a','c','r']:
            st_name_temp = temp_line[temp_line.find("\"")+1:temp_line.rfind("\"")].lower()
            if ((st_name_temp=='') or (temp_line.count("\"") != 2)):
                sys.stderr.write("ERROR::Not a valid input")
                i=i+1
                continue
        
        if code=='a':
            if st_name_temp not in st_name:
                st_name.append(st_name_temp)
            else:
                sys.stderr.write("ERROR::redundant street name")
                i=i+1
                continue
        
        #check for coordinates properly given 
        if code in ['a','c']:
            st_coords = []
            temp_line = temp_line[temp_line.find("("):]
            while (temp_line.count(")") != 0):
                st_coord = temp_line[temp_line.find("(")+1:temp_line.find(")")].split(",")
                st_coord[0] = float(st_coord[0])
                st_coord[1] = float(st_coord[1])
                temp_line = temp_line[temp_line.find(")")+1:]
                st_coords.append(st_coord)
            
            if(code=='a'):
                coords[st_name_temp] = st_coords
            else:
                if st_name_temp not in st_name:
                    sys.stderr.write("Error: 'c' or 'r' specified for a street that does not exist.")
                else:
                    coords[st_name_temp] = st_coords
                    
        elif(code == 'r'):
            remove_street(st_name_temp)
            
        elif(code == 'g'):
            #print("Create Graph")
            if(len(st_name)<=0):
                sys.stderr.write("ERROR::Not a valid input.")
                sys.exit(0)
            else:
                create_graph()
            
        i += 1 
    '''        
        street.append(street_temp[i])
        street_name = st_name#st_info[1]
        print (st_info)
        #print (st_coord)
        j = 0
        vertices = []
        while j < len(st_coords):
            vertices.append(st_coords[j])
            j += 1
        
        #print(vertices)
     
        #coords[st_info[1]] = coords_2_list(vertices)
        if(street[i][0] == 'a'):
            add_street(street_name, vertices)
            #print("Adding a new street " + st_info[1])
            
        elif(street[i][0] == 'c'):
            change_street(street_name, vertices)
            #print("Changing values of street " + st_info[1])
            
        elif(street[i][0] == 'r'):
            remove_street(street_name)
            #print("Removing the specifications of the street" + st_info[1])
            
        elif(street[i][0] == 'g'):
            print("Create Graph")
            create_graph()
            
            
        else: 
            sys.stderr.write("ERROR::Not a valid input")
            #print('Error')
       '''

process_input_data()
#find_intersection([0,0], [5,0], [4,4], [4,-3])



