#importacion del framework
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

#Inicializacion del APP
app = Flask (__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbsoftsit_pii'
app.secret_key='mysecrety'
mysql= MySQL(app)

#Declaracion de ruta http://localhost:5000
@app.route('/')
def index():
  return render_template('index.html')

#rura http:localhost:5000/guardar tipo POST para insert
@app.route('/GUARDAR', methods=['POST'])
def GUARDAR(): 
  if request.method == 'POST':

    # pasamos a variables el contenido de los input
    Vnombre=request.form['txtNombre']
    Vape_p=request.form['txtApe_p']
    Vape_m=request.form['txtApe_m']
    Vmuni=request.form['txtMunicipio']
    Vedo=request.form['txtEstado']
    Vcol=request.form['txtColonia']
    Vcalle=request.form['txtCalle']
    Vdirec=request.form['txtDireccion']

    #Conectar y ejecutar el insert
    cs= mysql.connection.cursor()
    cs.execute('insert into pefundas (Nombre, Ape_p, Ape_m, Municipio, Estado, Colonia, Calle, Direccion) values(%s,%s,%s,%s,%s,%s,%s,%s)',(Vnombre,Vape_p,Vape_m,Vmuni,Vedo,Vcol,Vcalle,Vdirec))
    mysql.connection.commit()

  flash('La información fue agregado correctamente')
  return redirect(url_for('index'))

  
#Ejecucion del servidor en el puerto 5000

if __name__ == '__main__':
        app.run(port=5000,debug=True)
