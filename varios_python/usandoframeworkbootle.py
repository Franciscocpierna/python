from bottle import route, run, template, static_file

#@route('/static/<filename>') # rota achar arquivos estaticos
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./views/static')
    
    

@route('/')
@route('/hello/<name>')
def hello(name='Stranger'):
   #return template('Hello {{name}}, how are you?', name=name)
   return template("index")

run(host='localhost', port=8080, debug=True)

#https://bottlepy.org/docs/dev/tutorial.html#generating-content
#http://localhost:8080/
#http://localhost:8080/hello/ola