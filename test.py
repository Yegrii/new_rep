class VideoItem:
    def __init__(self, title, descr, path):
        self.title, self.descr, self.path = title, descr, path
        self.rating = VideoRating()
    
class VideoRating:
    def __init__(self, num=0):
        self.rating = num

        
    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self, num):
        if 0 <= num <= 5:
            self.__rating = num
        else:
            raise ValueError('неверное присваиваемое значение')
v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
rating = VideoRating()

print(v.rating.rating) # 0
v.rating.rating = 5
print(v.rating.rating) # 5
title = v.title
descr = v.descr
#change 1
#change 2