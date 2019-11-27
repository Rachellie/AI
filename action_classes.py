# class hunger:
#     def __init__(self):
#         pass
#         
#     def exe_not_eat(self) -> str:
#         return 'extra_hunger'
#     
#     def exe_eat_meat(self) -> str:
#         return 'full'
#     
#     def exe_eat_fruit(self) -> str:
#         return 'half_full'
#     
#     def exe_eat_poison(self) -> str:
#         return 'weak'
#     
# 
# class extra_hunger:
#     def __init__(self):
#         pass
#         
#     def exe_not_eat(self) -> str:
#         return 'weak'
#     
#     def exe_eat_meat(self) -> str:
#         return 'full'
#     
#     def exe_eat_fruit(self) -> str:
#         return 'half_full'
#     
#     def exe_eat_poison(self) -> str:
#         return 'death'
#     
#     
# class full:
#     def __init__(self):
#         pass
#         
#     def exe_step(self) -> str:
#         return 'hunger'
#     
#     
# class half_full:
#     def __init__(self):
#         pass
#         
#     def exe_not_eat(self) -> str:
#         return 'hunger'
#     
#     def exe_eat_meat(self) -> str:
#         return 'full'
#     
#     def exe_eat_fruit(self) -> str:
#         return 'full'
#     
#     def exe_eat_poison(self) -> str:
#         return 'weak'
#     
#     
# class weak:
#     def __init__(self):
#         pass
#         
#     def exe_not_eat(self) -> str:
#         return 'death'
#     
#     def exe_eat_meat(self) -> str:
#         return 'full'
#     
#     def exe_eat_fruit(self) -> str:
#         return 'weak'
#     
#     def exe_eat_poison(self) -> str:
#         return 'death'
#     
#     
# class death:
#     def __init__(self):
#         pass



class hunger:
    def __init__(self):
        pass
        
    def exe_not_eat(self) -> str:
        return 'extra_hunger'
    
    def exe_eat_meat(self) -> str:
        return 'full'
    
    def exe_eat_fruit(self) -> str:
        return 'half_full'
    
    def exe_eat_poison(self) -> str:
        return 'weak'
    

class extra_hunger:
    def __init__(self):
        pass
        
    def exe_not_eat(self) -> str:
        return 'weak'
    
    def exe_eat_meat(self) -> str:
        return 'full'
    
    def exe_eat_fruit(self) -> str:
        return 'half_full'
    
    def exe_eat_poison(self) -> str:
        return 'death'
    
    
class full:
    def __init__(self):
        pass
        
    def exe_step(self) -> str:
        return 'hunger'
    
    
class half_full:
    def __init__(self):
        pass
        
    def exe_not_eat(self) -> str:
        return 'hunger'
    
    def exe_eat_meat(self) -> str:
        return 'full'
    
    def exe_eat_fruit(self) -> str:
        return 'full'
    
    def exe_eat_poison(self) -> str:
        return 'weak'
    
    
class weak:
    def __init__(self):
        pass
        
    def exe_not_eat(self) -> str:
        return 'death'
    
    def exe_eat_meat(self) -> str:
        return 'full'
    
    def exe_eat_fruit(self) -> str:
        return 'weak'
    
    def exe_eat_poison(self) -> str:
        return 'death'
    
    
class death:
    def __init__(self):
        pass