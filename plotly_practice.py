import plotly.express as px

points = [
  { 'x': 1, 'y': 2 },
  { 'x': 2, 'y': 6 },
  { 'x': 3, 'y': 9 },
  { 'x': 4, 'y': 5 },
  { 'x': 5, 'y': 3 },
]

fig = px.line(points, x='x', y='y')

fig.write_html('fig.html', auto_open=True)
