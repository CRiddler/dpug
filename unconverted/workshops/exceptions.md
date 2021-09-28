---
dpug:
  author: Cameron Riddell
  date: '2021-07-20'
jupytext:
  formats: md:myst
  notebook_metadata_filter: dpug,rise
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
rise:
  scroll: true
---

+++ {"slideshow": {"slide_type": "slide"}}

# Exceptions - Following a traceback
This workshop will help you understand how to read and understand error messages in python.

+++ {"slideshow": {"slide_type": "subslide"}}

<pre>
<span class="ansi-red-fg">---------------------------------------------------------------------------</span>
<span class="ansi-red-fg">KeyError</span>                                  Traceback (most recent call last)
<span class="ansi-green-fg">&lt;ipython-input-45-1b6d4eed09ff&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span>
<span class="ansi-green-intense-fg ansi-bold">      9</span>     <span class="ansi-green-fg">return</span> message
<span class="ansi-green-intense-fg ansi-bold">     10</span> 
<span class="ansi-green-fg">---&gt; 11</span><span class="ansi-red-fg"> </span>hello_world<span class="ansi-blue-fg">(</span><span class="ansi-blue-fg">"m"</span><span class="ansi-blue-fg">)</span>

<span class="ansi-green-fg">&lt;ipython-input-45-1b6d4eed09ff&gt;</span> in <span class="ansi-cyan-fg">hello_world</span><span class="ansi-blue-fg">(shortcut)</span>
<span class="ansi-green-intense-fg ansi-bold">      6</span>     }
<span class="ansi-green-intense-fg ansi-bold">      7</span> 
<span class="ansi-green-fg">----&gt; 8</span><span class="ansi-red-fg">     </span>message <span class="ansi-blue-fg">=</span> msg_shortcuts<span class="ansi-blue-fg">[</span>shortcut<span class="ansi-blue-fg">]</span>
<span class="ansi-green-intense-fg ansi-bold">      9</span>     <span class="ansi-green-fg">return</span> message
<span class="ansi-green-intense-fg ansi-bold">     10</span> 

<span class="ansi-red-fg">KeyError</span>: 'm'
</pre>

+++ {"slideshow": {"slide_type": "slide"}}

## Terminology:
* **Error/Exception**: A simple message/value to inform a user that something unexpected has occurred and that the code should not continue running.

* **Traceback**: A traceback is a message that points to where in the code an error has occurred.

+++ {"slideshow": {"slide_type": "subslide"}}

## What happens when an error occurs?
* Hello

+++ {"slideshow": {"slide_type": "slide"}}

## Common exceptions and common causes
* SyntaxError - python can't read some of the code you wrote
* TypeError - 
* ValueError
* ModeuleNotFoundError
* IndexError
* NameError

+++ {"slideshow": {"slide_type": "slide"}}

### SyntaxError

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
tags: [raises-exception]
---
a = "1
```

```{code-cell} ipython3
---
slideshow:
  slide_type: notes
tags: [raises-exception]
---
a = (1, 2
```

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
tags: [raises-exception]
---
if True:
    pass
```

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
tags: [raises-exception]
---
a = (1, 2)

if True:
     print("hello")
```

+++ {"slideshow": {"slide_type": "slide"}}

### TypeError
**This exception may be raised by user code to indicate that an attempted operation on an object is not supported, and is not meant to be.** [documentation](https://docs.python.org/3/library/exceptions.html##TypeError)

It is often up to the associated message and user to interpret the specific meaning of a TypeError

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
integer_list = [1, 2, 3]
string_list = ["a", "b", "c", "d"]
```

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
sum(integer_list)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
tags: [raises-exception]
---
sum(string_list)
```

```{code-cell} ipython3
:tags: [raises-exception]

len(8)
```

```{code-cell} ipython3
:tags: [raises-exception]

len("123", "a")
```

+++ {"heading_collapsed": true}

### ValueError

+++

### ModuleNotFoundError

```{code-cell} ipython3
## import does_not_exist
```

```{code-cell} ipython3
import itertools
```

```{code-cell} ipython3
## import itertols
```

+++ {"heading_collapsed": true}

### IndexError

+++ {"heading_collapsed": true}

### KeyError

+++ {"slideshow": {"slide_type": "slide"}}

### NameError
* Typo in variable name
* Especially important in notebooks!!!

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
tags: [raises-exception]
---
memoization = 0
print(memoizaton)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
tags: [raises-exception]
---
print(g)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
g = "hello world"
```

+++ {"slideshow": {"slide_type": "slide"}}

## Tracebacks with other code
So far we have only discussed errors where the only code in the traceback is code we've written. How do we scan through much longer error messages that include a lot of foreign code?

* import some standard lib, put in bad input, make error as confusing as possible.
* highlight "code I wrote vs code some one else wrote"
* solve the error
* The more nested functions become, the more complex the traceback!

```{code-cell} ipython3
## list("123", 5)
```

```{code-cell} ipython3
## if 1:
##     if 3:
##         print(((123))

## if 2:
##     print(123)
```

+++ {"slideshow": {"slide_type": "slide"}}

## Seeking help - How to ask a good question

+++ {"slideshow": {"slide_type": "slide"}}

## Challenge!
