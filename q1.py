"""
Encapsulation: This is about keeping fields within a class private, then providing access to them via public methods. It's a protective barrier that keeps the data and the code safe within the object, preventing external or unintended influences.
Usecase: In a BankAccount class, you can't just change the balance directly. You need to use methods like deposit() and withdraw() to add or take money safely. This helps prevent mistakes like taking out more money than you have.

Inheritance: This allows a class to inherit characteristics (methods and properties) from another class. It facilitates reuse and can simplify complex systems.
Usecase: There is a general class named Animal that has methods like eat() and sleep(). Other animal types, like Dog and Bird, start with these basic methods from Animal and can add their own specific behaviors. 
A Dog might add a bark() method, and a Bird could add a fly() method. Each specific animal gets to use the common methods of eating and sleeping, and also has its own special actions.

Polymorphism: This allows methods to do different things based on the object it is acting upon, which means the same method or operation may behave differently on different classes.
Usecase: Both a cat and a dog respond to the command "speak," but the sounds they make are different. In programming, you could use the speak() method on an animal object, and whether it's a dog or a cat, the correct sound comes out. 
You don't need to know if it's a dog or a cat for it to work.

Abstraction: This hides complex reality while exposing only the necessary parts. It helps in reducing programming complexity and effort.
Usecase: A Vehicle abstract class defines a method drive() that must be implemented by any subclass. This allows different types of vehicles like Car and Boat to implement specific driving behaviors tailored to their type while sharing the same interface. 
This abstraction hides the complexity of each vehicle's driving method from the user, who can use the drive method without knowing the details of vehicle operation.
"""