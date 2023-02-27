from flask import Flask, render_template, request,send_file
import pandas as pd
from werkzeug.utils import secure_filename
from geopy.geocoders import ArcGIS
from prettytable import PrettyTable



app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('home.html')
	
@app.route('/success', methods = ['GET', 'POST'])
def uploaded():
   global your_file
   if request.method == 'POST':
      try:
          f = request.files['address']
          f.save(secure_filename(f.filename))
          
          your_file=f.filename
          df=pd.read_csv(f.filename)
          cols=df.columns
          location=None
          nom=ArcGIS()
          print(cols)
          for i in cols:
              if i.capitalize()=="Address":
                  location=i
                  break
      
          if type(location)==str:
              df["coordinate"]=df[location].apply(nom.geocode)
              df["latitude"]=df["coordinate"].apply(lambda x: x.latitude if x!=None else None)
              df["longitude"]=df["coordinate"].apply(lambda x: x.longitude if x!=None else None)
              df1=df.drop("coordinate",1)
              df1.to_csv("uploaded_"+f.filename)
              
              with open(f.filename, "r") as myfile:
                  myfile=myfile.readlines
                  with open(f.filename) as f:
                      content = f.readlines()
    
                      content = [x.strip() for x in content] 
              x=PrettyTable()
              for line in range (0,len(content)):
                  new_row=content[line].split(",")
                  x.add_row(new_row)
              html_code=x.get_html_string()
              with open("templates/latitude and longitude.html", "w") as file2:
                  file2.write(html_code)
                  
              #df1.to_html() is another solution     
                  
                      
              
               
              return render_template('download.html')
          else:    
              return render_template('home.html',text="Please select a CSV file with an Address as a column")
      except FileNotFoundError:
          return render_template('home.html',text="File not found.Try not selecting a folder.")
            
              
              
          
      
      
      
@app.route('/download')
def download():
    return send_file("uploaded_"+your_file,attachment_filename="your_file.csv",as_attachment=True)   
      
      
      
      
      
      
		
if __name__ == '__main__':
   app.run(debug = True)

