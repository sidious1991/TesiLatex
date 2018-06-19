for i in range(0,len(strategies)):
        
        round_graph = nx.read_gpickle(path)
        round_data = initGraphData;
        #sorted_x_y = ut.sortNodes(None, g, initGraphData[8], initGraphData[9], i)#sorted by type sorting 'i'
        r1= r;
        print strategies[i]+' \n'
        print "rwc initial",r1[0], len(round_graph.edges())

        for k in range(0,edges_to_recommend): 
             
            R = []
  
            sorted_x_y = ut.sortNodes(None, round_graph, round_data[8], round_data[9], i)#sorted by type sorting 'i'
            sorted_dp = rwc_lib.deltaPredictorOrdered(None, round_graph, 0.85, k1, k2, sorted_x_y, round_data, r1)

            R.append(rwc_lib.fagin(sorted_dp,1))
            
            print R[0][1]
            
            (round_graph,opt,ratio,max_opt) = ut.addEdgeToGraph(None,round_graph,R[0][0],R[0][1],graph_name,strategies[i])
            
            #We assume that communities and partition do not change
            round_data = ut.computeData(None, round_graph, 0.85, i, percent_community=1, comms_part=(round_data[8],round_data[9]))  
            
            r1 = rwc_lib.rwc(0.85, round_data)
            
            print "rwc",r1[0]
            
        print "RWC score after addiction of accepted edges =%13.10f"%r1[0] #%width.precisionf
        print "Real Total Decrease RWC =%13.10f"%(r[0]-r1[0])
        print "-----------------------------------------------"
      
    print "-------------------------------------------------End of simulation---------------------------------------------------------"  

