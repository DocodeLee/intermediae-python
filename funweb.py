import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fect():
    
    clear() #clear the above screen
    
    put_html("<p align=""left""><h2><img src=""https://\
                media.geeksforgeeks.org/wp-content/uploads/\
                    20210720224119/MessagingHappyicon.png"" width =""7%""> \
                        Fun Fact Generator </h2></p>")
    # URL from where we will fetch the data 
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    response = requests.request("GEt",url)
    data = json.loads(response.text)
    useless_fact = data['text']
    
    style(put_text(useless_fact), 'color:blue; font-size: 30px')
    put_button(
        [dict(label = "Click Me", value = "outline-success",
              color = 'outline-success')], onclick=get_fun_fect)
    
if __name__ == '__main__':
    put_html("<p align=""left""><h2><img src=""https://media.geeksforgeeks.org/wp-content/uploads/20210720224119\MessagingHappyicon.png"" width=""7%"">Fun Fact Generator</h2></p>")
    
    put_button(
        [dict(label='Click Me', value ='outline-success',
              color = 'outline-success')],onclick=get_fun_fect)
hold()