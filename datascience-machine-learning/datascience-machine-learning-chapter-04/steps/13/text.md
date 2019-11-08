
Not all relationships are linear, but the linear regression is just one example of a whole class of regressions that we can do. If you remember the linear regression line that we ended up with was of the form y = mx + b, where we got back the values m and b from our linear regression analysis from ordinary least squares, or whatever method you choose. Now this is just a first order or a first-degree polynomial. The order or the degree is the power of x that you see. So that's the first-order polynomial.

Now if we wanted, we could also use a second-order polynomial, which would look like y = ax^2 + bx + c. If we were doing a regression using a second-order polynomial, we would get back values for a, b, and c. Or we could do a third-order polynomial that has the form ax^3 + bx^2 + cx + d. The higher the orders get, the more complex the curves you can represent. So, the more powers of x you have blended together, the more complicated shapes and relationships you can get.

But more degrees aren't always better. Usually there's some natural relationship in your data that isn't really all that complicated, and if you find yourself throwing very large degrees at fitting your data, you might be overfitting!

**Beware of overfitting!**

- Don't use more degrees than you need
- Visualize your data first to see how complex of a curve there might really be
- Visualize the fit and check if your curve going out of its way to accommodate outliers
- A high r-squared simply means your curve fits your training data well; it may or may not be good predictor