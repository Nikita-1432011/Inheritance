class bird :

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")
        
    def swim(self):
        print("swim faster")

    
class parrot(bird):
    def __init__(self):
        super.__init__()
        print("Parrot is ready")

    def whoisthis(self):
        print("parrot")

    def run(self):
        print("Run faster")

paro = parrot()
paro.whoisthis()
paro.swim()
paro.run()
        
        