from flask import Flask, render_template

@app.route('/inicio') 
def inicio():
    return render_template("index.html")
    
    
if __name__ == '__main__':
    app.run(debug=True)


