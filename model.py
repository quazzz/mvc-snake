import random

class Snake:
    def __init__(self):
        # snakes body has 3 parts and initializing
        self.body = [(5,5),(4,5),(3,5)]
        # and by init it goes to the right
        self.direction = (1, 0)
        
    def move(self):
        # head is always the first element
        head = self.body[0]
        # adding new values to head so if head was at (5,0) and dir is (1,0) (to right) then new head pos is (6,0)
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        # adding new head to the removed tail body (:-1 removes last elem)
        self.body = [new_head] + self.body[:-1]
        
    def grow(self):
        # duplicate last segment from snakes body
        self.body.append(self.body[-1])
        
    def change_dir(self, new_dir):
        # check if plr wants to new dir to be exactly opposite to the cur dir
        if(new_dir[0] == -self.direction[0] and new_dir[1] == -self.direction[1]):
            return
        self.direction = new_dir
        
    def collide_self(self):
        # if snake head pos is equal to other segment pos then return boolean val
        return self.body[0] in self.body[1:]
    
    def collide_wall(self, size):
        # getting heads cords
        x,y = self.body[0]
        # checking whether cords are too small or big
        return not (0 <= x < size and 0 <= y < size)
    
class Food:
    def __init__(self, size):
        self.grid_size = size
        self.pos = (0,0)
        self.relocate([])
        
    def relocate(self, body):
        while True:
            # getting random pos
            pos = (random.randint(0, self.grid_size - 1), random.randrange(0, self.grid_size - 1))
            # checking if new fruit position is the same to some of snakes body position
            if pos not in body:
                self.pos = pos
                break