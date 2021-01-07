class Background:
    def __init__(self):
        self.__rows=35
        self.__columns=400
        self.__matrix=[]
        self.__back=[] #s=sky g=ground m=money b=beams p=power a=magnet d=bullet l=dragon c=mandalorian e=dragon_bullet
        self.__store=[]



            
    def create_matrix(self):
        for i in range(self.__rows):
            temp=[]
            temp1=[]
            for j in range(self.__columns):
                temp.append(' ')
                temp1.append(' ')
            self.__matrix.append(temp)
            self.__back.append(temp1)
            
    def create_store(self):
        for i in range(self.__rows):
            tempp=[]
            for j in range(self.__columns):
                tempp1=[]
                for k in range(3):
                    tempp1.append(' ')
                tempp.append(tempp1)
            self.__store.append(tempp)

    def printing_the_matrix(self,start):
        for i in range(self.__rows):
            for j in range(start,start+110):
                print(self.__matrix[i][j],end='')
            print()
            

    def get_matrix(self):
        return self.__matrix
    
    def set_matrix(self,xco,yco,val):
        self.__matrix[xco][yco]=val

    def get_back(self):
        return self.__back

    def get_store(self):
        return self.__store