import sympy as sy

def f_capital(x):
    return (lambda x:eval(fnt_input))(x)
def f_small(x):
    t= sy.symbols("t")
    derivat = sy.Derivative(f_capital(t),t).doit()
    return (lambda t : eval(str(derivat)))(x)

x = sy.symbols("x")
v = sy.symbols("v")

def integral(value,number_of_bidders,low_limit,high_limit):
    return sy.integrate(pow(f_capital(x)/f_capital(value),number_of_bidders-1),(x,low_limit,high_limit))

def nash_optimal_bid(v):
    return v-integral(v,n,v_o,v)

# Expected revenue for first price auction
# expected utility or payment of a bidder
def u(v):
    return f_small(v)*pow(f_capital(v),n-1)*integral(v,n,v_o,v)
# expected profit for each bidder
def expected_profit_first_price(m):
     return  sy.integrate(u(v),(v,v_o,m))

def expected_revenue_first_price(m):
     return n*sy.integrate(f_small(v)*pow(f_capital(v),n-1)*nash_optimal_bid(v),(v,v_o,m))

# Expected revenue for second price auction
def expected_revenue_second_price(m):
    return sy.integrate(n*(n-1)*(1-f_capital(v))*f_small(v)*pow(f_capital(v),n-2)*v,(v,v_o,m))

def expected_profit_second_price(m):
    return sy.integrate((1-(n-1)*(1-f_capital(v))/f_capital(v))*f_small(v)*pow(f_capital(v),n-1)*v,(v,v_o,m))


fnt_input = str(input("Enter the cost function(CDF):"))
v_o = 0
input_ = 1
n = int(input("Total number of bidders(n): "))
print("Expected profit from first price auction\n",expected_profit_first_price(input_))
print("Expected profit from second price auction\n",expected_profit_second_price(input_))
print("Expected revenue from first price auction\n",expected_revenue_first_price(input_))
print("Expected revenue from second price auction\n",expected_revenue_second_price(input_))
