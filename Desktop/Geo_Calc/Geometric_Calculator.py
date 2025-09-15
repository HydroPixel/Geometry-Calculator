import tkinter as tk #Hey there! This is My first ever biggest project! Its a simple GeoCalculstor! Thank you!
import math

root = tk.Tk()
root.attributes("-fullscreen", True)
root.config(bg="#00ff99")

menu = tk.Frame(root)
cre = tk.Frame(root)
sec_d = tk.Frame(root)
thrd_d = tk.Frame(root)

sq = tk.Frame(root)
sq_a = tk.Frame(root)
sq_per = tk.Frame(root)

rec = tk.Frame(root)
rec_a = tk.Frame(root)
rec_per = tk.Frame(root)

tri = tk.Frame(root)
tri_a = tk.Frame(root)
tri_per = tk.Frame(root)

cir = tk.Frame(root)
cir_a = tk.Frame(root)
cir_cum = tk.Frame(root)

para = tk.Frame(root)
para_a = tk.Frame(root)
para_per = tk.Frame(root)

trap = tk.Frame(root)
trap_a = tk.Frame(root)
trap_per = tk.Frame(root)

cube = tk.Frame(root)

cuboid = tk.Frame(root)

sphere = tk.Frame(root)

cyl = tk.Frame(root)

cu_tsa = tk.Frame(root)
cu_lsa = tk.Frame(root)
cu_op = tk.Frame(root)

cuboi_tsa = tk.Frame(root)
cuboi_lsa = tk.Frame(root)
cuboi_op = tk.Frame(root)

cy_tsa = tk.Frame(root)
cy_csa = tk.Frame(root)
cy_op = tk.Frame(root)

sph_tsa = tk.Frame(root)

cu_v = tk.Frame(root)
cuboi_v = tk.Frame(root)
sph_v = tk.Frame(root)
cy_v = tk.Frame(root)

for frames in (
    menu,
    cre,
    sec_d,
    thrd_d,
    sq,
    sq_a,
    sq_per,
    rec,
    rec_a,
    rec_per,
    tri,
    tri_a,
    tri_per,
    para,
    para_a,
    para_per,
    trap,
    trap_a,
    trap_per,
    cir,
    cir_a,
    cir_cum,
    cube,
    cu_lsa,
    cu_op,
    cu_tsa,
    cu_v,
    cuboid,
    cuboi_tsa,
    cuboi_lsa,
    cuboi_op,
    cuboi_v,
    sphere,
    sph_v,
    cyl,
    cy_tsa,
    cy_csa,
    cy_op,
    cy_v,
    sph_tsa
):
    frames.place(relheight = 1, relwidth = 1)

def sf(frames):
    frames.tkraise()

#---MENU---
tk.Button(menu, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: root.destroy()).pack(padx=5, pady=5, anchor="nw")
tk.Label(menu, text="Shape Calculator PRO", font=("Cooper Black", 50)).pack(pady=80)
tk.Button(menu, text="2D Shapes", font=("Helvetica", 30), bg="#E1FF00", fg="Black", activebackground="Black", activeforeground="White", command=lambda: sf(sec_d)).pack(pady=5)
tk.Button(menu, text="3D Shapes", font=("Helvetica", 30), bg="#E1FF00", fg="Black", activebackground="Black", activeforeground="White", command=lambda: sf(thrd_d)).pack(pady=5)
tk.Button(menu, text="   Credits   ", font=("Helvetica", 30), bg="#E1FF00", fg="Black", activebackground="Black", activeforeground="White", command=lambda: sf(cre)).pack(pady=5)
tk.Button(menu, text="     Quit     ", font=("Helvetica", 30), bg="#E1FF00", fg="Black", activebackground="Black", activeforeground="White", command=lambda: root.destroy()).pack(pady=5)

#---CREDITS---
tk.Button(cre, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(menu)).pack(padx=5, pady=5, anchor="nw")
tk.Label(cre, text="Made By:\nAliasgar\nBaji\nOR\nHydroPixel", font=("Cooper Black", 50)).pack(pady=120, anchor="center")

#---2D_SHAPE---
tk.Button(sec_d, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(menu)).pack(padx=5, pady=5, anchor="nw")
tk.Label(sec_d, text="Choose a shape:", font=("Cooper Black", 50)).pack(pady=70)
tk.Button(sec_d, text="Square", font=("Cascadia Code", 20), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(sq)).pack(pady=2)
tk.Button(sec_d, text="Rectangle", font=("Cascadia Code", 20), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(rec)).pack(pady=2)
tk.Button(sec_d, text="Triangle", font=("Cascadia Code", 20), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(tri)).pack(pady=2)
tk.Button(sec_d, text="Paralallogram", font=("Cascadia Code", 20), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(para)).pack(pady=2)
tk.Button(sec_d, text="Trapezium", font=("Cascadia Code", 20), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(trap)).pack(pady=2)
tk.Button(sec_d, text="Circle", font=("Cascadia Code", 20), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(cir)).pack(pady=2)

