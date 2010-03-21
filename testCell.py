import cell
import graphDrawer

solution = cell.Solution(24000.0)
solution.addCell(1000.0)

solution.metabolites['AB'].amount = 2400.0

solution.cells[0].addProtein('transporter-AB', 10.0)
solution.cells[0].addProtein('transporter-A', 10.0)
solution.cells[0].addProtein('enzyme-ABase', 20.0)

graph = graphDrawer.Graph()
graphSeries = { 'Cell A':  solution.cells[0].metabolites['A'],
                'Cell B':  solution.cells[0].metabolites['B'],
                'Cell AB': solution.cells[0].metabolites['AB'],
                'Soln A': solution.metabolites['A'],
                'Soln AB': solution.metabolites['AB']}

for g in graphSeries.keys():
    graph.addSeries(g)

for t in range(1000):
    for g in graphSeries.keys():
        graph.addDataToSeries(g, 100*graphSeries[g].amount/graphSeries[g].volume)

    for cell in solution.cells:
        cell.update()

solution.cells[0].output()
solution.output()

graph.outputSeries('test', graph.series.keys())
