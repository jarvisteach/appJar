###PieChart ([beta](https://en.wikipedia.org/wiki/Software_release_life_cycle#BETA))  
---
Widget to depict a Pie Chart.  
It will automatically calculate percentages, and draw a pie chart, given a dictionary of items and their amount.  
The PieChart is purely for display purposes, and is not interactive, other than a simple mouse-over effect with a tooltip.  
![PieChart](../img/dev/pie.png)  

```python
from appJar import gui

app = gui()
app.addPieChart("p1", {"apples":50, "oranges":200, "grapes":75,
                        "beef":300, "turkey":150})
app.go()
```

####Add PieCharts  
* `.addPieChart(title, values)`  
    Takes a dictionary of names and values, which will be converted to percentages, and plotted on the chart.  
    The names will be used as part of tooltips that appear over each wedge of the PieChart.  

####Set PieCharts  
* `.setPieChart(title, name, value)`  
    Will update the PieChart, by either changing an existing value, adding a new value, or removing a value if it's set to 0.  