#---SQUARE---
tk.Button(sq, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(sec_d)).pack(padx=5, pady=5, anchor="nw")
tk.Label(sq, text="What you want to do?", font=("Cooper Black", 50)).pack(pady=100)
tk.Button(sq, text="  Area  ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="white", activeforeground="Black", command=lambda: sf(sq_a)).pack(pady=10)
tk.Button(sq, text="Perimter", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="white", activeforeground="Black", command=lambda: sf(sq_per)).pack(pady=10)

#---SQUARE_AREA---
remsqa = tk.Button(sq_a, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(sq))
remsqa.pack(padx=5, pady=5, anchor="nw")
sq_alab = tk.Label(sq_a, text="Enter lenght:", font=("Cooper Black", 50))
sq_alab.pack(pady=100)
sqaxval = tk.Entry(sq_a, font=("Cascadia Code", 40))
sqaxval.pack(pady=30)
sqxvalres = tk.Button(sq_a, text="Show Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
sqxvalres.pack(pady=10)

def areaofsq():
    try:
        x = float(sqaxval.get())
        area = x * x
        sqaxval.destroy()
        sqxvalres.destroy()
        sq_alab.destroy()
        l = tk.Label(sq_a, text=f"Area is {area}", font=("Cooper Black", 50))
        l.pack(pady=120)
        l.after(100)
    except ValueError:
        sq_alab.config(text="Please type Numerical Value")
sqxvalres.config(command=areaofsq)

#---SQUARE_PERIMETER---
remsqper = tk.Button(sq_per, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(sq))
remsqper.pack(padx=5, pady=5, anchor="nw")
sq_perlab = tk.Label(sq_per, text="Enter lenght:", font=("Cooper Black", 50))
sq_perlab.pack(pady=100)
sqperxval = tk.Entry(sq_per, font=("Cascadia Code", 40))
sqperxval.pack(pady=30)
sqperxvalres = tk.Button(sq_per, text="Show Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
sqperxvalres.pack(pady=10)

def periofsq():
    try:
        x = float(sqperxval.get())
        peri = 4 * x
        sqperxval.destroy()
        sqperxvalres.destroy()
        sq_perlab.destroy()
        tk.Label(sq_per, text=f"Perimeter is {peri}", font=("Cooper Black", 50)).pack(pady=120)
    except ValueError:
        sq_perlab.config(text="Please type Numerical Value")

sqperxvalres.config(command=periofsq)

#---RECTANGLE---
tk.Button(rec, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(sec_d)).pack(padx=5, pady=5, anchor="nw")
tk.Label(rec, text="What you want to do?", font=("Cooper Black", 50)).pack(pady=100)
tk.Button(rec, text="  Area  ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="white", activeforeground="Black", command=lambda: sf(rec_a)).pack(pady=10)
tk.Button(rec, text="Perimter", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="white", activeforeground="Black", command=lambda: sf(rec_per)).pack(pady=10)

#---RECTANGLE_AREA---
tk.Button(rec_a, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(rec)).pack(padx=5, pady=5, anchor="nw")
rec_alab = tk.Label(rec_a, text="Enter lenght:", font=("Cooper Black", 50))
rec_alab.pack(pady=100)
recaxval = tk.Entry(rec_a, font=("Cascadia Code", 40))
recaxval.pack(pady=30)
recaxvalres = tk.Button(rec_a, text="Result", font=("Cascaida Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
recaxvalres.pack(pady=10)

def askbreadth():
    try:
        val = recaxval.get()
        recaxval.destroy()
        recaxvalres.destroy()
        rec_alab.config(text="Enter Breadth:")
        global recalen
        recalen = float(val)
        global recaxval2
        recaxval2 = tk.Entry(rec_a, font=("Cascadia Code", 40))
        recaxval2.pack(pady=30)
        global recaxvalres2
        recaxvalres2 = tk.Button(rec_a, text="Result", font=("Cascaida Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=recareacal)
        recaxvalres2.pack(pady=10)
    except ValueError:
        rec_alab.config(text="Please Enter Numerical Value only")

recaxvalres.config(command=askbreadth)

def recareacal():
    try:
        val2 = recaxval2.get()
        recaxval2.destroy()
        recaxvalres2.destroy()
        rec_alab.destroy()
        global recabre
        recabre = float(val2)
        area = recalen * recabre
        tk.Label(rec_a, text=f"Area is {area}", font=("Cascadia Code", 50)).pack(pady=140)
    except ValueError:
        rec_alab.config(text="Please Enter Numerical Value only")
    
#---RECTANGLE_PERIMETER---
tk.Button(rec_per, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(rec)).pack(padx=5, pady=5, anchor="nw")
rec_plab = tk.Label(rec_per, text="Enter Lenght:", font=("Cooper Black", 50))
rec_plab.pack(pady=100)
recpxval = tk.Entry(rec_per, font=("Cascadia Code", 40))
recpxval.pack(pady=30)
recpxvalres = tk.Button(rec_per, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
recpxvalres.pack(pady=10)

def recbask():
    try:
        val = recpxval.get()
        recpxval.destroy()
        recpxvalres.destroy()
        rec_plab.config(text="Enter Breadth:")
        global recplen
        recplen = float(val)
        global recpxval2
        recpxval2 = tk.Entry(rec_per, font=("Cascadia Code", 40))
        recpxval2.pack(pady=30)
        global recpxvalres2
        recpxvalres2 = tk.Button(rec_per, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=recpercalc)
        recpxvalres2.pack(pady=10)
    except ValueError:
        rec_plab.config(text="Please Enter Numerical Value only")

recpxvalres.config(command=recbask)

def recpercalc():
    try:
        val2 = recpxval2.get()
        recpxval2.destroy()
        recpxvalres2.destroy()
        rec_plab.destroy()
        global recpbre
        recpbre = float(val2)
        peri = 2 * (recplen + recpbre)
        tk.Label(rec_per, text=f"Perimeter is {peri}", font=("Cascadia Code", 50)).pack(pady=140)
    except ValueError:
        rec_plab.config(text="Please Enter Numerical Value only")

#---TRIANGLE---
tk.Button(tri, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(sec_d)).pack(padx=5, pady=5, anchor="nw")
tk.Label(tri, text="What you want to do?", font=("Cooper Black", 50)).pack(pady=100)
tk.Button(tri, text="  Area  ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="white", activeforeground="Black", command=lambda: sf(tri_a)).pack(pady=10)
tk.Button(tri, text="Perimter", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="white", activeforeground="Black", command=lambda: sf(tri_per)).pack(pady=10)

#---TRIANGLE_AREA---
tk.Button(tri_a, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(tri)).pack(padx=5, pady=5, anchor="nw")
tri_alab = tk.Label(tri_a, text="Enter Height:", font=("Cooper Black", 50))
tri_alab.pack(pady=100)
triaxval = tk.Entry(tri_a, font=("Cascadia Code", 40))
triaxval.pack(pady=30)
triaxvalres = tk.Button(tri_a, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
triaxvalres.pack(pady=10)

def asktribase():
    val = triaxval.get()
    triaxval.destroy()
    triaxvalres.destroy()
    tri_alab.config(text="Enter Base:")
    global triah
    triah = float(val)
    global triaxval2
    triaxval2 = tk.Entry(tri_a, font=("Cascadia Code", 40))
    triaxval2.pack(pady=30)
    global triaxvalres2
    triaxvalres2 = tk.Button(tri_a, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=triareacalc)
    triaxvalres2.pack(pady=10)
    
triaxvalres.config(command=asktribase)

def triareacalc():
    val2 = triaxval2.get()
    triaxval2.destroy()
    triaxvalres2.destroy()
    tri_alab.destroy()
    global triab
    triab = float(val2)
    area = 1/2 * triah * triab
    tk.Label(tri_a, text=f"Area is {area}", font=("Cascadia Code", 50)).pack(pady=140) 

#---TRIANGLE_PERIMETER---
tk.Button(tri_per, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(tri)).pack(padx=5, pady=5, anchor="nw")
tri_plab = tk.Label(tri_per, text="Enter 1st Side:", font=("Cooper Black", 50))
tri_plab.pack(pady=100)
tripxval = tk.Entry(tri_per, font=("Cascadia Code", 40))
tripxval.pack(pady=30)
tripxvalres = tk.Button(tri_per, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
tripxvalres.pack(pady=10)

def secsidasktri():
    val = tripxval.get()
    tripxval.destroy()
    tripxvalres.destroy()
    tri_plab.config(text="Enter 2nd Side:")
    global tri1
    tri1 = float(val)
    global tripxval2
    tripxval2 = tk.Entry(tri_per, font=("Cascadia Code", 40))
    tripxval2.pack(pady=30)
    global tripxvalres2
    tripxvalres2 = tk.Button(tri_per, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=thrdsidasktri)
    tripxvalres2.pack(pady=10)

tripxvalres.config(command=secsidasktri)

def thrdsidasktri():
    val2 = tripxval2.get()
    tripxval2.destroy()
    tripxvalres2.destroy()
    tri_plab.config(text="Enter 3nd Side:")
    global tri2
    tri2 = float(val2)
    global tripxval3
    tripxval3 = tk.Entry(tri_per, font=("Cascadia Code", 40))
    tripxval3.pack(pady=30)
    global tripxvalres3
    tripxvalres3 = tk.Button(tri_per, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=tripercalc)
    tripxvalres3.pack(pady=10)

def tripercalc():
    val3 = tripxval3.get()
    tripxval3.destroy()
    tripxvalres3.destroy()
    tri_plab.destroy()
    global tri3
    tri3 = float(val3)
    peri = tri1 + tri2 + tri3
    tk.Label(tri_per, text=f"Perimeter is {peri}", font=("Cascadia Code", 50)).pack(pady=140)

#---PARALELLOGRAM---
tk.Button(para, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(sec_d)).pack(padx=5, pady=5, anchor="nw")
tk.Label(para, text="What you want to do?", font=("Cooper Black", 50)).pack(pady=100)
tk.Button(para, text="  Area  ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="white", activeforeground="Black", command=lambda: sf(para_a)).pack(pady=10)
tk.Button(para, text="Perimter", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="white", activeforeground="Black", command=lambda: sf(para_per)).pack(pady=10)

#---PARALELLOGRAM_AREA---
tk.Button(para_a, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(para)).pack(padx=5, pady=5, anchor="nw")
par_alab = tk.Label(para_a, text="Enter Height:", font=("Cooper Black", 50))
par_alab.pack(pady=100)
paraxval = tk.Entry(para_a, font=("Cascadia Code", 40))
paraxval.pack(pady=30)
paraxvalres = tk.Button(para_a, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
paraxvalres.pack(pady=10)

def askbrepara():
    val = paraxval.get()
    paraxval.destroy()
    paraxvalres.destroy()
    par_alab.config(text="Enter Base")
    global parah
    parah = float(val)
    global paraxval2
    paraxval2 = tk.Entry(para_a, font=("Cascadia Code", 40))
    paraxval2.pack(pady=30)
    global paraxvalres2
    paraxvalres2 = tk.Button(para_a, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=parareacalc)
    paraxvalres2.pack(pady=10)
    
paraxvalres.config(command=askbrepara)

def parareacalc():
    val2 = paraxval2.get()
    paraxval2.destroy()
    paraxvalres2.destroy()
    par_alab.destroy()
    global parab
    parab = float(val2)
    area = parah * parab
    tk.Label(para_a, text=f"Area is {area}", font=("Cascadia Code", 50)).pack(pady=140)
        
#---PARALELLOGRAM_PERIMETER---
tk.Button(para_per, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(para)).pack(padx=5, pady=5, anchor="nw")
par_plab = tk.Label(para_per, text="Enter 1st Side:", font=("Cooper Black", 50))
par_plab.pack(pady=100)
parpxval = tk.Entry(para_per, font=("Cascadia Code", 40))
parpxval.pack(pady=30)
parpxvalres = tk.Button(para_per, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
parpxvalres.pack(pady=10)

def paraasksid2():
    val = parpxval.get()
    parpxval.destroy()
    parpxvalres.destroy()
    par_plab.config(text="Enter 2nd Side:")
    global para1
    para1 = float(val)
    global parpxval2
    parpxval2 = tk.Entry(para_per, font=("Cascadia Code", 40))
    parpxval2.pack(pady=30)
    global parpxvalres2
    parpxvalres2 = tk.Button(para_per, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=paraasksid3)
    parpxvalres2.pack(pady=10)

parpxvalres.config(command=paraasksid2)

def paraasksid3():
    val2 = parpxval2.get()
    parpxval2.destroy()
    parpxvalres2.destroy()
    par_plab.config(text="Enter 3rd Side:")
    global para2
    para2 = float(val2)
    global parpxval3
    parpxval3 = tk.Entry(para_per, font=("Cascadia Code", 40))
    parpxval3.pack(pady=30)
    global parpxvalres3
    parpxvalres3 = tk.Button(para_per, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=paraasksid4)
    parpxvalres3.pack(pady=10)

def paraasksid4():
    val3 = parpxval3.get()
    parpxval3.destroy()
    parpxvalres3.destroy()
    par_plab.config(text="Enter 4th Side:")
    global para3
    para3 = float(val3)
    global parpxval4
    parpxval4 = tk.Entry(para_per, font=("Cascadia Code", 40))
    parpxval4.pack(pady=30)
    global parpxvalres4
    parpxvalres4 = tk.Button(para_per, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=parpercalc)
    parpxvalres4.pack(pady=10)

def parpercalc():
    val4 = parpxval4.get()
    parpxval4.destroy()
    parpxvalres4.destroy()
    par_plab.destroy()
    global para4
    para4 = float(val4)
    peri = para1 + para2 + para3 + para4
    tk.Label(para_per, text=f"Perimeter is {peri}", font=("Cascadia Code", 50)).pack(pady=140) 

#---TRAPEZIUM---
tk.Button(trap, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(sec_d)).pack(padx=5, pady=5, anchor="nw")
tk.Label(trap, text="What you want to do?", font=("Cooper Black", 50)).pack(pady=100)
tk.Button(trap, text="  Area  ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="white", activeforeground="Black", command=lambda: sf(trap_a)).pack(pady=10)
tk.Button(trap, text="Perimter", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="white", activeforeground="Black", command=lambda: sf(trap_per)).pack(pady=10)

#---TRAPEZIUM_AREA---
tk.Button(trap_a, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(trap)).pack(padx=5, pady=5, anchor="nw")
trap_alab = tk.Label(trap_a, text="Enter Height:", font=("Cooper Black", 50))
trap_alab.pack(pady=100)
trapaxval = tk.Entry(trap_a, font=("Cascadia Code", 40))
trapaxval.pack(pady=30)
trapaxvalres = tk.Button(trap_a, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
trapaxvalres.pack(pady=10)

def ask1paraside():
    val = trapaxval.get()
    trapaxval.destroy()
    trapaxvalres.destroy()
    trap_alab.config(text="Enter 1ST Paralell Side:")
    global traph
    traph = float(val)
    global trapaxval2
    trapaxval2 = tk.Entry(trap_a, font=("Cascadia Code", 40))
    trapaxval2.pack()
    global trapaxvalres2
    trapaxvalres2 = tk.Button(trap_a, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=ask2paraside)
    trapaxvalres2.pack(pady=10)

trapaxvalres.config(command=ask1paraside)

def ask2paraside():
    val2 = trapaxval2.get()
    trapaxval2.destroy()
    trapaxvalres2.destroy()
    trap_alab.config(text="Enter 2ND Paralell Side:")
    global trapa
    trapa = float(val2)
    global trapaxval3
    trapaxval3 = tk.Entry(trap_a, font=("Cascadia Code", 40))
    trapaxval3.pack()
    global trapaxvalres3
    trapaxvalres3 = tk.Button(trap_a, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=trapareacalc)
    trapaxvalres3.pack(pady=10)

def trapareacalc():
    val3 = trapaxval3.get()
    trapaxval3.destroy()
    trapaxvalres3.destroy()
    trap_alab.destroy()
    global trapb
    trapb = float(val3)
    area = 1/2 * traph * (trapa + trapb)
    tk.Label(trap_a, text=f"Area is {area}", font=("Cascadia Code", 50)).pack(pady=140)

#---TRAPEZIUM_PERIMETER---
tk.Button(trap_per, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(trap)).pack(padx=5, pady=5, anchor="nw")
trap_plab = tk.Label(trap_per, text="Enter 1st Side:", font=("Cooper Black", 50))
trap_plab.pack(pady=100)
trappxval = tk.Entry(trap_per, font=("Cascadia Code", 40))
trappxval.pack(pady=30)
trappxvalres = tk.Button(trap_per, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
trappxvalres.pack(pady=10)

def trapasksid2():
    val = trappxval.get()
    trappxval.destroy()
    trappxvalres.destroy()
    trap_plab.config(text="Enter 2nd Side:")
    global trap1
    trap1 = float(val)
    global trappxval2
    trappxval2 = tk.Entry(trap_per, font=("Cascadia Code", 40))
    trappxval2.pack(pady=30)
    global trappxvalres2
    trappxvalres2 = tk.Button(trap_per, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=trapasksid3)
    trappxvalres2.pack(pady=10)

trappxvalres.config(command=trapasksid2)

def trapasksid3():
    val2 = trappxval2.get()
    trappxval2.destroy()
    trappxvalres2.destroy()
    trap_plab.config(text="Enter 3rd Side:")
    global trap2
    trap2 = float(val2)
    global trappxval3
    trappxval3 = tk.Entry(trap_per, font=("Cascadia Code", 40))
    trappxval3.pack(pady=30)
    global trappxvalres3
    trappxvalres3 = tk.Button(trap_per, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=trapasksid4)
    trappxvalres3.pack(pady=10)

def trapasksid4():
    val3 = trappxval3.get()
    trappxval3.destroy()
    trappxvalres3.destroy()
    trap_plab.config(text="Enter 4th Side:")
    global trap3
    trap3 = float(val3)
    global trappxval4
    trappxval4 = tk.Entry(trap_per, font=("Cascadia Code", 40))
    trappxval4.pack(pady=30)
    global trappxvalres4
    trappxvalres4 = tk.Button(trap_per, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=trappercalc)
    trappxvalres4.pack(pady=10)

def trappercalc():
    val4 = trappxval4.get()
    trappxval4.destroy()
    trappxvalres4.destroy()
    trap_plab.destroy()
    global trap4
    trap4 = float(val4)
    peri = trap1 + trap2 + trap3 + trap4
    tk.Label(trap_per, text=f"Perimeter is {peri}", font=("Cascadia Code", 50)).pack(pady=140) 

#---CIRCLE---
tk.Button(cir, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(sec_d)).pack(padx=5, pady=5, anchor="nw")
tk.Label(cir, text="What you want to do?", font=("Cooper Black", 50)).pack(pady=100)
tk.Button(cir, text="     Area    ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="white", activeforeground="Black", command=lambda: sf(cir_a)).pack(pady=10)
tk.Button(cir, text="Circumference", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="white", activeforeground="Black", command=lambda: sf(cir_cum)).pack(pady=10)

#---CIRCLE_AREA---
tk.Button(cir_a, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(cir)).pack(padx=5, pady=5, anchor="nw")
cir_alab = tk.Label(cir_a, text="Enter Radius:", font=("Cooper Black", 50))
cir_alab.pack(pady=100)
ciraxval = tk.Entry(cir_a, font=("Cascadia Code", 40))
ciraxval.pack(pady=30)
ciraxvalres = tk.Button(cir_a, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
ciraxvalres.pack(pady=10)

def circlearea():
    val = ciraxval.get()
    ciraxval.destroy()
    ciraxvalres.destroy()
    cir_alab.destroy()
    global cirad
    cirad = float(val)
    area = math.pi * cirad**2
    tk.Label(cir_a, text=f"Area is {area: .2f}", font=("Cascadia Code", 50)).pack(pady=140)
    
ciraxvalres.config(command=circlearea)

#---CIRCLE_CIRCUMFERENCE----
tk.Button(cir_cum, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(cir)).pack(padx=5, pady=5, anchor="nw")
cir_plab = tk.Label(cir_cum, text="Enter Radius:", font=("Cooper Black", 50))
cir_plab.pack(pady=100)
cirpxval = tk.Entry(cir_cum, font=("Cascadia Code", 40))
cirpxval.pack(pady=30)
cirpxvalres = tk.Button(cir_cum, text="Next", font=("Casacadia Black", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
cirpxvalres.pack(pady=10)

def circumference():
    val = cirpxval.get()
    cirpxval.destroy()
    cirpxvalres.destroy()
    cir_plab.destroy()
    global cirrad
    cirrad = float(val)
    circum = 2 * math.pi * cirrad
    tk.Label(cir_cum, text=f"Circumference is {circum: .2f}", font=("Cascadia Code", 50)).pack(pady=140)
    
cirpxvalres.config(command=circumference)


#---3D_SHAPEES---
tk.Button(thrd_d, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(menu)).pack(padx=5, pady=5, anchor="nw")
tk.Label(thrd_d, text="Choose a shape:", font=("Cooper Black", 50)).pack(pady=70)
tk.Button(thrd_d, text="Cube", font=("Cascadia Code", 20), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(cube)).pack(pady=7)
tk.Button(thrd_d, text="Cuboid", font=("Cascadia Code", 20), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(cuboid)).pack(pady=7)
tk.Button(thrd_d, text="Sphere", font=("Cascadia Code", 20), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(sphere)).pack(pady=7)
tk.Button(thrd_d, text="Cylinder", font=("Cascadia Code", 20), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(cyl)).pack(pady=7)
tk.Button(thrd_d, text="Back", font=("Cascadia Code", 20), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(menu)).pack(pady=7)

#---CUBE---
tk.Button(cube, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(thrd_d)).pack(padx=5, pady=5, anchor="nw")
tk.Label(cube, text="Choose from the following:", font=("Cooper Black", 50)).pack(pady=70)
tk.Button(cube, text=" Total Surface Area ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(cu_tsa)).pack(pady=5)
tk.Button(cube, text="Lateral Surface Area", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(cu_lsa)).pack(pady=5)
tk.Button(cube, text="  Open Surface Area  ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(cu_op)).pack(pady=5)
tk.Button(cube, text="       Volume       ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(cu_v)).pack(pady=5)

#---CUBE_TSA---
tk.Button(cu_tsa, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(cube)).pack(padx=5, pady=5, anchor="nw")
cu_tsalab = tk.Label(cu_tsa, text="Enter Lenght:", font=("Cooper Black", 50))
cu_tsalab.pack(pady=70)
cutsaxval = tk.Entry(cu_tsa, font=("Cascadia Code", 50))
cutsaxval.pack(pady=30)
cutsaxvalres = tk.Button(cu_tsa, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
cutsaxvalres.pack(pady=20)

def cutsacalc():
    val = cutsaxval.get()
    cutsaxval.destroy()
    cutsaxvalres.destroy()
    cu_tsalab.destroy()
    x = float(val)
    area = 6 * x**2
    tk.Label(cu_tsa, text=f"Total Surface Area of cube is:\n{area: .2f}", font=("Cooper Black", 50)).pack(pady=140)
    
cutsaxvalres.config(command=cutsacalc)

#---CUBE_LSA---
tk.Button(cu_lsa, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(cube)).pack(padx=5, pady=5, anchor="nw")
cu_lsalab = tk.Label(cu_lsa, text="Enter Lenght:", font=("Cooper Black", 50))
cu_lsalab.pack(pady=70)
culsaxval = tk.Entry(cu_lsa, font=("Cascadia Code", 50))
culsaxval.pack(pady=30)
culsaxvalres = tk.Button(cu_lsa, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
culsaxvalres.pack(pady=20)

def culsacalc():
    val = culsaxval.get()
    culsaxval.destroy()
    culsaxvalres.destroy()
    cu_lsalab.destroy()
    x = float(val)
    area = 4 * x**2
    tk.Label(cu_lsa, text=f"Lateral Surface Area of cube is:\n{area: .2f}", font=("Cooper Black", 50)).pack(pady=140)
    
culsaxvalres.config(command=culsacalc)

#---CUBE_OPSA---
tk.Button(cu_op, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(cube)).pack(padx=5, pady=5, anchor="nw")
cu_osalab = tk.Label(cu_op, text="Enter Lenght:", font=("Cooper Black", 50))
cu_osalab.pack(pady=70)
cuosaxval = tk.Entry(cu_op, font=("Cascadia Code", 50))
cuosaxval.pack(pady=30)
cuosaxvalres = tk.Button(cu_op, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
cuosaxvalres.pack(pady=20)

def cuosacalc():
    val = cuosaxval.get()
    cuosaxval.destroy()
    cuosaxvalres.destroy()
    cu_osalab.destroy()
    x = float(val)
    area = 5 * x**2
    tk.Label(cu_op, text=f"Lateral Surface Area of cube is:\n{area: .2f}", font=("Cooper Black", 50)).pack(pady=140)
    
cuosaxvalres.config(command=cuosacalc)

#---CUBE_VOLUME---
tk.Button(cu_v, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(cube)).pack(padx=5, pady=5, anchor="nw")
cu_vlab = tk.Label(cu_v, text="Enter Lenght:", font=("Cooper Black", 50))
cu_vlab.pack(pady=70)
cuvxval = tk.Entry(cu_v, font=("Cascadia Code", 50))
cuvxval.pack(pady=30)
cuvxvalres = tk.Button(cu_v, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
cuvxvalres.pack(pady=20)

def cuvcalc():
    val = cuvxval.get()
    cuvxval.destroy()
    cuvxvalres.destroy()
    cu_vlab.destroy()
    x = float(val)
    v = x**3
    tk.Label(cu_v, text=f"Volume of cube is:\n{v: .2f}", font=("Cooper Black", 50)).pack(pady=140)
    
cuvxvalres.config(command=cuvcalc)

#---CUBOID---
tk.Button(cuboid, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(thrd_d)).pack(padx=5, pady=5, anchor="nw")
tk.Label(cuboid, text="Choose from the following:", font=("Cooper Black", 50)).pack(pady=70)
tk.Button(cuboid, text=" Total Surface Area ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(cuboi_tsa)).pack(pady=5)
tk.Button(cuboid, text="Lateral Surface Area", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(cuboi_lsa)).pack(pady=5)
tk.Button(cuboid, text="  Open Surface Area  ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(cuboi_op)).pack(pady=5)
tk.Button(cuboid, text="       Volume       ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(cuboi_v)).pack(pady=5)

#---CUBOID_TSA---
tk.Button(cuboi_tsa, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(cuboid)).pack(padx=5, pady=5, anchor="nw")
cuboi_tsalab = tk.Label(cuboi_tsa, text="Enter Lenght:", font=("Cooper Black", 50))
cuboi_tsalab.pack(pady=70)
cuboitsaxval = tk.Entry(cuboi_tsa, font=("Cascadia Code", 50))
cuboitsaxval.pack(pady=30)
cuboitsaxvalres = tk.Button(cuboi_tsa, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
cuboitsaxvalres.pack(pady=20)

def cuboibask():
    val = cuboitsaxval.get()
    cuboitsaxval.destroy()
    cuboitsaxvalres.destroy()
    cuboi_tsalab.config(text="Enter Breadth:")
    global cuboidl
    cuboidl = float(val)
    global cuboitsaxval2
    cuboitsaxval2 = tk.Entry(cuboi_tsa, font=("Cascadia Code", 50))
    cuboitsaxval2.pack(pady=30)
    global cuboitsaxvalres2
    cuboitsaxvalres2 = tk.Button(cuboi_tsa, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=cuboihask)
    cuboitsaxvalres2.pack(pady=20)
    
cuboitsaxvalres.config(command=cuboibask)

def cuboihask():
    val = cuboitsaxval2.get()
    cuboitsaxval2.destroy()
    cuboitsaxvalres2.destroy()
    cuboi_tsalab.config(text="Enter Height:")
    global cuboidb
    cuboidb = float(val)
    global cuboitsaxval3
    cuboitsaxval3 = tk.Entry(cuboi_tsa, font=("Cascadia Code", 50))
    cuboitsaxval3.pack(pady=30)
    global cuboitsaxvalres3
    cuboitsaxvalres3 = tk.Button(cuboi_tsa, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=cuboitsacalc)
    cuboitsaxvalres3.pack(pady=20)
    
def cuboitsacalc():
    val = cuboitsaxval3.get()
    cuboi_tsalab.destroy()
    cuboitsaxval3.destroy()
    cuboitsaxvalres3.destroy()
    global cuboidh
    cuboidh = float(val)
    tsa = 2 * (cuboidl * cuboidb + cuboidb * cuboidh + cuboidh * cuboidl)
    tk.Label(cuboi_tsa, text=f"Total Surface Area of cuboid is:\n{tsa: .2f}", font=("Cooper Black", 50)).pack(pady=170)

#---CUBOID_LSA---
tk.Button(cuboi_lsa, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(cuboid)).pack(padx=5, pady=5, anchor="nw")
cuboi_lsalab = tk.Label(cuboi_lsa, text="Enter Lenght:", font=("Cooper Black", 50))
cuboi_lsalab.pack(pady=70)
cuboilsaxval = tk.Entry(cuboi_lsa, font=("Cascadia Code", 50))
cuboilsaxval.pack(pady=30)
cuboilsaxvalres = tk.Button(cuboi_lsa, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
cuboilsaxvalres.pack(pady=20)

def cuboilbask():
    val = cuboilsaxval.get()
    cuboilsaxval.destroy()
    cuboilsaxvalres.destroy()
    cuboi_lsalab.config(text="Enter Breadth:")
    global cuboidll
    cuboidll = float(val)
    global cuboilsaxval2
    cuboilsaxval2 = tk.Entry(cuboi_lsa, font=("Cascadia Code", 50))
    cuboilsaxval2.pack(pady=30)
    global cuboilsaxvalres2
    cuboilsaxvalres2 = tk.Button(cuboi_lsa, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=cuboilhask)
    cuboilsaxvalres2.pack(pady=20)
    
cuboilsaxvalres.config(command=cuboilbask)

def cuboilhask():
    val = cuboilsaxval2.get()
    cuboilsaxval2.destroy()
    cuboilsaxvalres2.destroy()
    cuboi_lsalab.config(text="Enter Height:")
    global cuboidlb
    cuboidlb = float(val)
    global cuboilsaxval3
    cuboilsaxval3 = tk.Entry(cuboi_lsa, font=("Cascadia Code", 50))
    cuboilsaxval3.pack(pady=30)
    global cuboilsaxvalres3
    cuboilsaxvalres3 = tk.Button(cuboi_lsa, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=cuboilsacalc)
    cuboilsaxvalres3.pack(pady=20)
    
def cuboilsacalc():
    val = cuboilsaxval3.get()
    cuboi_lsalab.destroy()
    cuboilsaxval3.destroy()
    cuboilsaxvalres3.destroy()
    global cuboidlh
    cuboidlh = float(val)
    lsa = 2 * cuboidlh * (cuboidll + cuboidlb)
    tk.Label(cuboi_lsa, text=f"Total Surface Area of cuboid is:\n{lsa: .2f}", font=("Cooper Black", 50)).pack(pady=170)

#---CUBOID_OSA---
tk.Button(cuboi_op, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(cuboid)).pack(padx=5, pady=5, anchor="nw")
cuboi_olab = tk.Label(cuboi_op, text="Enter Lenght:", font=("Cooper Black", 50))
cuboi_olab.pack(pady=70)
cuboioxval = tk.Entry(cuboi_op, font=("Cascadia Code", 50))
cuboioxval.pack(pady=30)
cuboioxvalres = tk.Button(cuboi_op, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
cuboioxvalres.pack(pady=20)

def cuboiobask():
    val = cuboioxval.get()
    cuboioxval.destroy()
    cuboioxvalres.destroy()
    cuboi_olab.config(text="Enter Breadth:")
    global cuboidol
    cuboidol = float(val)
    global cuboioxval2
    cuboioxval2 = tk.Entry(cuboi_op, font=("Cascadia Code", 50))
    cuboioxval2.pack(pady=30)
    global cuboioxvalres2
    cuboioxvalres2 = tk.Button(cuboi_op, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=cuboiohask)
    cuboioxvalres2.pack(pady=20)
    
cuboioxvalres.config(command=cuboiobask)

def cuboiohask():
    val = cuboioxval2.get()
    cuboioxval2.destroy()
    cuboioxvalres2.destroy()
    cuboi_olab.config(text="Enter Height:")
    global cuboidob
    cuboidob = float(val)
    global cuboioxval3
    cuboioxval3 = tk.Entry(cuboi_op, font=("Cascadia Code", 50))
    cuboioxval3.pack(pady=30)
    global cuboioxvalres3
    cuboioxvalres3 = tk.Button(cuboi_op, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=cuboiocalc)
    cuboioxvalres3.pack(pady=20)
    
def cuboiocalc():
    val = cuboioxval3.get()
    cuboi_olab.destroy()
    cuboioxval3.destroy()
    cuboioxvalres3.destroy()
    global cuboidoh
    cuboidoh = float(val)
    osa = 2 * cuboidoh * (cuboidol + cuboidob) + (cuboidol * cuboidob)
    tk.Label(cuboi_op, text=f"Total Surface Area of cuboid is:\n{osa: .2f}", font=("Cooper Black", 50)).pack(pady=170)

#---CUBOID_VOLUME---
tk.Button(cuboi_v, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(cuboid)).pack(padx=5, pady=5, anchor="nw")
cuboi_vlab = tk.Label(cuboi_v, text="Enter Lenght:", font=("Cooper Black", 50))
cuboi_vlab.pack(pady=70)
cuboivxval = tk.Entry(cuboi_v, font=("Cascadia Code", 50))
cuboivxval.pack(pady=30)
cuboivxvalres = tk.Button(cuboi_v, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
cuboivxvalres.pack(pady=20)

def cuboivbask():
    val = cuboivxval.get()
    cuboivxval.destroy()
    cuboivxvalres.destroy()
    cuboi_vlab.config(text="Enter Breadth:")
    global cuboidvl
    cuboidvl = float(val)
    global cuboivxval2
    cuboivxval2 = tk.Entry(cuboi_v, font=("Cascadia Code", 50))
    cuboivxval2.pack(pady=30)
    global cuboivxvalres2
    cuboivxvalres2 = tk.Button(cuboi_v, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=cuboivhask)
    cuboivxvalres2.pack(pady=20)
    
cuboivxvalres.config(command=cuboivbask)

def cuboivhask():
    val = cuboivxval2.get()
    cuboivxval2.destroy()
    cuboivxvalres2.destroy()
    cuboi_vlab.config(text="Enter Height:")
    global cuboidvb
    cuboidvb = float(val)
    global cuboivxval3
    cuboivxval3 = tk.Entry(cuboi_v, font=("Cascadia Code", 50))
    cuboivxval3.pack(pady=30)
    global cuboivxvalres3
    cuboivxvalres3 = tk.Button(cuboi_v, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=cuboivcalc)
    cuboivxvalres3.pack(pady=20)
    
def cuboivcalc():
    val = cuboivxval3.get()
    cuboi_vlab.destroy()
    cuboivxval3.destroy()
    cuboivxvalres3.destroy()
    global cuboidvh
    cuboidvh = float(val)
    v = cuboidvl * cuboidvb * cuboidvh
    tk.Label(cuboi_v, text=f"Volume of cuboid is:\n{v: .2f}", font=("Cooper Black", 50)).pack(pady=170)

#---SPHERE---
tk.Button(sphere, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(thrd_d)).pack(padx=5, pady=5, anchor="nw")
tk.Label(sphere, text="Choose from the following:", font=("Cooper Black", 50)).pack(pady=70)
tk.Button(sphere, text=" Total Surface Area ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(sph_tsa)).pack(pady=5)
tk.Button(sphere, text="       Volume       ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(sph_v)).pack(pady=5)

#---SPHERE_TSA---
tk.Button(sph_tsa, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(sphere)).pack(padx=5, pady=5, anchor="nw")
sph_tsalab = tk.Label(sph_tsa, text="Enter Radius:", font=("Cooper Black", 50))
sph_tsalab.pack(pady=70)
sphtsaxval = tk.Entry(sph_tsa, font=("Cascadia Code", 50))
sphtsaxval.pack(pady=30)
sphtsaxvalres = tk.Button(sph_tsa, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
sphtsaxvalres.pack(pady=20)

def sphtsacalc():
    val = sphtsaxval.get()
    sphtsaxval.destroy()
    sphtsaxvalres.destroy()
    sph_tsalab.destroy()
    global sphrad
    sphrad = float(val)
    tsa = 4 * math.pi * sphrad ** 2
    tk.Label(sph_tsa, text=f"Total Surface Area of Sphere is:\n{tsa: .2f}", font=("Cooper Black", 50)).pack(pady=170)

sphtsaxvalres.config(command=sphtsacalc)

#---SPHERE_VOLUME---
tk.Button(sph_v, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(sphere)).pack(padx=5, pady=5, anchor="nw")
sph_vlab = tk.Label(sph_v, text="Enter Radius:", font=("Cooper Black", 50))
sph_vlab.pack(pady=70)
sphvxval = tk.Entry(sph_v, font=("Cascadia Code", 50))
sphvxval.pack(pady=30)
sphvxvalres = tk.Button(sph_v, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
sphvxvalres.pack(pady=20)

def sphvcalc():
    val = sphvxval.get()
    sphvxval.destroy()
    sphvxvalres.destroy()
    sph_vlab.destroy()
    global sphvrad
    sphvrad = float(val)
    v = 4 * math.pi * sphvrad ** 3 / 3
    tk.Label(sph_v, text=f"Total Surface Area of Sphere is:\n{v: .2f}", font=("Cooper Black", 50)).pack(pady=170)

sphvxvalres.config(command=sphvcalc)

#---CYLINDER---
tk.Button(cyl, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(thrd_d)).pack(padx=5, pady=5, anchor="nw")
tk.Label(cyl, text="Choose from the following:", font=("Cooper Black", 50)).pack(pady=70)
tk.Button(cyl, text=" Total Surface Area ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(cy_tsa)).pack(pady=5)
tk.Button(cyl, text=" Curved Surface Area ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(cy_csa)).pack(pady=5)
tk.Button(cyl, text="       Volume       ", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=lambda: sf(cy_v)).pack(pady=5)

#---CYLINDER_TSA---
tk.Button(cy_tsa, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(cyl)).pack(padx=5, pady=5, anchor="nw")
cy_tsalab = tk.Label(cy_tsa, text="Enter Radius:", font=("Cooper Black", 50))
cy_tsalab.pack(pady=70)
cytsaxval = tk.Entry(cy_tsa, font=("Cascadia Code", 50))
cytsaxval.pack(pady=30)
cytsaxvalres = tk.Button(cy_tsa, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
cytsaxvalres.pack(pady=20)

def askhcy():
    val = cytsaxval.get()
    cytsaxval.destroy()
    cytsaxvalres.destroy()
    cy_tsalab.config(text="Enter Height:")
    global cyrad
    cyrad = float(val)
    global cytsaxval2
    cytsaxval2 = tk.Entry(cy_tsa, font=("Cascadia Code", 50))
    cytsaxval2.pack(pady=30)
    global cytsaxvalres2
    cytsaxvalres2 = tk.Button(cy_tsa, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=cytsacalc)
    cytsaxvalres2.pack(pady=20)
    
cytsaxvalres.config(command=askhcy)

def cytsacalc():
    val = cytsaxval2.get()
    cytsaxval2.destroy()
    cytsaxvalres2.destroy()
    cy_tsalab.destroy()
    global cyh
    cyh = float(val)
    tsa = 2 * math.pi * cyrad * (cyrad + cyh)
    tk.Label(cy_tsa, text=f"Total Surface Area of Cylinder is:\n{tsa: .2f}", font=("Cooper Black", 50)).pack(pady=170)

#---CYLINDER_CSA---
tk.Button(cy_csa, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(cyl)).pack(padx=5, pady=5, anchor="nw")
cy_csalab = tk.Label(cy_csa, text="Enter Radius:", font=("Cooper Black", 50))
cy_csalab.pack(pady=70)
cycsaxval = tk.Entry(cy_csa, font=("Cascadia Code", 50))
cycsaxval.pack(pady=30)
cycsaxvalres = tk.Button(cy_csa, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
cycsaxvalres.pack(pady=20)

def askhcyc():
    val = cycsaxval.get()
    cycsaxval.destroy()
    cycsaxvalres.destroy()
    cy_csalab.config(text="Enter Height:")
    global cycrad
    cycrad = float(val)
    global cycsaxval2
    cycsaxval2 = tk.Entry(cy_csa, font=("Cascadia Code", 50))
    cycsaxval2.pack(pady=30)
    global cycsaxvalres2
    cycsaxvalres2 = tk.Button(cy_csa, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=cycsacalc)
    cycsaxvalres2.pack(pady=20)
    
cycsaxvalres.config(command=askhcyc)

def cycsacalc():
    val = cycsaxval2.get()
    cycsaxval2.destroy()
    cycsaxvalres2.destroy()
    cy_csalab.destroy()
    global cych
    cych = float(val)
    csa = 2 * math.pi * cycrad * cych
    tk.Label(cy_csa, text=f"Total Surface Area of Cylinder is:\n{csa: .2f}", font=("Cooper Black", 50)).pack(pady=170)

#---CYLINDER_CSA---
tk.Button(cy_v, text="X", font=("Pusab", 20), bg="Black", fg="White", activebackground="Red", activeforeground="White", command=lambda: sf(cyl)).pack(padx=5, pady=5, anchor="nw")
cy_vlab = tk.Label(cy_v, text="Enter Radius:", font=("Cooper Black", 50))
cy_vlab.pack(pady=70)
cyvxval = tk.Entry(cy_v, font=("Cascadia Code", 50))
cyvxval.pack(pady=30)
cyvxvalres = tk.Button(cy_v, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black")
cyvxvalres.pack(pady=20)

def askhcyv():
    val = cyvxval.get()
    cyvxval.destroy()
    cyvxvalres.destroy()
    cy_vlab.config(text="Enter Height:")
    global cyvrad
    cyvrad = float(val)
    global cyvxval2
    cyvxval2 = tk.Entry(cy_v, font=("Cascadia Code", 50))
    cyvxval2.pack(pady=30)
    global cyvxvalres2
    cyvxvalres2 = tk.Button(cy_v, text="Result", font=("Cascadia Code", 30), bg="Black", fg="White", activebackground="White", activeforeground="Black", command=cyvcalc)
    cyvxvalres2.pack(pady=20)
    
cyvxvalres.config(command=askhcyv)

def cyvcalc():
    val = cyvxval2.get()
    cyvxval2.destroy()
    cyvxvalres2.destroy()
    cy_vlab.destroy()
    global cyvh
    cyvh = float(val)
    v = math.pi * cyvrad ** 2 * cyvh
    tk.Label(cy_v, text=f"Total Surface Area of Cylinder is:\n{v: .2f}", font=("Cooper Black", 50)).pack(pady=170)

sf(menu)
root.mainloop()