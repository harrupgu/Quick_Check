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

sample='G1C400'

good_list=[]
bad_list=[]
# Define callback functions for the arrow keys
def on_left_arrow(event):
    if event.event_type == 'down':
        print('No: ',card)
        bad_list.append(card)
        sys.stdout.flush()
        keyboard.unhook_all()
        pyautogui.hotkey('alt', 'f4')


def on_right_arrow(event):
    if event.event_type == 'down':
        print('Yes',card)
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
    keyboard.on_press_key('left', on_left_arrow)
    keyboard.on_press_key('right', on_right_arrow)

    # Wait for the user to press an arrow key or escape key
    while True:
        
        if keyboard.is_pressed('left'):
            image.close()
            break
        elif keyboard.is_pressed('right'):
            image.close()
            break
        elif keyboard.is_pressed('esc'):
            image.close()
            break

    # Close the image
    #image.close()
# name of the CSV file to save
savename = '%s_good_pores.csv'%(sample)
savenameb = '%s_bad_pores.csv'%(sample)

# open the CSV file in write mode
with open(savename, 'w', newline='') as csv_file:

    # create a CSV writer object
    writer = csv.writer(csv_file)

    # write each row of data to the CSV file
    for row in good_list:
        writer.writerow([row])

print(f"CSV file {savename} saved successfully!")

with open(savenameb, 'w', newline='') as csv_file:

    # create a CSV writer object
    writer = csv.writer(csv_file)

    # write each row of data to the CSV file
    for row in bad_list:
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
