"""
An irrigation machine
You're going to automate the watering of farm parcels by making an intelligent irrigation machine. Multi-label classification problems differ from multi-class problems in that each observation can be labeled with zero or more classes. So classes/labels are not mutually exclusive, you could water all, none or any combination of farm parcels based on the inputs.

To account for this behavior what we do is have an output layer with as many neurons as classes but this time, unlike in multi-class problems, each output neuron has a sigmoid activation function. This makes each neuron in the output layer able to output a number between 0 and 1 independently.

The Sequential() model and Dense() layers are ready to be used. It's time to build an intelligent irrigation machine!


Instructions
100 XP
Instantiate a Sequential() model.
Add a hidden layer of 64 neurons with as many input neurons as there are sensors and relu activation.
Add an output layer with as many neurons as parcels and sigmoidactivation.
Compile your model with the adam optimizer and binary_crossentropy loss.
"""

