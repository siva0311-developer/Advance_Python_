# decoration:-

# 1st method
'''
def parent():
    def start():
        print("Enter the First......!")
        process()
        finish()
    start()    
def process():
    print("processing")

def finish():
    print("finishing.....")


parent()
'''

def parent(fun):
    def start():
        print("Enter the First......!")
        fun()
        finish()
    return start

@parent

def process():
    print("processing")

def finish():
    print("finishing.....")


process()
