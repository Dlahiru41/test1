#------important libraries
import random
import time
import sys

def createGrid():#-----------main function
    userInput = input(str("> : "))#----takes the user input
    if (userInput[0:4] == 'perc' or userInput[0:4] == 'Perc'):#----check whether there is the necessary command
        if (len(userInput) == 4):#-----checks the length of the user input
            #-----the default grid will be creates 
            gridRows = 5
            gridCols = 5
            gridArray = [[0 for x in range(gridCols)] for y in range(gridRows)]
            for gR in range(gridRows):
                for gC in range(gridCols):
                    gridArray[gR][gC] = random.randint(10,99)#----assign random number to the array
            emptySpacesCount = gridRows
            
            for a in range (emptySpacesCount):
                emptyRow = random.randint(0, gridRows-1)
                emptyCol= random.randint(0, gridCols-1)
                gridArray[emptyRow][emptyCol] = '  '
                
            for gR2 in range(gridRows):
                for gC2 in range(gridCols):
                    print(gridArray[gR2][gC2], end='  ')
                print()
                
            resultArray = ['OK' for z in range(gridCols)]
            
            for gR3 in range(gridRows):
                for gC3 in range(gridCols):
                    if (gridArray[gR3][gC3] == '  '):
                        resultArray[gC3] = 'NO'
                        
            for result in range(gridCols):
                print(resultArray[result], end='  ')
            print('\n')
            #--------------------------------
            #-----FILE HANDLING-------
            t,s = str(time.time()).split('.')
            filename = t+".txt"#-----creates an unique name for the file
            print ("writing to", filename)

            stdoutOrigin=sys.stdout
            sys.stdout=open(filename,"a")
            
            
            for gR2 in range(gridRows):
                for gC2 in range(gridCols):
                    print(gridArray[gR2][gC2], end='  ')
                print()
            for result in range(gridCols):
                print(resultArray[result], end='  ')
            
            print('\n')
            sys.stdout.close()
            sys.stdout=stdoutOrigin
            #-----------------------------------
            #-------HTML TABLE---------
            gridArray.append(resultArray)
            result_string = """<HTML>
            <style>
            table, th, td {
              border: 1px solid black;
              border-collapse: collapse;
            }
            </style>
            <body>
                <table>\n"""
            for gR2 in range(gridRows+1):
                result_string += "        <tr>\n            "
                for gC2 in range(gridCols):
                    result_string += "<td>%s</td>" %gridArray[gR2][gC2]
                result_string += "\n        </tr>\n"
            result_string += """    </table>                       
            
            </body>
            </HTML>"""
            display = open("table.html", 'w')
            display.write(result_string)
            display.close()

            
        else:#------exectues only if the user gives values
            try:
                gridRows = int(userInput[5])#-----checks the first number(No of rows)
                try:
                    gridCols = int(userInput[7])#-----checks the second number(No of columns)
                    if ((3<=gridRows<=9) and (3<=gridCols<=9)):#------range validation
                        gridArray = [[0 for x in range(gridCols)] for y in range(gridRows)]
                        for gR in range(gridRows):
                            for gC in range(gridCols):
                                gridArray[gR][gC] = random.randint(10,99)#--------assigns random number 
                        emptySpacesCount = gridRows
                        for a in range (emptySpacesCount):
                            emptyRow = random.randint(0, gridRows-1)
                            emptyCol= random.randint(0, gridCols-1)#-------randomly select an index
                            gridArray[emptyRow][emptyCol] = '  '

                        for gR2 in range(gridRows):
                            for gC2 in range(gridCols):
                                print(gridArray[gR2][gC2], end='\t')
                            print()
                        resultArray = ['OK' for z in range(gridCols)]
                        
                        for gR3 in range(gridRows):
                            for gC3 in range(gridCols):
                                if (gridArray[gR3][gC3] == '  '):
                                    resultArray[gC3] = 'NO'

                        for result in range(gridCols):
                            print(resultArray[result], end='\t')
                        
                        print('\n')
                        #--------------------------------
                        #------FILE HANDLING----------
                        gridArray.append(resultArray)
                        t,s = str(time.time()).split('.')
                        filename = t+".txt"#-----creats an unique name for the file 
                        print ("writing to", filename)

                        stdoutOrigin=sys.stdout
                        sys.stdout=open(filename,"a")
                        
                        
                        for gR2 in range(gridRows+1):
                            for gC2 in range(gridCols):
                                print(gridArray[gR2][gC2], end='\t')
                            print('\n')

                        sys.stdout.close()
                        sys.stdout=stdoutOrigin
                        #-----------------------------------
                        #----HTML TABLE------
                        #gridArray.append(resultArray)
                        result_string = """<HTML>
                        <style>
                        table, th, td {
                          border: 1px solid black;
                          border-collapse: collapse;
                        }
                        </style>
                        <body>
                            <table>\n"""
                        for gR2 in range(gridRows+1):
                            result_string += "        <tr>\n            "
                            for gC2 in range(gridCols):
                                result_string += "<td>%s</td>" %gridArray[gR2][gC2]
                            result_string += "\n        </tr>\n"
                        result_string += """    </table>                       
                        
                        </body>
                        </HTML>"""
                        display = open("table.html", 'w')
                        display.write(result_string)
                        display.close()

                    else:
                        print('The grids should be in between 3x3 and 9x9.')
                except TypeError:
                    print("The grids can only be created with integer values.")
            except ValueError:
                print("The grids can only be created with integer values.")
        
    else:
        print('Invalid Input. Your Input should start with "perc".')



createGrid()
