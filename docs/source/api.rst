Summary
=======

Input data
----------

Currently, **hello** is just a small tutorial

The idea
--------
Understand how to create a python module. It only have some small functionalities


#. :meth:`hello.register.Person`
#. :mod:`hello.utils`

Be aware that you can use LaTeX inside the documentation. For example, to calculate the average we do:

.. math::
    average = \frac{age_1 + age_2}{2}

Also we can put in-line math expressions :math:`a = 2 + 2 \neq 5` 

Average functions
-----------------

We can also put some nice python code inside of the docs


.. code-block:: python

    from hello.register import Person
    pepe = Person('pepe', (2000, 2, 3))
