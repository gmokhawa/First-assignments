#Python Assignment From Gaone Gee Mokhawa Student Number 14M8501

#Question 1.This program computes the cost of of  a meal, including taxes and a tip

cost_of_meal=input("enter cost of meal ")
restaurant_tax= 6.75

tax_amount_paid= (restaurant_tax* cost_of_meal)/100
cost_of_meal_before_restaurant_tax=cost_of_meal-tax_amount_paid
#total_cost_paid = cost_of_meal + 10% tip
tip =(10* cost_of_meal)/100
total_cost_paid = cost_of_meal + tip 

print "cost before tax =R",cost_of_meal_before_restaurant_tax
print "6.75 % tax =R",tax_amount_paid
print "cost of meal =R",cost_of_meal
print "10% tip =R",tip
print "total cost paid =R",total_cost_paid
