class Head():
    def __init__(self,eyes, nose, mouth, ears):
        self.eyes = eyes 
        self.nose = nose
        self.mouth = mouth
        self.ears = ears


class Arm():
    def __init__(self, hand,side):
        self.hand = hand
        self.side = side

class Hand():
    def __init__(self,fingers):
        self.fingers = fingers


class Leg():
    def __init__(self,foot,side):
        self.foot = foot
        self.side =side

class Foot():
    def __init__(self, toes):
        self.toes = toes
        

class Torso():
    def __init__(self, head, left_arm, right_arm, left_leg, right_leg):
        self.head = head 
        self.left_arm = left_arm 
        self.right_arm = right_arm 
        self.left_leg = left_leg
        self.right_leg = right_leg


class Human():
    def __init__(self, torso, name):
        self.torso = torso
        self.name = name
    
    def show_traits(self):
        print(f"""A new human has been created with {self.torso.head.eyes} eyes, {self.torso.head.nose} nose, {self.torso.head.mouth} mouth and {self.torso.head.ears} ears in his head.
He has a {self.torso.left_arm.side} arm with {self.torso.left_arm.hand.fingers} finger is his hand
and a {self.torso.right_arm.side} arm with {self.torso.right_arm.hand.fingers} finger in that hand.
He also has a {self.torso.left_leg.side} and a {self.torso.right_leg.side} leg with {self.torso.left_leg.foot.toes + self.torso.right_leg.foot.toes} toes in his feet.
His name is {self.name}""")
        
new_head = Head(2,1,1,2)
lef_hand = Hand(5)
left_arm = Arm(lef_hand,"left")
right_hand = Hand(5)
right_arm = Arm(lef_hand,"right")
lef_foot = Foot(5)
left_leg = Leg(lef_foot,"left")
right_foot = Foot(5)
right_leg = Leg(lef_foot,"right")
new_torso = Torso(new_head,left_arm,right_arm,left_leg,right_leg)
new_human = Human(new_torso, "The Fiend")

new_human.show_traits()

#named {self.name}