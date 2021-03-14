# Week 1: Encapsulation

## Introduction

An object is fundamental piece of object-orientated programming.
It comprises of

- **DATA** in the form of *instance variables*
- **BEHAVIOUR** in the form of *methods*

In this first tutorial, we will write a class in Python that has some data and behaviour that will allow us to model a game of Monopoly.

## Data: Properties of the obeject

A object's data describes some property of the object.

For example, if an object was a Person, properties could include their

- Name
- Sex
- Age
- *etc.*

### Exercise 1: Adding the data to `MonopolyPlayer`

#### Goal

Write a simple **class** that models a Monopoly Player.

An object of class `MonopolyPlayer` will have the following data

- **Name,** the Player's name
- **Piece,** the player's Monopoly piece
- **Account,** the Player's bank account

#### Tasks

Using the skeleton class provided,

1. Write **declarations** for all the variables
2. Add a **Constructor**
3. Have the Constructor **initialise** all the variables to their default values

## Getters and setters: Methods to access and change our data

<!--add blurb-->

### Exercise 2: Adding get methods and set methods

Write getters and setters for `piece` and `account`, following the example given for `name`.

## Behaviour: Defining what our objects can do

An object's behaiour is how they respond to a message.
For an object to show behaviour, a corresponding method must exist in its *protocol.*
An object's protocol is the collection of messages it understands.

For example, our Person object could understand the message `jump()` by jumping up an down on the spot.

### Exercise 3: Defining the behaviour of an object

Write instance methods for the following messages

1. `describe()`
2. `is_same_player_as(a_player)`
3. `setup_player(a_name, a_piece, an_account)`

## Summary
