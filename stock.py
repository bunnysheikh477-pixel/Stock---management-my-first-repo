# Stock---management-my-first-repo
A simple stock management system for learning Git and GitHub . A stock management system to add, update and track products in inventory .  

##Features
-Adding
-Updating
-Deleting
-Watching product list 



import json,os
stock_list=[]

from flask import Flask,render_template,request,redirect,url_for


# Data load and save functions


def load_S(path="Stock_list.json"):
    if not os.path.exists(path):
        return []
    with open(path,"r",encoding="utf-8") as f:
        return json.loads(f.read()or"[]")
    

def save_S(path="Stock_list.json"):
    with open(path,"w",encoding="utf-8") as f:
        json.dump(stock_list,f,indent=2)






app=Flask(__name__)
@app.route("/")
def index():
  return render_template("Stock.html")



@app.route("/add",methods=["POST"])
def add_p():
    pro_N=request.form.get("Name").upper().strip()
    pro_Q=int(request.form.get("Quantity"))
    E_Price=float(request.form.get("Price"))
    
    new_P={
        'pro_N':pro_N,
        'pro_Q':pro_Q,
        'E_Price':E_Price,
        'done':False
        } 
    
    stock_list.append(new_P)
    save_S()
    # return redirect(url_for(""))
    return render_template("Stock.html")
    


            
            
@app.route("/delete/<int:pro_N>")            
def delete(pro_N):
    global stock_list
    for i,p in enumerate(stock_list):
        if p["pro_N"]==pro_N:
            del stock_list[i]
            save_S()
            break
 
    return render_template("Stock.html")

            
@app.route("/sell",methods=["POST"]) 
def sell(stock_list,pro_N,pro_Q):
  product_to_sell=None
  for product in stock_list:
      if product['pro_N']==pro_N:
          product_to_sell=product
          break
  if product_to_sell is None:
     print(f"\n'{pro_N} is not found in the stock list:")
     return 
  if product_to_sell['pro_Q']<pro_Q:
      print(f"Not enough {pro_N} in stock. Available: {product_to_sell['pro_Q']}")
      return 
  product_to_sell['pro_Q']-=pro_Q
  save_S()
  total_p=product_to_sell["E_Price"]*pro_Q
  print(f"\n  ITEM SOLD . \nItem quantity = {pro_Q}.\nItem name = {pro_N}.\nTotal price = Rs.{total_p}.\nRemaining stock: {product_to_sell['pro_Q']}")  
  return render_template("Stock.html")
        
   
   
   
   
   
if __name__=="__main__":
    load_S()
    app.run(debug=True)             
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
