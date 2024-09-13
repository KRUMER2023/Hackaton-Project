# To track the changes
action_stack = []
redo_stack = []

def set_action(action):
    action_stack.append(action)
    
def get_action():
    return action_stack\
        
def set_redo(action):
    redo_stack.append(action)
    
def get_redo():
    return redo_stack

def pop_action():
    return action_stack.pop()

def pop_redu():
    return redo_stack.pop()