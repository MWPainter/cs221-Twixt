from twixt import twixtBoard
import agent
from util import printc, bcolors

n = 8
iter = 1
depth = 1
width = 4
agent = [agent.MCTreeSearch(agent.uniformPolicy, agent.uniformPolicy, 10000), agent.PureMCAgent(10000)]

def drawBoard(n, labels, assignments, bridges):
	for i in range(n):
		for j in range(n):
			if (i == 0 or i == n-1) and (j == 0 or j == n-1):
				print "%-*s" % (width, ""),
			else:
				if (i,j) in labels:
					if labels[(i,j)] in assignments[0]:
						#printc("%-*s" % (width, assignments[0][labels[(i,j)]])),
						if (i,j) in bridges:
							printc('O', bcolors.OKBLUE, 'bold'),
						else:
							printc('O'),
					elif labels[(i,j)] in assignments[1]:
						#printc("%-*s" % (width, assignments[1][labels[(i,j)]]), bcolors.FAIL),
						if (i,j) in bridges:
							printc('O', bcolors.FAIL, 'bold'),
						else:
							printc('O', bcolors.FAIL),
				else:
					print "%-*s" % (width, "x"),
			if j == n-1:
				print "\n"

tb = twixtBoard(n)
while tb.winner() == -1:
    print "iteration: ", iter
    iter += 1


    action = agent[tb.agent].getAction(tb)
    #print "agent, action: ", tb.agent, action
    tb.updateBoard(action)
    #print "pins: ", tb.pins
    #print "bridges: ", tb.bridges
    drawBoard(n, tb.label, tb.assignment, tb.bridges)

print tb.winner()

