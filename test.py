class VideoItem:
    def __init__(self, title, descr, rate):
        self.title, self.descr = title, descr
        self.rating = VideoRating(rate).rating
    
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
v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 4)
print(v.__dict__)