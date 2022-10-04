def get_led():
    led_string = """
  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###"""
      
    lines = led_string.split("\n")[1:]
    led = {
        '1':[],
        '2':[],
        '3':[],
        '4':[],
        '5':[],
        '6':[],
        '7':[],
        '8':[],
        '9':[],
        '0':[],
    }

    for line in lines:
        for i,v in enumerate(led.keys()):
            led[v].append(line[4*i:4*i+3])
    return led
    
def turnon(num,led):
    num = list(num)
    for line in range(5):
        line_string = ""
        for n in num:
            line_string += led[n][line]+" "
        print(line_string)
        
if __name__ == "__main__":
    led = get_led()
    turnon("123",led)
