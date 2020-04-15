import selenium, os, base64, time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def select(arg1, arg2):
	select_element = Select(driver.find_element_by_id(arg1))
	select_element.select_by_visible_text(arg2)

def change_entry(arg1, arg2, arg3, arg4):
	element = driver.find_element_by_id(arg1)
	element.send_keys(arg2)
	if arg4 is not None:
		if arg4 < 3:
			element.send_keys(bits)
		else:
			element.send_keys(no_bits)
	else:
		element.send_keys(arg3)



def get_image(file_num):
	#get and download image
	output = driver.find_element_by_id('output')
	# get the canvas as a PNG base64 string
	canvas_base64 = driver.execute_script('return arguments[0].toDataURL(\'image/png\').substring(21);', output)

	# decode
	canvas_png = base64.b64decode(canvas_base64)

	# save to a file
	with open(r'frame_' + file_num + '.png', 'wb') as f:
	    f.write(canvas_png)

backspace = '\b'
backspace_three = backspace*3
width = '1280'
height = '960'
preFormat = 'RGB32'
pixelFormat = 'BGRA'
bits = '12'
no_bits = '0'
pixelPlane = 'PackedYUV'

driver = webdriver.Chrome()
driver.get('https://rawpixels.net/')

change_entry('imageWidth', backspace_three, width, None)
change_entry('imageHeight', backspace_three, height, None)

select('formatSelect', preFormat)
select('pixelFormatSelect', pixelFormat)

for i in range(1, 5):
	arg1 = 'format.bpsp' + str(i) + 'Input'
	change_entry(arg1, backspace, height, i)

select('pixelPlaneSelect', pixelPlane)


for i in range(1, 100):
	i_str = str(i)
	curDir = os.getcwd()
	driver.implicitly_wait(10)
	driver.find_element_by_id('fileName').send_keys(curDir + '/frame-video8-' + i_str + '.raw')
	print("Getting frame: " + i_str)
	time.sleep(.5)
	get_image(i_str)


driver.quit()