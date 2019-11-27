import random
from action_classes import hunger, extra_hunger, full, half_full, weak, death
# from collections import defaultdict



class Ryan:
    action_dict = {'hunger':{'not_eat':0, 'eat_meat':0, 'eat_fruit':0, 'eat_poison':0},
                   'extra_hunger':{'not_eat':0, 'eat_meat':0, 'eat_fruit':0, 'eat_poison':0},
                   'full':{'step':0},
                   'half_full':{'not_eat':0, 'eat_meat':0, 'eat_fruit':0, 'eat_poison':0},
                   'weak':{'not_eat':0, 'eat_meat':0, 'eat_fruit':0, 'eat_poison':0},
                   'death':None
                   }
    
    def __init__(self):
        self.state = 'hunger'
        self.last_state = None
        self.last_action = None
        
    def get_state(self) -> str:
        return self.state
    
    def get_last_state(self):
        return self.last_state
    
    def change_state(self, state):
        self.last_state = self.state
        self.state = state
        
    def get_actions(self, state) -> [str]:
        return list(Ryan.action_dict[state].keys())
    
    def pick_action(self):
        return self.get_actions(self.get_state())[random.randint( 0, len( Ryan.action_dict[self.get_state()] )-1 )]
    
    def get_last_action(self):
        return self.last_action
    
    def exe_action(self, action):
        o = eval( str(self.get_state()) + "()" )
        self.change_state( eval( "o.exe_" + str(action) + "()" ) )
        self.last_action = action
        
        self._reward_points()
        
        
    def _reward_points(self):
        if self.get_state() == 'hunger':
            Ryan.action_dict[self.get_last_state()][self.get_last_action()] += -0.25
        elif self.get_state() == 'extra_hunger':
            Ryan.action_dict[self.get_last_state()][self.get_last_action()] += -0.25
        elif self.get_state() == 'full':
            Ryan.action_dict[self.get_last_state()][self.get_last_action()] += 1
        elif self.get_state() == 'half_full':
            Ryan.action_dict[self.get_last_state()][self.get_last_action()] += 0.5
        elif self.get_state() == 'weak':
            Ryan.action_dict[self.get_last_state()][self.get_last_action()] += -0.5
        elif self.get_state() == 'death':
            Ryan.action_dict[self.get_last_state()][self.get_last_action()] += -1
            
            

    def get_viable_actions(self, options:[str]) -> set():
        '''options: ['meat', 'fruit', 'poison']'''
        viable_actions = set()
        if self.get_state() != 'full':
            viable_actions.add('not_eat')
            for o in options:
                viable_actions.add("eat_" + str(o))
        else:
            viable_actions.add('step')    
        return viable_actions
         
    def pick_best_action(self, viable_actions) -> str:
        return max( [ (action, Ryan.action_dict[self.get_state()][action]) for action in viable_actions ], key=lambda x:x[1] )[0]
    
        
        
        
class Plant:
    
    def __init__(self, poison=False):
        self.poison = poison
        self.color = self.get_color()
        
    def get_color(self):
        return 'red' if self.poison else 'blue'
        
       
 
 

# r = Ryan()
#  
# counter = 0
# 
# for i in range(10):
#     counter = 0
#     r.change_state('hunger')
#     print("LIFE #", i+1, "-------------------")
#     while r.get_state() != 'death':
#         counter += 1
#        
#         options = input("options:").split(",")
#         b_action = r.pick_best_action(r.get_viable_actions(options))
#         r.exe_action(b_action)
#         print(r.get_last_state(), r.get_last_action(), r.get_state(), counter)
#          
#     print("alive for:", counter, "days")
#     print()
#     for k,v in Ryan.action_dict.items():
#         print(k,v)
 
#meat,poison,fruit 
       
def train(r):
    for i in range(100):
        while r.get_state() != 'death':
            r.exe_action(r.pick_action())  
        r.change_state('hunger')
             
ALL_OPTIONS = ['meat','fruit','poison']           
             
r = Ryan()
  
for i in range(100):
    while r.get_state() != 'death':
        r.exe_action(r.pick_action())       
    r.change_state('hunger')
      
      
print()
for k,v in Ryan.action_dict.items():
    print(k,v)
  
print()
options = ['poison', 'poison', 'fruit']
print( r.pick_best_action(r.get_viable_actions(options)) )
 
print()
options = ['meat', 'poison', 'fruit']
print( r.pick_best_action(r.get_viable_actions(options)) )
 
print()
counter = 0
while r.get_state() != 'death':
     
    options = []
    for i in range(random.randint(1,5)):
        options.append(random.choice(ALL_OPTIONS))
    b_action = r.pick_best_action(r.get_viable_actions(options))
    r.exe_action(b_action)
    print(r.get_last_state(), r.get_last_action(), r.get_state(), counter)
     
    counter += 1
  
    

# if __name__ == '__main__':
#     print('\ndriver testing with batch_self_check:')
#     import driver
#     driver.default_file_name = "bsc1.txt"
#     driver.driver()   
    
    

    
