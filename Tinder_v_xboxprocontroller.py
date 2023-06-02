# -*- coding: utf-8 -*-
"""
Created on Thu May 11 17:08:17 2023

@author: HARRUPGU
"""

from PIL import Image
import sys
import keyboard
import pyautogui
import csv
import pygame


sample='G1C400'

# Initialize the xbox controller

pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Check for connected controllers
if pygame.joystick.get_count() == 0:
    print("No controller detected.")
    pygame.quit()
    # exit()

# Get the first controller
controller = pygame.joystick.Joystick(0)
controller.init()
print("Controller connected:", controller.get_name())

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                print("A button pressed")
            elif event.button == 1:
                print("B button pressed")
        elif event.type == pygame.JOYBUTTONUP:
            if event.button == 0:
                print("A button released")
            elif event.button == 1:
                print("B button released")


good_list=[]
# Define callback functions for the arrow keys
def on_a_button(event):
    if event.event_type == 'down':
        print('No')
        sys.stdout.flush()
        keyboard.unhook_all()
        pyautogui.hotkey('alt', 'f4')


def on_b_button(event):
    if event.event_type == 'down':
        print('Yes')
        good_list.append(card)
        sys.stdout.flush()
        keyboard.unhook_all()
        pyautogui.hotkey('alt', 'f4')

# Display and get input for 10 images
for card in range(1, 30):
    # Load the image
    filename='cards/Card_pore%04d.png'%(card)
    print(filename)
    image = Image.open(filename)
    image.show()

    # Hook the arrow key events
    keyboard.on_press_key('left', on_a_button)
    keyboard.on_press_key('right', on_b_button)

    # Wait for the user to press an arrow key or escape key
    while True:
        if keyboard.is_pressed('left'):
            #print(card)
            break
        elif keyboard.is_pressed('right'):
            image.close()
            break
        elif keyboard.is_pressed('esc'):
            image.close()
            break

    # Close the image
    image.close()
# name of the CSV file to save
savename = '%s_good_pores.csv'%(sample)

# open the CSV file in write mode
with open(savename, 'w', newline='') as csv_file:

    # create a CSV writer object
    writer = csv.writer(csv_file)

    # write each row of data to the CSV file
    for row in good_list:
        writer.writerow([row])

print(f"CSV file {savename} saved successfully!")


 #                               --::;;,,.
 #                  .,;;<!!!!!!!!;;;. `''!!!!;;.
 #               ;!!!!!!!!!!!!!!!!!!>;,.  `'!!!!!;.
 #            ;!!!!!!!!!!!!!!!!!!!!!!!!!!;;.- ``!!!!;
 #           <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>;.`'!!!>,
 #          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!;;
 #         ;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!;.
 #         !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!.
 #        ;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 #        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>
 #        !`!!!!!!!!!!!!''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>
 #        !'!!!!!!!!!!' ;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!`!
 #         :!!!!!!!!! ''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! !!!!!! /
 #        :!!!!!!!!!>';!!!!!!!!!!!!!!!!!!!!!!!!`;!!!!!!!' !!!!'
 #       :!!!!!!!!!' <!!!!!!!!!!!!!!!!!!!!!!!` !!!!''`.  !!'  .:!!
 #     :!!!!!!!!!! :!!!!!!!!!!!!!!!!!!!!''`.  '`..ee$"  ,,=   `)!!
 #    <!!!!!!!(`    !!!!!;,'``````` .,,=="""zd$$$$$$"$P"    ". <!!!
 #   !!!!!!!!!!!!! !!'!!!!! d$$$$$PF"",    /"??$$$$$ $,L,,zed$r <!!>
 #  !!!!!!!!!!!!!! `! ` !!! $$$$$$c, ??    "Lze$$$$$.?$$$$$$$$$. !!!!
 # `!!!!!!!!!!!!!!> `': !!!>`$$$$$$$$$$$$$$$$$$$$$$$$."$$$$$$$$$ `!!!!
 # `!!!!!!!!!!!!!!!!. !!!!!! "$$$$$$$$$$$$$$$$$$$$$$$$b."$$$$$$$  !!!!>
 #  <!!!!!!!!!!!!!!!!!!!!!!!! "$$$$$$$$$$$$$$$$$$$P?)$$$$ $$$$$F ;!!!!>
 #   <!!!!!!!!!!!!!!!!!!!!!!!! `$$$$$$$$$$$$$$$$$"$P?)CP",$$$$$  !!!!!
 #    <!!!`!!!!!!!!!!!!!!!!!!!> 3$$$$$$$$$$$$$$$$bc,$$$$$$$$$$F !!!!!
 #   ; `'! `!!!!!!!!!!!!!!!!!!!  $$$$$$$$$$$$$$$$$$P".,;;; $$$ :!!!'
 #   `!;.   `'!!;`!!!!!!!!!!!!!  $$$$$$$$$$$$$$$$",'``  .; ?$F !!!
 #    <!!!;.': `' `!!!!!!!!!!!! J$$$$$$$$$$$$$$$ '::;;;;;'.d$F !!
 #     `!!!!!!!!;. `!!!'!!!!!! .$$$$$$$$$$$$$$$$$$c,..,,c$$$$" `!>
 #      `!!!!!!!!!> <!! !!!!!! d$$$$$$$$$$$$$$$$$$$$$$$$$$$$P
 #       `!!!!!!!!!> `!>`!!!!! $$$$$$C?$$$$$$$$$$$$$$$$$$$$"
 #          `<!!!!!!!:.`  `!!! $$$$$$$$$ee.."""???$$$PFF"".,;;;,.
 #            ` `!!!!!!!!:.`'! ?$$$$$`$$$$$$$$$eeec. :--:;;;;;;;;;;;;;.
 #               `!!!!!!!!!!:.  ?$$$$$.?$$$$$$$$$$$P ;;;;;;;,.`':;;;;;;;;,
 #                 '`'<!!!!!!! be$$$$$$c"$$$$$$$$$$F ;;;;;;;;;;;;;;;;;;;;;
 #                 ,`:;,.`'!!> $$$$$$$$$b`$$$$$$$$$F :;;;;;;;;;;;;;;:'''`
 #                 ;;,`';;;,   $$$$$$$$$$$`$$$$$$$$b  ``':;;;;;;;'`
 #                ':;;;, `;;;;;.`"?$$$$$$$$$$$$$$$$$ `$ec.`:;;;' ;;;
 #                ' ;;;;; `;;;;;;;, "?$$$$$$$$$$$$$$L 3$$$$c`:  ;;;;:;;;;;.
 #                 `;'`;;;.`;;;;;;;;;:. "$$$$$$$$$$$$e ?$$C.ec `:;;;:';;;;;;
 #                  `;;:  .;;;;;;'` .,.'  `?$$$$$$$$$$$.P.$$$$$c.``'' ';;;;;
 #                ;'.''; ;;;;;'  :;;;;;;;;;.`?$$$$??$$P".$$$$$$$$$$cc, ;;;;;
 #              .;;;; ,.`` ` .:   `':;;;;;;;;, ?$$$$$$$$$$$$$$$$$$$$$',;;;;'
 #          .;;;;;;',;;;;;;;;;;;;.`<,.`':;;;;;;.`?$$$$$$$$$$$$$$$$$$P ;;;;;
 #       ;;;;;;;;'.;;;;;;;;;;;;;;;;.`':;;,``':;;; "?$$$$$$$$$$$$$$$$" ;;;;'
 #    ;;;;;;;;;'.;;;;;;;;;;;;;;;;;;;;; `:;;;:.`:;;;.`?$$$$$$$$$$$$$P ;;;;' ;
