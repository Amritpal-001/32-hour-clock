from flask import Flask

import time
app = Flask(__name__)

@app.route('/')
def homepage():

    TimeAtStart = datetime.now(timezone('Asia/Kolkata'))
    seconds = int( TimeAtStart.strftime(" %S " ) )
    minutes = int ( TimeAtStart.strftime(" %M " ) )
    hours =   int ( TimeAtStart.strftime(" %H " ) )

    #Getting initial values of time
    x = seconds +  ( minutes* 60 ) + ( hours * 3600)    # x = total of seconds passed.
    hora = int(x / 2700)                        #b is our new hour , = hora(spanish)
    minuto = int (  (x - hora * 2700)/54  )    #a is new minute , minuto (spanish)
    zen =  x - minuto * 54 - hora * 2700       #zen is our new second

    #continuing clock from there
    while True:
        zen = zen + 1
        time.sleep(0.99)
        if zen == 45:
            zen = 0
            minuto = minuto + 1
        if minuto == 60:
            minuto = 0 
            hora = hora + 1
        if hora == 32:
            hora = 0
    
    return """
    <h1>32 hours clock </h1>
    <p>.       </p>
    <p> {hora} : {minuto} : {zen}</p>
    
    """.format(hora = hora , minuto = minuto , zen = zen)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
