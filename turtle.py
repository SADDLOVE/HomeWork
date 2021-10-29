#Задание выданное на лекции от 11.10.2021
#Напишите программу, чтобы понять как работает черепашья графика
import turtle

turtle.setup(800,800)
turtle.shape("turtle")
turtle.color("blue")
turtle.fd(50)
turtle.circle(200, 700)
turtle.color("black")
turtle.up()
turtle.fd(-50)
turtle.down()
turtle.circle(200, 700)
turtle.exitonclick()
turtle.mainloop()
