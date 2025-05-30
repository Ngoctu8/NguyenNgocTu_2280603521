from SinhVien import Student

class QuanLySinhVien:
    listStudent = []
    def generateID(self):
        maxID = 1
        if (self.numberOfStudent() > 0):
            maxID = self.listStudent[0].id
            for s in self.listStudent:
                if (maxID < s.id):
                    maxID = s.id
            maxID = maxID + 1
        return maxID
    
    def numberOfStudent(self):
        return self.listStudent.__len__()
    
    def insertStudent(self):
        id = self.generateID()
        name = input("Nhap ten sinh vien: ")
        gender = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        averageScore = float(input("Nhap diem cua sinh vien: "))
        s = Student(id, name, gender, major, averageScore)
        self.academicRanking(s)
        self.listStudent.append(s)
    
    def updateStudent(self, ID):
        s:Student= self.findByID(ID)
        if(s != None):
            name = input("Nhap ten sinh vien: ")
            gender = input("Nhap gioi tinh cua sinh vien: ")
            major = input("Nhap chuyen nganh cua sinh vien: ")
            averageScore = float(input("Nhap diem cua sinh vien: "))
            s.name = name
            s.gender = gender
            s.major = major
            s. averageScore = averageScore
            self.academicRanking(s)
        else:
            print("Sinh vien co ID = {} khong ton tai.".format(ID))
    
    def sortByID(self):
        self.listStudent.sort(key=lambda x: x.id, reverse=False)
        
    def sortByName(self):
        self.listStudent.sort(key=lambda x: x.name, reverse=False)
        
    def sortByMajor(self):
        self.listStudent.sort(key=lambda x: x.major, reverse=False)
        
    def sortByAverageScore(self):
        self.listStudent.sort(key=lambda x: x.averageScore, reverse=False)
        
    def findByID(self, ID):
        searchResult = None
        if(self.numberOfStudent() > 0):
            for s in self.listStudent:
                if(s.id == ID):
                    searchResult = s
        return searchResult
    
    def findByName(self, keyword):
        listS = []
        if (self.numberOfStudent() > 0):
            for s in self.listStudent:
                if(keyword.upper() in s.name.upper()):
                    listS.append(s)
        return listS
    
    def deleteByID(self, ID):
        isDeleted = False
        s = self.findByID(ID)
        if(s != None):
            self.listStudent.remove(s)
            isDeleted = True
        return isDeleted
    
    def academicRanking(self, s:Student):
        if (s.averageScore >= 8):
            s.rank = "Gioi"
        elif (s.averageScore >= 6.5):
            s.rank = "Kha"
        elif (s.averageScore >= 5):
            s.rank = "Trung Binh"
        else:
            s.rank = "Yeu"
            
    def showStudent(self, listS):
        print("{:<8} {:<18} {:<8} {:<8}{:<18} {:<8}".format("ID", "Name", "Gender", "Major", "Average Score", "Rank"))
        if(listS.__len__() > 0):
            for s in listS:
                print("{:<8} {:<18} {:<8} {:<8}{:<18} {:<8}".format(s.id, s.name, s.gender, s.major, s.averageScore, s.rank))
        print("\n")
        
    def getListStudent(self):
        return self.listStudent         
            
            
        
    