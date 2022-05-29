# Behaviour testing
The implementation of complicated rules is not always easy to read.
A good way to document and explain the behaviour of rule engines are natural language tests.
A frame work we use for that is [jgiven](http://jgiven.org/). 
We write the tests using the [dataprovider] (https://github.com/TNG/junit-dataprovider) runner.
This is basically a runner that allows to use parametrized tests. 

The basic testing frame work is still [JUnit4](http://junit.org/), assertions are made using [hamcrest](https://code.google.com/p/hamcrest/wiki/Tutorial) and we mock complicated input classes with [mockito](http://mockito.org/).
