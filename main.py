import time
import os


armas = ["Desarmador", "Picahielo", "Libro", "Cuchillo"
         "Lapiz", "Veneno", "Silla", "Cerveza"]
personas = ["CR7", "Cepillin", "Bad Bunny",
            "Peña Nieto", "Mamá lucha", "Messi", "Blue Demon", ]

zonas = ["Auditorio", "Estadio",
       "Casa Blanca", "La feria", "Baños",
       "Aurrera", "Cuadrilatero", "Cine"]

n_preguntas: int = 0

salidas = {}
salidas [(1,1,1)] = ["Aurrera"]
salidas [(1,1,2)] = ["Casa Blanca"]
salidas [(1,1,3)] = ["Estadio"]
salidas [(1,1,4)] = ["Cuadrilatero"]
salidas [(2,1,1)] = ["La feria"]
salidas [(1,1,2)] = ["Auditorio"]
salidas [(2,1,3)] = ["Cine"]
salidas [(1,1,4)] = ["Baños"]


print ("\nEres un ex detective policial que está retirado, "
           "pero de vez en cuando tomas casos para hacer justicia con tus propias manos.\n")
print ( "Vas a tu café favorito de las mañanas y en la ciudad parece abrumada, pues han asesinado a una persona"
        "comun y corriente y entre los involucrados se encuentran estos grandes famosos"
        "por lo que decides tomar el caso...\n")
time.sleep(15)

n_historia = int(input("\nQué historia quieres jugar?\n"
                       "1) El asesinato de Enrique.\n"
                       "2) El asesinato de Valeria.\n"))
