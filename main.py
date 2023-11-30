etel_lista=["Rakott krumpli","Spenótos tészta","Franciahagymaleves","Barackkrémleves"]
etel_ar=[1600,1400,1250,1300]
rendeles_lista:int=[]

import etlap
etlap_meret: int = 36


etlap.kiiras("*", etlap_meret)

etlap.szöveg("*", "Étlap", "*", etlap_meret)

etlap.kiiras("*", etlap_meret)

etlap.szöveg("*", "Főétel", "*", etlap_meret)

etlap.kiiras("*", etlap_meret)

etlap.kis_szöveg("*", etel_lista[0],str(etel_ar[0])+"Ft", "*", etlap_meret)

etlap.kis_szöveg("*", etel_lista[1],str(etel_ar[1])+"Ft", "*", etlap_meret)

etlap.kiiras("*", etlap_meret)

etlap.szöveg("*", "Levesek", "*", etlap_meret)

etlap.kiiras("*", etlap_meret)

etlap.kis_szöveg("*", etel_lista[2],str(etel_ar[2])+"Ft", "*", etlap_meret)

etlap.kis_szöveg("*", etel_lista[3],str(etel_ar[3])+"Ft", "*", etlap_meret)

import rendeles
rendeles.foetel("*", etlap_meret, etel_ar, etel_lista, rendeles_lista)
rendeles.leves("*", etlap_meret, etel_ar, etel_lista, rendeles_lista)


import rendelesosszegzes
rendelesosszegzes.szamla(rendeles_lista[0],300,rendeles_lista[1],300)

import kozos_eljaras
kozos_eljaras.focim("*", 36)
kozos_eljaras.szoveg_kiiaras("*", "Rendelés", "*")
kozos_eljaras.focim("*", 36)

kozos_eljaras.foetelek(f"", "300Ft")
kozos_eljaras.foetelek("Rakot Krumpli", "300Ft")

kozos_eljaras.focim("*", 36)
rendelesosszegzes.szoveg_kiiras("*","Köszönjük hogy a vendégünk volt","*")
kozos_eljaras.focim("*", 36)