from bangtal import *

scene1 = Scene('룸1', 'Images/배경-1.png')

door1 = Object('Images/문-오른쪽-닫힘.png')
door1.closed = True
door1.locate(scene1,800,270)
door1.show()

key = Object('Images/열쇠.png')
key.locate(scene1,600,150)
key.setScale(0.2)
key.show()

flowerPot = Object('Images/열쇠.png')
flowerPot.locate(scene1,550,150)
flowerPot.show()


scene2 = Scene('룸2', 'Images/배경-2.png')

door2 = Object('Images/문-오른쪽-닫힘.png')
door2.locate(scene2, 320, 270)
door2.show()

door3 = Object('Images/문-오른쪽-닫힘.png')
door3.locate(scene2, 910, 270)
door3.locked = True
door3.closed = True
door3.show()

keyPad = Object('Images/키패드.png')
keyPad.locate(scene2, 885, 420)
keyPad.show()

switch = Object('Images/스위치.png')
switch.locate(scene2, 880, 440)
switch.lighted = True
switch.show()

password = Object('Images/암호.png')
password.locate(scene2, 400, 100)



def door1_onMouseAction(x,y,action):
    if door1.closed:  #문이 닫혀있으면
       if key.inHand() == True:   #열쇠가 손에 있다면
           door1.setImage('Images/문-오른쪽-열림.png')  
           door1.closed = False  #문을 열어준다
       else:  #그렇지 않다면(열쇠가 손에 없다면)
           showMessage('잠겨있군, 열쇠가 필요하다.')  #메시지 출력
    else:  #그렇지 않다면 (문이 열려있으면)
        scene2.enter()  #룸2로 넘어간다


def key_onMouseAction(x,y,action):
    key.pick()


flowerPot.moved = False
def flowerPot_onMouseAction(x,y,action):
    if flowerPot.moved == False:
        if action == MouseAction.DRAG_LEFT:
            flowerPot.locate(scene1, 450, 150) 
            flowerPot.moved = True;
        elif action == MouseAction.DRAG_RIGHT:
            flowerPot.locate(scene1, 450, 150) 
            flowerPot.moved = True;


def door2_onMouseAction(x,y,action):
    scene1.enter()


def door3_onMouseAction(x,y,action):
    if door3.locked:
        showMessage('문이 잠겨있다.')
    elif door3.closed:  
       door1.setImage('Images/문-오른쪽-열림.png')  
       door1.closed = False 
    else:  
       endGame()  


def keyPad_onMouseAction(x,y,action):
    showKeypad('BANGTAL', door3)

def door3_onKeyPad():
    showMessage("철컥 소리가 났다. 문이 열린 모양이다.")
    door3.locked = False


def switch_onMouseAction(x,y,action):
    switch.lighted = not switch.lighted
    if switch.lighted:
        scene2.setLight(1)
        password.hide()
    else:
        scene2.setLight(0.25)
        password.show()



key.onMouseAction = key_onMouseAction
door1.onMouseAction = door1_onMouseAction
door2.onMouseAction = door2_onMouseAction
door3.onMouseAction = door3_onMouseAction
door3.onKeypad = door3_onKeyPad
flowerPot.onMouseAction = flowerPotflowerPot_onMouseAction
keyPad.onMouseAction = keyPad_onMouseAction
switch.onMouseAction = switch_onMouseAction

startGame(scene1)

