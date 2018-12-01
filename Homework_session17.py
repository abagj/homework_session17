#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 09:23:43 2018

@author: anikkengjeruldsen
"""

#%%
#Session 17
#Exercise white belt


inventory = {
    'Guitar': 1000,
    'Pick Box': 5,
    'Guitar Strings': 10,
    'Insurance': 5,
    'Priority mail': 10
}

per_cart_items = ('Insurance', 'Priority mail')

def checkout(cart, inventory=inventory, per_cart_items=per_cart_items):
    if len(cart) <= 0:
        raise RuntimeError('Shopping cart must not be empty')

   
    price = 0

    for item in per_cart_items:
        if item in cart:
            price += inventory[item]

    for item in cart:
        if item not in per_cart_items:
            price += inventory[item]

    return price

def test_checkout():
    test_carts = (
        ("Guitar", "Pick Box"),
        ("Guitar", "Guitar Strings"),
        ("Pick Box", "Guitar Strings")
    )

    expected = (1005, 1010, 15)

    for cart, price in zip(test_carts, expected):
        assert checkout(cart) == price

test_checkout()

#%%
#Session 17

#Excercise blue belt

def main():
    filename = input('Enter file name: ')
    try:
        f = open(filename)
        for line in f:
            print(line.upper().strip())
        f.close()
    except FileNotFoundError:
        print(filename + " is not found!")

main()



#%%
#session 17

#Excercise black belt

def copy_file(origin, destination):

    try:
        origin_file = open(origin)
        destination_file = open(destination, "w")
        
       #if len(origin_file.read) == 0
    
        for line in origin_file:
            destination_file.write(line)
    
     except Exception:
         print("something went wrong")


        
       
            
        
#%%     