if n_historia == 1:
    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    print ("\n ¡Han asesinado a Colosio!, o almenos a alguien que se parece mucho a él.\n"
           "Es tu deber investigar este caso hasta el final\n")
    while n_preguntas <=7:

        pregunta= int(input("\nQué quieres hacer?\n"
               "1) Interrogar un Famoso\n"
               "2) Investigar un Lugar\n"
               "3) Investigar un Arma Homicida\n"))
        if pregunta == 1 :
            p_persona = int(input("\nA quién quieres interrogar?\n"
                            "1) CR7.\n"
                            "2) Cepillin.\n"
                            "3) Bad Bunny.\n"
                            "4) Peña Nieto.\n"
                            "5) Mamá lucha."
                            "6) Messi.\n"
                            "7) Blue Demon.\n"
                            "8) Cantinflas.\n"))
            if p_persona == 1:
                    print ("\nLe preguntas a CR7 qué hizo en los últimos minutos, y él contesta:\n "
                            "“Llevo horas paseando en el aurrera,\n"
                            "Estuve buscando un Lapiz de buena marca,\n"
                            "no he tenido tiempo para nada más”.\n"
                            "El profe también menciona que vio a Cantinflas actuar raro. Pero... pues es actor\n")
            elif p_persona == 2:
                    print( "Le preguntas a Cepillin qué ha estado haciendo en los últimos minutos, y tal vez le pidas un autógrafo,\n"
                           "es famoso después de todo: “Desde hace tiempo que estoy comiendo con Bad Bunny, creo que he tenido suerte, \n"
                           "canta muy bien.\n"
                           "Al final no le pides un autógrafo, no resultó muy agradable.\n")
            elif p_persona == 3 :
                    print ("Le preguntas a Bad Bunny qué ha hecho en los últimos minutos\n "
                        "¿Solo he estado comiendo con Cepillin, hace buenos trucos, sabes? "
                           "Gana mucho dinero, hemos hablado por horas.\n "
                           "Te alejas con disimulo diciendo que tienes un caso que resolver\n " )
            elif p_persona == 4:
                    print("\n Te acercas a Peña Nieto con cuidado y le preguntas por lo que ha estado haciendo:\n "
                          "“Mi país está investigando estas extrañas criaturas para descubrir sus secretos,\n"
                          "me ha tomado todo el día conseguir estas figuras.”\n"
                          "Peña Nieto también menciono haber visto a mama lucha ir hacia los baños y al cine.\n")
            elif p_persona == 5:
                    print("Con entusiasmo te acercas a Mama lucha y le preguntas sobre sus actividades en las últimas horas: "
                          "“Intenté usar el juego de baile, pero mis impulsos de lucha me ganaron y destruí la máquina, intenté repararla, "
                          "pero una silla no es una buena herramienta”. Te alejas sintiendo lástima por ella"
                          "Mama lucha también mencionó que vio a Messi cerca de los baños.")
            elif p_persona == 6:
                    print("Te acercas, con un poco de admiracion, a Messi. Le preguntas sobre lo que ha hecho en estas horas: "
                          "“Solo he estado viendo los partidos, fueron muy intensos, casi se me cae mi comida. ")
            elif p_persona == 7:
                    print("Te acercas con Blue Demon, para preguntarle qué ha hecho con Enrique. "
                          "“¿Enrique? Yo solo le puse una paliza a Cantinflas en el Ring, y ahora compraré un juego con lo que gané”. "
                          "Las personas feas no son necesariamente malas, ahora lo sabes. Deberías reflexionar sobre tus prejuicios. "
                          "Blue Demon menciona que no vio a Messi en su partida, solo lo vio cuando iba de camino a comprar un juego.")
            elif p_persona == 8:
                    print("Te acercas a Cantinflas, aguantando la tentación de decirle que estamos al aire, y le preguntas por lo que ha estado haciendo: "
                          "“Solo quería una platicaa amistosa con Blue"
                          "Cantinflas menciona que no notó a Messi en la partida, no recuerda haberlo visto, "
                          "pero tampoco prestaba mucha atención a sus alrededores.")
            time.sleep(20)
            clear()
        elif pregunta == 2:
            p_lugar = int (input ("\nQué lugar quieres investigar?:\n"
                                  "1) Aurrera\n"
                                  "2) Casa Blanca\n"
                                  "3) Estadio\n"
                                  "4) cuadrilatero\n"
                                  "5) La Feria\n"
                                  "6) Auditorio\n"
                                  "7) Cine\n"
                                  "8) Baños\n"))
            if p_lugar == 1:
                print("No están funcionando, pero en realidad no es digno de sospecha, pero es curioso como nada funciona aquí.\n"
                      "Parece que el CR7 intenta conseguir algo, dice que lleva aquí horas, pero no logra dar con el problema.\n"
                      "Espero que en algún momento logre encontrar todo lo que busca a buen precio.\n")
            elif p_lugar == 2:
                print("Parece que esta solo el lugar, se alcanza a ver un libro en el jardin, demasiado limpia la Casa,\n "
                      "incluso huele a jabón. El resto del lugar es normal, dentro de lo que cabe.\n "
                      "Peña Nieto tiene una gran bolsa llena de cosas, parecen  algunos libros viejos,\n ")
            elif p_lugar == 3:
                print("Hay un cuchillo aquí, parece usado,\n "
                      "pero el que tenga sangre no significa nada, ¿o sí? "
                      "Blue Demon está comprando boletos para toda su familia"
                      "Qué manera de malgastar dinero.\n")
            elif p_lugar == 4:
                print("Parece todo normal a excepción de un poco de papel higiénico en el suelo. ¿Qué demonios hace aquí?\n")
            elif p_lugar == 5:
                print(
                      "parece que alguien olvidó su desarmador aqui, Este lugar está limpio.\n"
                      "Cantinflas parece atónito, creo que perdió un amigo.\n"
                      "Messi intenta consolarlo, parece agitado, ¿se habran peleado?\n")
            elif p_lugar == 6:
                print("Hay un picahielos cerca de una nevera, justo donde debería de estar.\n"
                      "Cepillin, y Bad Bunny están comiendo juntos, la verdad no me sorprende,\n"
                      )
            elif p_lugar == 7:
                print(
                      "No hay signos de sangre o batalla. Hay una Silla frente a la pantalla, que extraño\n"
                      "Mamá lucha está frustrada en una esquina, incluso tal vez preocupada, me pregunto qué le pasa.\n")
            elif p_lugar == 8:
                print("Este lugar no huele bien, incluso peor de lo que debería, una puerta está caida,\n"
                      "hay algo raro en el lavabo, ¿acaso es sangre?\n")
            time.sleep(20)
            clear()
        elif pregunta == 3:
            p_arma = int(input("\nQué arma quieres investigar?:\n"
                               "1) Desarmador\n"
                               "2) Picahielo\n"
                               "3) Libro\n"
                               "4) Cuchillo\n"
                               "5) Lapiz\n"
                               "6) Cerveza\n"
                               "7) Veneno\n"
                               "8) Silla\n"))
            if p_arma == 1:
                print("Alguien dejó esto en La Feria, tal vez estaban arreglando algo.\n"
                       )
            elif p_arma == 2:
                print("Está justo en su lugar, al lado de la nevera de un restaurante. No parece dañada o manchada de sangre.\n")
            elif p_arma == 3:
                print("Es raro ver un libro tirado en el jardin de la Casa Blanca\n"
                       "aunque huele un poco a jabón en realidad no tiene nada de malo.\n")
            elif p_arma == 4:
                print("Definitivamente está usado, podrías analizar las huellas dactilares para saber quién lo usó,\n"
                       "pero eso le quitaría la diversión a las cosas, así que solo lo dejas donde está,\n"
                       "no quieres mancharte de sangre, ¿o sí?\n")
            elif p_arma == 5:
                print("¿Quién busca tanto un lápiz? Es ridículo. Aun así, en realidad no hay nada malo con él,\n"
                       "salvo que estaba en el Aurrera.\n")
            elif p_arma == 6:
                print("Por alguna razón están en el Estadio.\n"
                       "Parece que tomaron algunas.\n")
            elif p_arma == 7:
                print("No hay nada malo. El frasco está lleno. Parece hasta sellado\n")
            elif p_arma == 8:
                print( "La encontré en el Cine frente a la pantalla.\n"
                       "Parece que se usó, pero para el propósito normal de una silla.\n")
            time.sleep(20)
            clear()
        n_preguntas = n_preguntas + 1
    clear()
    if n_preguntas >= 7:
        r_arma = int(input("\n\n\nSe acabaron las preguntas, espero que sepas quién es el asesino:\n"
                           "Qué arma usaron para cometer el asesinato?:\n"
                           "1) Tanga de hule\n"
                           "2) Pica hielo\n"
                           "3) Figura de wuaifu\n"
                           "4) Cuchillo\n"
                           "5) Lapiz muy, muy filoso \n"
                           "6) Tijeras para zurdos\n"
                           "7) Veneno para rata\n"
                           "8) Calceta con mantequilla\n"))
        if r_arma == 1:
            r_lugar = int(input("En qué lugar se cometió el asesinato?\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if r_lugar == 1:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 2:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 3:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 4:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 5:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 6:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 7:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 8:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
        if r_arma == 2:
            r_lugar = int(input("En qué lugar se cometió el asesinato?\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if r_lugar == 1:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 2:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 3:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 4:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 5:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 6:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 7:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 8:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
        if r_arma == 3:
            r_lugar = int(input("En qué lugar se cometió el asesinato?\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if r_lugar == 1:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 2:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 3:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 4:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 5:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 6:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 7:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 8:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
        if r_arma == 4:
            r_lugar = int(input("En qué lugar se cometió el asesinato?\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if r_lugar == 1:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print("Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                          "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                          "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                          "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print("A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                          "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                          "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print("Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                          "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                          "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 2:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print("Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                          "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                          "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                          "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print("A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                          "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                          "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print("Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                          "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                          "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 3:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print("Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                          "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                          "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                          "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print("A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                          "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                          "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print("Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                          "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                          "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 4:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print("Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                          "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                          "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                          "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print("A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                          "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                          "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print("Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                          "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                          "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 5:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print("Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                          "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                          "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                          "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print("A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                          "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                          "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print("Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                          "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                          "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 6:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print("Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                          "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                          "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                          "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print("A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                          "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                          "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print("Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                          "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                          "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 7:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print("Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                          "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                          "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                          "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print("A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                          "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                          "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print("Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                          "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                          "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 8:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print("Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                          "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                          "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                          "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print("Es un día triste para el mundo, pero las pruebas son concluyentes.\n"
                          "Acusas al Panadero con el pan, quien era el verdadero asesino.Has ganado el juego, pero a qué costo.\n"
                          "Personalmente estoy muy afectado y no creo poder seguir narrando, solo me voy a recostar aquí, sin hacer nada.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print("Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                          "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                          "Tampoco me asustaría mucho, es una marioneta después de todo.")
        if r_arma == 5:
            r_lugar = int(input("En qué lugar se cometió el asesinato?\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if r_lugar == 1:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 2:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 3:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 4:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 5:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 6:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 7:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 8:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
        if r_arma == 6:
            r_lugar = int(input("En qué lugar se cometió el asesinato?\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if r_lugar == 1:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 2:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 3:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 4:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 5:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 6:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 7:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 8:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
        if r_arma == 7:
            r_lugar = int(input("En qué lugar se cometió el asesinato?\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if r_lugar == 1:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 2:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 3:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 4:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 5:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 6:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 7:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 8:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
        if r_arma == 8:
            r_lugar = int(input("En qué lugar se cometió el asesinato?\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if r_lugar == 1:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 2:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 3:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 4:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 5:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 6:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 7:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
            if r_lugar == 8:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profesor de ser el asesino, después del juicio resulta que era inocente,\n"
                          "sin embargo, fue procesado por posesión de sustancias ilegales y pasará un tiempo en la cárcel.\n"
                          "Cabe resaltar que reprobaste su clase")
                if r_persona == 2:
                    print("Con entusiasmo, acusas a Ricardo de ser el asesino, a tu ex no le causa gracia,\n"
                          "pero tampoco es que te importe mucho su opinión. Sin embargo, Ricardo no era el asesino,\n"
                          "y ahora está libre y fuera de sospechas.\n"
                          "Deberías correr, dicen que Canadá es bonito en estas épocas.")
                if r_persona == 3:
                    print(
                        "Acusas a tu ex de ser quien asesinó a Colosio, tal vez fue más por motivos personales que por sospechas reales.\n"
                        "Aún así estás satisfecho con los resultados, o eso creías, ya que resultó ser inocente.\n"
                        "Ahora enfrentas una demanda por violencia psicológica y cargos por agresión física,\n"
                        "los cuales jamás pasaron, pero aceptémoslo, con nuestro sistema judicial machista estarás afuera en 2 semanas.")
                if r_persona == 4:
                    print("¿En serio?, acusas a Putin, que en lo personal no parece una asombrosa idea, en fin,\n"
                          "aunque fuera el asesino (que, por cierto, no lo es), saldría de la cárcel en unas horas,y seguramente eres hombre muerto.\n"
                          "Te han salido muchas cosas mal en la vida, pero esto sobrepasa a todas las demás.")
                if r_persona == 5:
                    print("Muy a tu pesar, acusas a mamá lucha.\n"
                          "Seguro que las madres de todo el mundo no estarán felices ahora que nadie luchará por los precios bajos.\n"
                          "Pero ella no era la asesina.\n"
                          "Aun así, esta experiencia la hizo reflexionar y decidió dejar la lucha para estudiar leyes,\n"
                          "y es una lástima ya que eso de pelear con precios bajos era lo suyo.")
                if r_persona == 6:
                    print(
                        "A pesar de toda la felicidad que le ha dado al mundo, acusas al Panadero con el pan de ser el asesino.\n"
                        "Sin embargo, no hay suficientes pruebas para acusarlo y es inocente hasta probar lo contrario.\n"
                        "Si de verdad es el asesino… Bueno, nunca lo sabremos, pero al menos tendremos pan.")
                if r_persona == 7:
                    print("Acusas a la Hermanastra fea, ni siquiera tú estás muy seguro del por qué, pero vamos,\n"
                          "con esa cara quién más puede ser el asesino. Pero tú y tus perjuicios están mal, como siempre.\n"
                          "Es inocente, ella te perdona y te dice que solo pasen página.\n"
                          "Es buena persona, no sé cómo pudiste hacerle eso. Das asco.")
                if r_persona == 8:
                    print(
                        "Acusas a el presentador del programa 31 minutos de ser el asesino, seguro será un escándalo en los medios.\n"
                        "Pero te equivocaste, Tulio es inocente y ahora usará todo su poder para hacerte caer.\n"
                        "Tampoco me asustaría mucho, es una marioneta después de todo.")
elif n_historia == 2:
    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    print("¡Han asesinado a Paquita la del barrio! y no se sabe quién fue la rata que lo hizo.\n"
          "Pero no te preocupes,tú y tus habilidades detectivescas son suficientes para resolver el caso.\n"
          "Aunque claro, pudo haber muerto de un infarto o algo así, de todos modos, estás aburrido y esto puede ser interesante.\n")
    while n_preguntas <=7:
        pregunta = int(input("\nQué quieres hacer?\n"
                             "1) Interrogar a alguien\n"
                             "2) Investigar un lugar\n"
                             "3) Investigar un arma\n"))
        if pregunta == 1:
            p_persona = int(input("\nA quién quieres interrogar?\n"
                                  "1) El profe.\n"
                                  "2) Ricardo, el modelo de ropa interior.\n"
                                  "3) Mi ex.\n"
                                  "4) Putin.\n"
                                  "5) Mamá lucha."
                                  "6) El panadero con el pan.\n"
                                  "7) Hermanastra más fea (Sherk)\n"
                                  "8) Tulio Triviño.\n"))
            if p_persona == 1:
                print("\nLe preguntas al profe qué hizo en los últimos minutos, y él contesta:\n"
                      "“Estoy a punto de esculpir una escultura en hielo, me dijeron que sostener un picahielo de manera sospechosa me ame ayudaría,\n"
                      "he meditado aquí en las escaleras un buen rato”. No sé quien le habrá dicho eso al profe, pero no sé cómo no se me ocurrió antes.\n"
                      "El profe mencionó ver al Panadero con el pan correr asustado.\n")
            elif p_persona == 2:
                print("Le preguntas a Ricardo qué ha estado haciendo en los últimos minutos:\n"
                      "“Tengo que mantenerme en forma, he hecho cardio en estas escaleras eléctricas durante 5 horas, la vida de un modelo es difícil”.\n"
                      "No tienes palabras, es raro verlo hacer ejercicio en las escaleras eléctricas.\n"
                      "Ricardo menciona haber escuchado algo, después de eso la figura de waifu cayó aquí.\n"
                      "No ayuda de nada, pero tampoco esperabas mucho de él.\n")
            elif p_persona == 3:
                print("\nCon resignación, le preguntas a tu ex qué ha hecho en los últimos minutos:\n"
                      "“Nada, Ricardo y yo discutimos, estamos saliendo, pero no me gusta como se ha comportado últimamente”.\n"
                      "Lo dice casi gruñendo, solo una vez la he visto tan enojada, fue cuando mi conejo hizo Nesquik en su bolso de diseñador.\n"
                      "Extraño a ese conejo.\n"
                      "Ella menciona que Mamá lucha y el Panadero con el pan estaban susurrando algo cerca del baño.\n")
            elif p_persona == 4:
                print("\n Con cuidado de no desconcentrarlo, le preguntas a Putin qué ha estado haciendo:\n"
                      "“He prracticado con este simuladorr de batalla desde ayerr. Es poco rrealista, ya que aquí ganan los Estados Unidos”.\n"
                      "No quieres meterte en problemas con ningún país, así que solo te alejas asintiendo.\n"
                      "Putin dice que no vio nada en este lugar, tal vez solo estaba muy centrado en el juego, tal vez no.\n")
            elif p_persona == 5:
                print("\nCon entusiasmo te acercas a Mama lucha y le preguntas sobre sus actividades en las últimas horas:\n"
                      "“He estado limpiando este baño, el Panadero con el pan y yo lo ensuciamos cuando…”.\n"
                      "La detienes antes de que continue, prefieres no saber.\n"
                      "Mama lucha también mencionó que vio a tu ex ir hacia las escaleras eléctricas con disimulo.")
            elif p_persona == 6:
                print("\n Te acercas al panadero. Le preguntas sobre lo que ha hecho en estas horas:\n"
                      "“Estaba… con Mamá lucha un tiempo, pero es demasiado ruda, hui cuando empezó a hacer llaves de lucha, debería ir a disculparme”.\n"
                      "Sientes lástima por el pobre hombre y lo que tuvo que vivir, a veces los hombres somos las víctimas.\n"
                      "El panadero menciona haber visto a tu ex por la zona de maquinitas\n")
            elif p_persona == 7:
                print("\nCuestionas a la Hermanastra más fea por sus actividades estos últimos momentos.\n"
                      "Pero no te contesta, solo observa las figuras con una especie de odio y fascinación.\n"
                      "Esto me parece atemorizante, por favor, hay que irnos.\n"
                      "Ella no dice nada, pero su sola mirada te comunica que ella vio a Putin asesinando a alguien en la zona de maquinitas.\n")
            elif p_persona == 8:
                print("\n Te acercas a Tulio, aguantando la tentación de decirle que estamos al aire, y le preguntas por lo que ha estado haciendo:\n"
                      "“He estado discutiendo con esta persona para que me devuelva mi dinero, pero no parece querer cooperar,\n"
                      "parece que no tiene ni idea de con quién habla, esto es un ultraje”.\n"
                      "La verdad es que su situación no te podría importar menos, pero al menos es una cuartada.\n"
                      "Tulio menciona que vio al Panadero con el pan asustado y algo preocupado, como si hubiera hecho algo malo.\n")
            time.sleep(20)
            clear()
        elif pregunta == 2:
            p_lugar = int(input("\nQué lugar quieres investigar?:\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if p_lugar == 1:
                print("\n Curioso, funcionan perfectamente, casi parece que alguien pudo repararlas antes de ser arrestado.\n"
                      "Ricardo está ejercitándose en las escaleras, haciendo cardio, como si no le sobraran músculos.\n"
                      "Hay una figura de waifu aquí, y se ve rara, ¿estará sucia?\n")
            elif p_lugar == 2:
                print("\n Está sorprendentemente limpio, si no contamos las babas en el suelo, seguramente fueron las personas que observan las figuras.\n"
                      "Es extraño como algunos se emocionan por cosas así.\n"
                      "La hermanastra más fea esta observando una figura, pero no sé si sea con deseo o solo con odio.\n")
            elif p_lugar == 3:
                print("\nCompletamente vacío, salvo por Tulio Triviño, quien se queja porque un juego no funcionó correctamente.\n"
                      "No creo que consiga un reembolso, hay un letrero que especifica que no hay devoluciones a marionetas.\n"
                      "Me parece racista\n")
            elif p_lugar == 4:
                print("\n Hay una especie de botón para una consola, alguien debió olvidarlo aquí, es una lástima, es un buen botón.\n"
                      "El profe sostiene el picahielos de una manera muy amenazadora, mejor me voy.\n")
            elif p_lugar == 5:
                print("\n Hay vómito en este lugar, parece que alguien comió una baraja entera de cartas.\n"
                      "No sabía que estaban en el menú. Es asqueroso, pero no parece haber signos de violencia.\n"
                      "Mi ex está sentada sosteniendo una tanga de hule, no sé como puede tocar esa cosa, pero no se ve muy feliz.\n")
            elif p_lugar == 6:
                print("\nUn cuchillo está atravesando la cabeza de una vaca, eso de verdad es brutal.\n"
                      "Lamentablemente estás aquí para investigar un caso humano, pero nadie niega que la crueldad animal es un crimen.\n"
                      "Además de eso, creo que todo aquí es normal.\n")
            elif p_lugar == 7:
                print("\n : Algunos juegos rotos, pantallas hechas pedazos, creo que hay sangre, pero podría ser cátsup, no lo sé.\n"
                      "Lo que sí sé es que aquí hubo una kill, pero… ¿será en COD?\n"
                      "Hablando de COD, Putin está jugando, parece ser muy bueno, y ni siquiera está usando las manos.\n"
                      "Parece que tiene un amuleto de la suerte, ¿qué será?\n")
            elif p_lugar == 8:
                print("\n Wow, esto es sorprendente, está completamente limpio, Mamá lucha parece estar limpiando.\n"
                      "No es una conclusión machista, de verdad lo está haciendo.\n")
            time.sleep(20)
            clear()
        elif pregunta == 3:
            p_arma = int(input("\nQué arma quieres investigar?:\n"
                               "1) Tanga de hule\n"
                               "2) Picahielo\n"
                               "3) Figura de wuaifu\n"
                               "4) Cuchillo\n"
                               "5) Lapiz muy, muy filoso\n"
                               "6) Tijeras para zurdos\n"
                               "7) Veneno para rata\n"
                               "8) Calceta con mantequilla\n"))
            if p_arma == 1:
                print("\n La tiene mi ex en las mesas de juegos. Parece que la sostiene con ira, pero tal vez sea solo porque yo estoy aquí.\n")
            elif p_arma == 2:
                print("\nEl profe lo está sosteniendo de una manera extraña en las escaleras normales, me da miedo preguntar qué hace, pero sé que de todos modos lo harás.\n")
            elif p_arma == 3:
                print("\n : Está en las escaleras eléctricas, parece que alguien la dejó aquí mientras intentaba huir.\n"
                      "No me sorprende, está manchada de sangre.\n")
            elif p_arma == 4:
                print("\nEstá clavado en la cabeza de una vaca en el piso de comida.\n"
                      "No cabe duda de que está manchado de sangre. Lo siento vaquita, te haré justicia después de este caso.\n")
            elif p_arma == 5:
                print("\nEl panadero con el pan lo está usando para escribir. Parece apurado.\n")
            elif p_arma == 6:
                print("\nPor alguna razón están en el piso de los videojuegos, no sé por qué están ahí, pero están.\n"
                      "Parece que se usaron recientemente, pero no están dañadas.\n")
            elif p_arma == 7:
                print("\n Está en el baño. Alguien la usó recientemente, espero que no sea para algún siniestro propósito.\n")
            elif p_arma == 8:
                print("\nPutin usa la calceta con mantequilla como amuleto de la buena suerte.\n"
                      "Dudo que funcione, pero yo no conozco sus costumbres rusas.\n")
            time.sleep(20)
            clear()
        n_preguntas = n_preguntas + 1
    clear()
    if n_preguntas >= 7:
        r_arma = int(input("\n\n\nSe acabaron las preguntas, espero que sepas quién es el asesino:\n"
                           "Qué arma usaron para cometer el asesinato?:\n"
                           "1) Tanga de hule\n"
                           "2) Pica hielo\n"
                           "3) Figura de wuaifu\n"
                           "4) Cuchillo\n"
                           "5) Lapiz muy, muy filoso \n"
                           "6) Tijeras para zurdos\n"
                           "7) Veneno para rata\n"
                           "8) Calceta con mantequilla\n"))
        if r_arma == 1:
            r_lugar = int(input("En qué lugar se cometió el asesinato?\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if r_lugar == 1:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print("Acusas al profe de ser el asesino. ¿De verdad creyó que eso de la escultura te engañaría?, pues hoy no amigo.\n"
                          "Lamentablemente te equivocaste, y el maestro no está muy feliz de verte después del juicio, y tampoco lo está su picahielos.")
                elif r_persona == 2:
                    print("\nAcusas a Ricardo de ser el asesino. Y no estás muy seguro de el por qué.\n"
                          "Creo que solo hiciste una ruleta al azar y escogiste al primero que cayó.\n"
                          "Como sea, él es inocente, obviamente, pero no te culpa de nada, parece que huir de la ley fue un mejor cardio.\n")
                elif r_persona == 3:
                    print("\n: Acusas a tu ex de ser la asesina, pero por falta de pruebas no es procesada. La parte buena es que tu ex te persigue, para bien o para mal, suerte con la loca campeón.\n")
                elif r_persona == 4:
                    print("\nAcusas a Putin, el cual se encuentra muy ofendido. Deja el lugar tranquilamente montado en su oso mascota.\n"
                          "No parece importarle el sistema de justicia de este país.\n"
                          "Como sea, él era inocente y ahora tendrás que vivir con las consecuencias de haber ofendido al rey de Rusia… es un rey, ¿verdad?\n")
                elif r_persona == 5:
                    print("\nAcusas a mamá lucha de ser la asesina, además de faltas hacia la moral en el baño.\n"
                          "No era la asesina y ahora también rompiste una relación, felicidades.\n")
                elif r_persona == 6:
                    print("\nPobre panadero, tan asustado que estaba y tú lo inculpas. Es inocente, por si no te ha quedado claro. Pero aceptó la culpa por alguna razón.\n"
                          "El mundo se quedó sin pan y tú sin credibilidad.")
                elif r_persona == 7:
                    print("\nAcusas a la Hermanastra más fea, su silencio fue demasiado sospechoso.\n"
                          "Pero el hecho de que alguien es callado no significa que sea un maniaco asesino, al menos no en este caso.\n"
                          "De todas formas, a pesar de su inocencia, la Hermanastra más fea presenta cargos, no se sabe muy bien por qué.\n")
                elif r_persona == 8:
                    print("\nAcusas a el presentador del programa 31 minutos de ser el asesino,\n"
                          "si no estuviera tan furioso por ser discriminado por su estado de marioneta, de seguro tomaría represalias contra ti.\n"
                          "Por si no lo has entendido, Tulio es inocente.\n")
                print("Lo siento, más suerte a la próxima, no te rindas, ya estabas muy cerca, más o menos.\n")
        elif r_arma == 2:
            r_lugar = int(input("En qué lugar se cometió el asesinato?\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if r_lugar == 1:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print(
                        "Acusas al profe de ser el asesino. ¿De verdad creyó que eso de la escultura te engañaría?, pues hoy no amigo.\n"
                        "Lamentablemente te equivocaste, y el maestro no está muy feliz de verte después del juicio, y tampoco lo está su picahielos.")
                elif r_persona == 2:
                    print("\nAcusas a Ricardo de ser el asesino. Y no estás muy seguro de el por qué.\n"
                          "Creo que solo hiciste una ruleta al azar y escogiste al primero que cayó.\n"
                          "Como sea, él es inocente, obviamente, pero no te culpa de nada, parece que huir de la ley fue un mejor cardio.\n")
                elif r_persona == 3:
                    print(
                        "\n: Acusas a tu ex de ser la asesina, pero por falta de pruebas no es procesada. La parte buena es que tu ex te persigue, para bien o para mal, suerte con la loca campeón.\n")
                elif r_persona == 4:
                    print(
                        "\nAcusas a Putin, el cual se encuentra muy ofendido. Deja el lugar tranquilamente montado en su oso mascota.\n"
                        "No parece importarle el sistema de justicia de este país.\n"
                        "Como sea, él era inocente y ahora tendrás que vivir con las consecuencias de haber ofendido al rey de Rusia… es un rey, ¿verdad?\n")
                elif r_persona == 5:
                    print("\nAcusas a mamá lucha de ser la asesina, además de faltas hacia la moral en el baño.\n"
                          "No era la asesina y ahora también rompiste una relación, felicidades.\n")
                elif r_persona == 6:
                    print(
                        "\nPobre panadero, tan asustado que estaba y tú lo inculpas. Es inocente, por si no te ha quedado claro. Pero aceptó la culpa por alguna razón.\n"
                        "El mundo se quedó sin pan y tú sin credibilidad.")
                elif r_persona == 7:
                    print("\nAcusas a la Hermanastra más fea, su silencio fue demasiado sospechoso.\n"
                          "Pero el hecho de que alguien es callado no significa que sea un maniaco asesino, al menos no en este caso.\n"
                          "De todas formas, a pesar de su inocencia, la Hermanastra más fea presenta cargos, no se sabe muy bien por qué.\n")
                elif r_persona == 8:
                    print("\nAcusas a el presentador del programa 31 minutos de ser el asesino,\n"
                          "si no estuviera tan furioso por ser discriminado por su estado de marioneta, de seguro tomaría represalias contra ti.\n"
                          "Por si no lo has entendido, Tulio es inocente.\n")
                print("Lo siento, más suerte a la próxima, no te rindas, ya estabas muy cerca, más o menos.\n")
        elif r_arma == 3:
            r_lugar = int(input("En qué lugar se cometió el asesinato?\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if r_lugar == 1:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print(
                        "Acusas al profe de ser el asesino. ¿De verdad creyó que eso de la escultura te engañaría?, pues hoy no amigo.\n"
                        "Lamentablemente te equivocaste, y el maestro no está muy feliz de verte después del juicio, y tampoco lo está su picahielos.")
                elif r_persona == 2:
                    print("\nAcusas a Ricardo de ser el asesino. Y no estás muy seguro de el por qué.\n"
                          "Creo que solo hiciste una ruleta al azar y escogiste al primero que cayó.\n"
                          "Como sea, él es inocente, obviamente, pero no te culpa de nada, parece que huir de la ley fue un mejor cardio.\n")
                elif r_persona == 3:
                    print("\nAcusas a tu ex de ser la asesina, y la verdad no te sorprende que lo sea, ya sospechabas que no había algo bien con ella,\n"
                          "parece que cometió el asesinato por celos, parece que Paquita había coqueteado con Ricardo.\n"
                          "Aunque no sabes si le hizo un favor al mundo, la enviaste a la cárcel.\n")
                    print ("\n¡Felicidades!, ¡encerraste a tu ex!, ah, y también descubriste al asesino, hoy fue ganar ganar para todo el mundo.\n")
                elif r_persona == 4:
                    print(
                        "\nAcusas a Putin, el cual se encuentra muy ofendido. Deja el lugar tranquilamente montado en su oso mascota.\n"
                        "No parece importarle el sistema de justicia de este país.\n"
                        "Como sea, él era inocente y ahora tendrás que vivir con las consecuencias de haber ofendido al rey de Rusia… es un rey, ¿verdad?\n")
                elif r_persona == 5:
                    print("\nAcusas a mamá lucha de ser la asesina, además de faltas hacia la moral en el baño.\n"
                          "No era la asesina y ahora también rompiste una relación, felicidades.\n")
                elif r_persona == 6:
                    print(
                        "\nPobre panadero, tan asustado que estaba y tú lo inculpas. Es inocente, por si no te ha quedado claro. Pero aceptó la culpa por alguna razón.\n"
                        "El mundo se quedó sin pan y tú sin credibilidad.")
                elif r_persona == 7:
                    print("\nAcusas a la Hermanastra más fea, su silencio fue demasiado sospechoso.\n"
                          "Pero el hecho de que alguien es callado no significa que sea un maniaco asesino, al menos no en este caso.\n"
                          "De todas formas, a pesar de su inocencia, la Hermanastra más fea presenta cargos, no se sabe muy bien por qué.\n")
                elif r_persona == 8:
                    print("\nAcusas a el presentador del programa 31 minutos de ser el asesino,\n"
                          "si no estuviera tan furioso por ser discriminado por su estado de marioneta, de seguro tomaría represalias contra ti.\n"
                          "Por si no lo has entendido, Tulio es inocente.\n")
        elif r_arma == 4:
            r_lugar = int(input("En qué lugar se cometió el asesinato?\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if r_lugar == 1:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print(
                        "Acusas al profe de ser el asesino. ¿De verdad creyó que eso de la escultura te engañaría?, pues hoy no amigo.\n"
                        "Lamentablemente te equivocaste, y el maestro no está muy feliz de verte después del juicio, y tampoco lo está su picahielos.")
                elif r_persona == 2:
                    print("\nAcusas a Ricardo de ser el asesino. Y no estás muy seguro de el por qué.\n"
                          "Creo que solo hiciste una ruleta al azar y escogiste al primero que cayó.\n"
                          "Como sea, él es inocente, obviamente, pero no te culpa de nada, parece que huir de la ley fue un mejor cardio.\n")
                elif r_persona == 3:
                    print(
                        "\n: Acusas a tu ex de ser la asesina, pero por falta de pruebas no es procesada. La parte buena es que tu ex te persigue, para bien o para mal, suerte con la loca campeón.\n")
                elif r_persona == 4:
                    print(
                        "\nAcusas a Putin, el cual se encuentra muy ofendido. Deja el lugar tranquilamente montado en su oso mascota.\n"
                        "No parece importarle el sistema de justicia de este país.\n"
                        "Como sea, él era inocente y ahora tendrás que vivir con las consecuencias de haber ofendido al rey de Rusia… es un rey, ¿verdad?\n")
                elif r_persona == 5:
                    print("\nAcusas a mamá lucha de ser la asesina, además de faltas hacia la moral en el baño.\n"
                          "No era la asesina y ahora también rompiste una relación, felicidades.\n")
                elif r_persona == 6:
                    print(
                        "\nPobre panadero, tan asustado que estaba y tú lo inculpas. Es inocente, por si no te ha quedado claro. Pero aceptó la culpa por alguna razón.\n"
                        "El mundo se quedó sin pan y tú sin credibilidad.")
                elif r_persona == 7:
                    print("\nAcusas a la Hermanastra más fea, su silencio fue demasiado sospechoso.\n"
                          "Pero el hecho de que alguien es callado no significa que sea un maniaco asesino, al menos no en este caso.\n"
                          "De todas formas, a pesar de su inocencia, la Hermanastra más fea presenta cargos, no se sabe muy bien por qué.\n")
                elif r_persona == 8:
                    print("\nAcusas a el presentador del programa 31 minutos de ser el asesino,\n"
                          "si no estuviera tan furioso por ser discriminado por su estado de marioneta, de seguro tomaría represalias contra ti.\n"
                          "Por si no lo has entendido, Tulio es inocente.\n")
                print("Lo siento, más suerte a la próxima, no te rindas, ya estabas muy cerca, más o menos.\n")
        elif r_arma == 5:
            r_lugar = int(input("En qué lugar se cometió el asesinato?\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if r_lugar == 1:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print(
                        "Acusas al profe de ser el asesino. ¿De verdad creyó que eso de la escultura te engañaría?, pues hoy no amigo.\n"
                        "Lamentablemente te equivocaste, y el maestro no está muy feliz de verte después del juicio, y tampoco lo está su picahielos.")
                elif r_persona == 2:
                    print("\nAcusas a Ricardo de ser el asesino. Y no estás muy seguro de el por qué.\n"
                          "Creo que solo hiciste una ruleta al azar y escogiste al primero que cayó.\n"
                          "Como sea, él es inocente, obviamente, pero no te culpa de nada, parece que huir de la ley fue un mejor cardio.\n")
                elif r_persona == 3:
                    print(
                        "\n: Acusas a tu ex de ser la asesina, pero por falta de pruebas no es procesada. La parte buena es que tu ex te persigue, para bien o para mal, suerte con la loca campeón.\n")
                elif r_persona == 4:
                    print(
                        "\nAcusas a Putin, el cual se encuentra muy ofendido. Deja el lugar tranquilamente montado en su oso mascota.\n"
                        "No parece importarle el sistema de justicia de este país.\n"
                        "Como sea, él era inocente y ahora tendrás que vivir con las consecuencias de haber ofendido al rey de Rusia… es un rey, ¿verdad?\n")
                elif r_persona == 5:
                    print("\nAcusas a mamá lucha de ser la asesina, además de faltas hacia la moral en el baño.\n"
                          "No era la asesina y ahora también rompiste una relación, felicidades.\n")
                elif r_persona == 6:
                    print(
                        "\nPobre panadero, tan asustado que estaba y tú lo inculpas. Es inocente, por si no te ha quedado claro. Pero aceptó la culpa por alguna razón.\n"
                        "El mundo se quedó sin pan y tú sin credibilidad.")
                elif r_persona == 7:
                    print("\nAcusas a la Hermanastra más fea, su silencio fue demasiado sospechoso.\n"
                          "Pero el hecho de que alguien es callado no significa que sea un maniaco asesino, al menos no en este caso.\n"
                          "De todas formas, a pesar de su inocencia, la Hermanastra más fea presenta cargos, no se sabe muy bien por qué.\n")
                elif r_persona == 8:
                    print("\nAcusas a el presentador del programa 31 minutos de ser el asesino,\n"
                          "si no estuviera tan furioso por ser discriminado por su estado de marioneta, de seguro tomaría represalias contra ti.\n"
                          "Por si no lo has entendido, Tulio es inocente.\n")
                print("Lo siento, más suerte a la próxima, no te rindas, ya estabas muy cerca, más o menos.\n")
        elif r_arma == 6:
            r_lugar = int(input("En qué lugar se cometió el asesinato?\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if r_lugar == 1:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print(
                        "Acusas al profe de ser el asesino. ¿De verdad creyó que eso de la escultura te engañaría?, pues hoy no amigo.\n"
                        "Lamentablemente te equivocaste, y el maestro no está muy feliz de verte después del juicio, y tampoco lo está su picahielos.")
                elif r_persona == 2:
                    print("\nAcusas a Ricardo de ser el asesino. Y no estás muy seguro de el por qué.\n"
                          "Creo que solo hiciste una ruleta al azar y escogiste al primero que cayó.\n"
                          "Como sea, él es inocente, obviamente, pero no te culpa de nada, parece que huir de la ley fue un mejor cardio.\n")
                elif r_persona == 3:
                    print(
                        "\n: Acusas a tu ex de ser la asesina, pero por falta de pruebas no es procesada. La parte buena es que tu ex te persigue, para bien o para mal, suerte con la loca campeón.\n")
                elif r_persona == 4:
                    print(
                        "\nAcusas a Putin, el cual se encuentra muy ofendido. Deja el lugar tranquilamente montado en su oso mascota.\n"
                        "No parece importarle el sistema de justicia de este país.\n"
                        "Como sea, él era inocente y ahora tendrás que vivir con las consecuencias de haber ofendido al rey de Rusia… es un rey, ¿verdad?\n")
                elif r_persona == 5:
                    print("\nAcusas a mamá lucha de ser la asesina, además de faltas hacia la moral en el baño.\n"
                          "No era la asesina y ahora también rompiste una relación, felicidades.\n")
                elif r_persona == 6:
                    print(
                        "\nPobre panadero, tan asustado que estaba y tú lo inculpas. Es inocente, por si no te ha quedado claro. Pero aceptó la culpa por alguna razón.\n"
                        "El mundo se quedó sin pan y tú sin credibilidad.")
                elif r_persona == 7:
                    print("\nAcusas a la Hermanastra más fea, su silencio fue demasiado sospechoso.\n"
                          "Pero el hecho de que alguien es callado no significa que sea un maniaco asesino, al menos no en este caso.\n"
                          "De todas formas, a pesar de su inocencia, la Hermanastra más fea presenta cargos, no se sabe muy bien por qué.\n")
                elif r_persona == 8:
                    print("\nAcusas a el presentador del programa 31 minutos de ser el asesino,\n"
                          "si no estuviera tan furioso por ser discriminado por su estado de marioneta, de seguro tomaría represalias contra ti.\n"
                          "Por si no lo has entendido, Tulio es inocente.\n")
                print("Lo siento, más suerte a la próxima, no te rindas, ya estabas muy cerca, más o menos.\n")
        elif r_arma == 7:
            r_lugar = int(input("En qué lugar se cometió el asesinato?\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if r_lugar == 1:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print(
                        "Acusas al profe de ser el asesino. ¿De verdad creyó que eso de la escultura te engañaría?, pues hoy no amigo.\n"
                        "Lamentablemente te equivocaste, y el maestro no está muy feliz de verte después del juicio, y tampoco lo está su picahielos.")
                elif r_persona == 2:
                    print("\nAcusas a Ricardo de ser el asesino. Y no estás muy seguro de el por qué.\n"
                          "Creo que solo hiciste una ruleta al azar y escogiste al primero que cayó.\n"
                          "Como sea, él es inocente, obviamente, pero no te culpa de nada, parece que huir de la ley fue un mejor cardio.\n")
                elif r_persona == 3:
                    print(
                        "\n: Acusas a tu ex de ser la asesina, pero por falta de pruebas no es procesada. La parte buena es que tu ex te persigue, para bien o para mal, suerte con la loca campeón.\n")
                elif r_persona == 4:
                    print(
                        "\nAcusas a Putin, el cual se encuentra muy ofendido. Deja el lugar tranquilamente montado en su oso mascota.\n"
                        "No parece importarle el sistema de justicia de este país.\n"
                        "Como sea, él era inocente y ahora tendrás que vivir con las consecuencias de haber ofendido al rey de Rusia… es un rey, ¿verdad?\n")
                elif r_persona == 5:
                    print("\nAcusas a mamá lucha de ser la asesina, además de faltas hacia la moral en el baño.\n"
                          "No era la asesina y ahora también rompiste una relación, felicidades.\n")
                elif r_persona == 6:
                    print(
                        "\nPobre panadero, tan asustado que estaba y tú lo inculpas. Es inocente, por si no te ha quedado claro. Pero aceptó la culpa por alguna razón.\n"
                        "El mundo se quedó sin pan y tú sin credibilidad.")
                elif r_persona == 7:
                    print("\nAcusas a la Hermanastra más fea, su silencio fue demasiado sospechoso.\n"
                          "Pero el hecho de que alguien es callado no significa que sea un maniaco asesino, al menos no en este caso.\n"
                          "De todas formas, a pesar de su inocencia, la Hermanastra más fea presenta cargos, no se sabe muy bien por qué.\n")
                elif r_persona == 8:
                    print("\nAcusas a el presentador del programa 31 minutos de ser el asesino,\n"
                          "si no estuviera tan furioso por ser discriminado por su estado de marioneta, de seguro tomaría represalias contra ti.\n"
                          "Por si no lo has entendido, Tulio es inocente.\n")
                print("Lo siento, más suerte a la próxima, no te rindas, ya estabas muy cerca, más o menos.\n")
        elif r_arma == 8:
            r_lugar = int(input("En qué lugar se cometió el asesinato?\n"
                                "1) Escaleras eléctricas\n"
                                "2) Piso de figuras\n"
                                "3) Piso de videojuegos\n"
                                "4) Escaleras normales\n"
                                "5) Mesas de juegos\n"
                                "6) Piso de comida\n"
                                "7) Zona de maquinitas\n"
                                "8) Baños\n"))
            if r_lugar == 1:
                r_persona = int(input("Ahora, quién crees que es el asesino?\n"
                                      "1) El profe\n"
                                      "2) Ricardo, el modelo de ropa interior\n"
                                      "3) Mi ex\n"
                                      "4) Putin\n"
                                      "5) Mamá lucha\n"
                                      "6) El panadero con el pan\n"
                                      "7) Hermanastra más fea (Sherk)\n"
                                      "8) Tulio Triviño\n"))
                if r_persona == 1:
                    print(
                        "Acusas al profe de ser el asesino. ¿De verdad creyó que eso de la escultura te engañaría?, pues hoy no amigo.\n"
                        "Lamentablemente te equivocaste, y el maestro no está muy feliz de verte después del juicio, y tampoco lo está su picahielos.")
                elif r_persona == 2:
                    print("\nAcusas a Ricardo de ser el asesino. Y no estás muy seguro de el por qué.\n"
                          "Creo que solo hiciste una ruleta al azar y escogiste al primero que cayó.\n"
                          "Como sea, él es inocente, obviamente, pero no te culpa de nada, parece que huir de la ley fue un mejor cardio.\n")
                elif r_persona == 3:
                    print(
                        "\n: Acusas a tu ex de ser la asesina, pero por falta de pruebas no es procesada. La parte buena es que tu ex te persigue, para bien o para mal, suerte con la loca campeón.\n")
                elif r_persona == 4:
                    print(
                        "\nAcusas a Putin, el cual se encuentra muy ofendido. Deja el lugar tranquilamente montado en su oso mascota.\n"
                        "No parece importarle el sistema de justicia de este país.\n"
                        "Como sea, él era inocente y ahora tendrás que vivir con las consecuencias de haber ofendido al rey de Rusia… es un rey, ¿verdad?\n")
                elif r_persona == 5:
                    print("\nAcusas a mamá lucha de ser la asesina, además de faltas hacia la moral en el baño.\n"
                          "No era la asesina y ahora también rompiste una relación, felicidades.\n")
                elif r_persona == 6:
                    print(
                        "\nPobre panadero, tan asustado que estaba y tú lo inculpas. Es inocente, por si no te ha quedado claro. Pero aceptó la culpa por alguna razón.\n"
                        "El mundo se quedó sin pan y tú sin credibilidad.")
                elif r_persona == 7:
                    print("\nAcusas a la Hermanastra más fea, su silencio fue demasiado sospechoso.\n"
                          "Pero el hecho de que alguien es callado no significa que sea un maniaco asesino, al menos no en este caso.\n"
                          "De todas formas, a pesar de su inocencia, la Hermanastra más fea presenta cargos, no se sabe muy bien por qué.\n")
                elif r_persona == 8:
                    print("\nAcusas a el presentador del programa 31 minutos de ser el asesino,\n"
                          "si no estuviera tan furioso por ser discriminado por su estado de marioneta, de seguro tomaría represalias contra ti.\n"
                          "Por si no lo has entendido, Tulio es inocente.\n")
                print("Lo siento, más suerte a la próxima, no te rindas, ya estabas muy cerca, más o menos.\n")