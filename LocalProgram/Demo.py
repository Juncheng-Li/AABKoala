from LocalProgram.graphRequest import *
from LocalProgram.resultRequest import *

r = resultRequest()
g = graphRequest()

#retrieveing all data from server
r.listResults()

#inserting new result into the database
# r.insertNewResult()

#plot this result and retrive the graph generated
# g.plot_graph([31],"history")

#update results
# r.updateResults()

#delete results
# r.deleteResultWithID("31")
