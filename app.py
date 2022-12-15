from flask import Flask,request,render_template,redirect,flash,session
from flask_debugtoolbar import DebugToolbarExtension
from forms import addPetForm, editPetForm
from models import db,connect_db, Pet

app = Flask(__name__)
app.app_context().push()



app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]= False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']= True
app.config['SECRET_KEY']= 'bensaba'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
debug= DebugToolbarExtension(app)
connect_db(app)
db.create_all()



@app.route('/')
def show_all():
    pets=Pet.query.all()
    return render_template("all_pets.html",pets=pets)

@app.route("/add",methods=["GET","POST"])
def add_pet():
    form=addPetForm()
    if form.validate_on_submit():
        name=form.name.data
        species=form.species.data
        photo_url=form.photo_url.data
        age=form.age.data
        notes=form.notes.data
        available=form.available.data
        new_pet=Pet(name=name,species=species,photo_url=photo_url,age=age,notes=notes,available=available)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    
    else:
        return render_template("add_pet_form.html",form=form)


@app.route('/<int:id>',methods=["GET","POST"])
def edit_data(id):
    pet = Pet.query.get_or_404(id)
    form = editPetForm(obj=pet)
    if form.validate_on_submit():
        photo_url=form.photo_url.data
        age=form.age.data
        notes=form.notes.data
        pet.photo_url=photo_url
        pet.age=age
        pet.notes=notes
        db.session.commit()
        return redirect('/')


    return render_template ("edit_form.html",pet=pet,form=form)
