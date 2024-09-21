def start(color='linen'):
  clearscreen()
  setup(400,400)
  showborder()
  bgcolor(color)
  speed(0)

def xycirc_rc(x,y,r):
  setheading(0)
  pu()
  goto(x,y-r)
  pd()
  circle(r)
