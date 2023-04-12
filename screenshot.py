from datetime import datetime
import pyautogui


now = datetime.now()
txtdate = now.strftime('%d%m%Y_%H%M%S')
myScreenshot = pyautogui.screenshot()
myScreenshot.save(r"C:\Users\vdx7607\Vale S.A\NL - Team Workspace - Data Center - Data Center\Screenshot\screenshot_" + txtdate + ".png")