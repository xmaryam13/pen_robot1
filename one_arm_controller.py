from controller import Robot, Keyboard 

bot = Robot()
keyboard = Keyboard()
timestep = 64

shoulder_lift = bot.getDevice("shoulder_lift_joint")
shoulder_pan = bot.getDevice("shoulder_pan_joint")
elbow = bot.getDevice("elbow_joint")
wrist_1 = bot.getDevice("wrist_1_joint")
wrist_2 = bot.getDevice("wrist_2_joint")
wrist_3 = bot.getDevice("wrist_3_joint")

keyboard.enable(timestep)

def move_bot(a=0,b=0,c=0,d=0,e=0,f=0):
    shoulder_lift.setPosition(a)
    shoulder_pan.setPosition(b)
    elbow.setPosition(c)
    wrist_1.setPosition(d)
    wrist_2.setPosition(e)
    wrist_3.setPosition(f)
    
move_bot()

shoulder_lift_pos = 0
shoulder_pan_pos = 0 
elbow_pos = 0 
wrist_1_pos = 0 
wrist_2_pos = 0 
wrist_3_pos = 0 

while bot.step(timestep) != -1:
    keypressed = keyboard.getKey()
    print(keypressed)
    if keypressed == 317:
        shoulder_lift_pos += 0.01
    elif keypressed == 315:
        shoulder_lift_pos -= 0.01
    elif keypressed == 314:
        shoulder_pan_pos += 0.01
    elif keypressed == 316:
        shoulder_pan_pos -= 0.01
    elif keypressed == 87:
        elbow_pos -= 0.01
    elif keypressed == 83:
        elbow_pos += 0.01
    elif keypressed == 65:
        wrist_1_pos += 0.01
    elif keypressed == 68:
        wrist_1_pos -= 0.01
    elif keypressed == 49:
        wrist_2_pos += 0.01
    elif keypressed == 50:
        wrist_2_pos -= 0.01
    elif keypressed == 51:
        wrist_3_pos += 0.01
    elif keypressed == 52:
        wrist_3_pos -= 0.01
    
    move_bot(shoulder_lift_pos,shoulder_pan_pos,elbow_pos,wrist_1_pos,wrist_2_pos,wrist_3_pos)
    
        


    