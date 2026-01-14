# STEP 2019 Paper 1 Question 1

## Problem 1
A straight line passes through (1, k), gradient = $-tan{theta}$, k > 0, $0 < theta < pi/2$. Find the x and y intercepts<br>

### Method
The key idea was to use the y coordinate of the y intercept as the constant in the equation of the line and solve for the x and y intercepts.

### Solution
y-intercept = (0, a)<br>
x-intercept = (b, 0)<br>
The equation of the line: $y = (-tan{theta})x + c$<br>
Substitute x = 0, y = a and rearrange to get c = a<br>
Therefore the equation fo the line is $y = (-tan{theta})x + a$<br>
Rearrange to get a = k + $tan{theta}$ and substitute to get b = 1 + $kcot{theta}$<br>

### Conclusion
Therefore:
 - Y = (0, k + $tan{theta}$)<br>
 - X = (1 + $kcot{theta}$, 0)<br>


## Problem 2
Calculate area of triangle OXY

### Method
The key idea was to take the area of the triangle and sub in the intercepts as lengths.

### Solution
Area of a triangle = 1/2(a)(b)<br>
a = k + $tan{theta}$, b = 1 + $kcot{theta}$<br>
Therefore the area of the triangle is 1/2(k + $tan{theta}$)(1 + $kcot{theta}$)<br>
This rearranges to $1/2tan{theta}(k + tan{theta})^2$

### Conclusion
A = $1/2tan{theta}(k + tan{theta})^2$


## Problem 3
${theta}$ varies, A has a minimum value, find the minimum value in terms of k.

### Method
Find the derivative of the equation of the area.

### Solution
$dA/d{theta}$ = 1/2( $-k^2cosec^2{theta} + sec^2{theta}$ )<br>
As it is a turning point, the derivative is set to 0<br>
Solve for $tan{theta}$ = k or $tan{theta}$ = -k (this can be rejected though as $0 < {theta} < 1/2pi$>)<br>
Substitute $tan{theta}$ = k into the equation of the area and solve to get 2k.<br>

### Conclusion
Therefore A = 2k.

### Reflection
I should have initially written the equation of the area into a more manageable form.


## Problem 4
Find the perimeter of OXY

### Method
Sum the intercepts and the hypotenuse they form.

### Solution
Perimeter = $1 + kcot{theta} + k + tan{theta} + sqrt{(1+kcot{theta})^2 + (k+tan{theta})^2}$<br>
Rearrange the root part of the equation to get $sqrt{(sec{theta} + kcosec{theta})^2}$<br>
And finally you get $1 + kcot{theta} + k + tan{theta} + sec{theta} + kcosec{theta}$<br>

### Conclusion
Therefore the final answer is L = $1 + tan{theta} + sec{theta} + k(1 + cot{theta} + cosec{theta})$


## Problem 5
Show the minimum value of L where ${theta}$ = a

### Method
Differentiate and solve

### Solution
$dL/d{theta}$ = $sec^2{theta} + sec{theta}tan{theta} + k(-cosec^2{theta} - cosec{theta}cot{theta})$<br>
Rearrange for k = $(sec^2{theta} + sec{theta}tan{theta})/(cosec^2{theta} + cosec{theta}cot{theta})$<br>
Further rearranging reduces to $(1-cos{theta})/(1-sin{theta})$<br>

### Conclusion
Therefore the minimum value of L occurs when k = $(1-cos{theta})/(1-sin{theta})$

### Reflection
Re-writing in many different forms helps a lot e.g. $cos^2{theta}$ = $(1+sin{theta})(1-sin{theta}).<br>
Tip: c = $cos{theta}$, s = $sin{theta}$.<br>


## Problem 6
Find an expression for the minimum value of L.

### Method
Substitution of the equation for k found in part 5.

### Solution
Start with Lmin = $1 + tan{theta} + sec{theta} + ({1-cos{theta}}/{1-sin{theta}})(1 + cot{theta} + cosec{theta})$<br>
This rearranges to ${2}/{1-sin{a}}$

### Conclusion
Lmin = ${2}/{1-sin{a}}$