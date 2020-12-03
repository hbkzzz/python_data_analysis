class Greet :
    def __init__(self, human) :
        self.human = human

    def hello(self, msg) :
        print(msg)

    def hi(self, msg) :
        print(f'''{self.human} : {msg}''')

# main()
print('민주 => 안녕하세요')
print('Jane => Hello')
human = 'Sara'
say = '안녕!'
print(f'''{human} => {say}''')

human1 = '장동건'
say1 = '반갑습니다.'
print(f'''{human1} => {say1}''')

# Greet 객체이용
jain = Greet('제인')
jain.hello('안녕하세요')
jain.hi('안녕')
