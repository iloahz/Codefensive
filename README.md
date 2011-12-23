Introduction
============

This is a geek thing trying to make the source code unreadable.  
Now(2011-7-3) I consider the final product to be a webpage, so ```PHP``` is chosen as the process language.  
Now I will start with ```C++``` source code, and I believe this project will be able to process more programming languages, so I will think carefully for the architecture. ^.^

Algorithm
=========

* Replace all the variables with different numbers of '\_'
* <del>Replace `if-else` with `?:`</del>
* <del>Transform loops(e.g. ```for```, ```while```, ```do-until```) to recursive functions</del>
* Replace constants with variables

Updates
=======

* Update 2011-7-5: Since I am not familiar with PHP....So I plan to use ```C++``` or ```Python``` as the process language. Still we can create a webpage with CGI to achieve the same function.

* Update 2011-12-23: PHP? What's that ridiculous? As I currently know, building an AST(Abstract syntax tree) would be the best choice, ```Python``` may be choosed as the processing language in order to support GAE. btw gcc is definitely unreadable.

* Update 2011-12-23: AST may not be needed.
