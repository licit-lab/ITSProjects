FOR /L %%s IN (0,200,1000) DO (
    
    REM #### Boucle de simulation le s correspond à la varible, le 0 la premier valeur le 200 le pas et 1000 la derniere valeur ####
    REM #### Exemple de fichier batch pour des distances de communication differentes. Pour un d=[0,200,400,600,800,1000] m Attention il est preféerable d enlever les parametres dans la boucles pour pouvoir effectuer les simulations de maniere optimale. ####
    sumo -c traffic_light_sim.sumocfg --device.glosa.range %%s --tripinfo-output trip_info_test_%%s.xml --summary-output vsummary_%%s.xml --queue-output queue_%%s.xml  --fcd-output FCD_test_%%s.xml  --emission-output emission_test_%%s.xml 
    
    )