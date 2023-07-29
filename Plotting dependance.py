import numpy as np
import matplotlib.pyplot as plt
from form_factor_calculator import form_factor_calc

length = 0.2
width = 0.01
terms = 1000


# Plotting the effect of varying the length, width and number of terms on the form factor
nvarlist=np.linspace(1,30,30,dtype=int)
avarlist=np.linspace(1,10,100)
bvarlist=np.linspace(1,10,100)

formA=[]   
formB=[]
formN=[]

for i in range(0,100):
    formA.append(form_factor_calc(avarlist[i], width, terms))
    formB.append(form_factor_calc(length, bvarlist[i], terms))
for i in range(0,30):
    formN.append(form_factor_calc(length, width, nvarlist[i]))    

# create three plots in a row on one figure ax
fig, ax = plt.subplots(1,3,figsize=(15,5))
ax[0].plot(avarlist,formA)
ax[0].set_title("Varying Length 'a'", y=1.05)
ax[0].set_xlabel("a")
ax[0].set_ylabel("Form Factor")
ax[0].grid(alpha=0.3)

ax[1].plot(bvarlist,formB)
ax[1].set_title("Varying Width 'b'", y=1.05)
ax[1].set_xlabel("b")
ax[1].set_ylabel("Form Factor")
ax[1].grid(alpha=0.3)

ax[2].plot(nvarlist,formN)
ax[2].scatter(nvarlist,formN, s=5)
ax[2].set_title("Varying Number of Terms 'n'", y=1.05)
ax[2].set_xlabel("n")
ax[2].set_ylabel("Form Factor")
ax[2].grid(alpha=0.3)
plt.show()
