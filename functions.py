from typing import *
from vars import *

def AI():
    '''Generates text, summarizes information, categorizes information, and accesses real-time information. This function is a Google Workspace with Gemini featu'''

def ARRAY_CONSTRAIN(input_range: Range | Cell[Range], num_rows: int | Cell[int], num_cols: int | Cell[int]):
    '''Constrains an array result to a specified size.'''

def BYCOL(array_OR_range: Array | Range | Cell[Array | Range], LAMBDA: Any):
    '''Groups an array by columns by application of a LAMBDA function to each column.'''

def BYROW(array_OR_range: Array | Range | Cell[Array | Range], LAMBDA: Any):
    '''Groups an array by rows by application of a LAMBDA function to each row.'''

def CHOOSECOLS(array: Array | Cell[Array], col_num1: int | Cell[int], col_num2: Optional[int | Cell[int]]):
    '''Creates a new array from the selected columns in the existing range.'''

def CHOOSEROWS(array: Array | Cell[Array], row_num1: int | Cell[int], row_num2: Optional[int | Cell[int]]):
    '''Creates a new array from the selected rows in the existing range.'''

def FLATTEN(range1: Range | Cell[Range], *, range2: Optional[Range | Cell[Range]]):
    '''Flattens all the values from one or more ranges into a single column.'''

def FREQUENCY(data: Any, classes: Any):
    '''Calculates the frequency distribution of a one-column array into specified classes.'''

def GROWTH(known_data_y: Range | Cell[Range], known_data_x: Optional[Range | Cell[Range]], new_data_x: Optional[Range | Cell[Range]], b: Optional[Any]):
    '''Given partial data about an exponential growth trend, fits an ideal exponential growth trend and/or predicts further values.'''

def HSTACK(range1: Range | Cell[Range], *, range2: Optional[Range | Cell[Range]]):
    '''Appends ranges horizontally and in sequence to return a larger array.'''

def LINEST(known_data_y: Range | Cell[Range], known_data_x: Optional[Range | Cell[Range]], calculate_b: Optional[Any], verbose: Optional[Any]):
    '''Given partial data about a linear trend, calculates various parameters about the ideal linear trend using the least-squares method.'''

def LOGEST(known_data_y: Range | Cell[Range], known_data_x: Optional[Range | Cell[Range]], b: Optional[Any], verbose: Optional[Any]):
    '''Given partial data about an exponential growth curve, calculates various parameters about the best fit ideal exponential growth curve.'''

def MAKEARRAY(rows: int | Cell[int], columns: Any, LAMBDA: Any):
    '''Returns an array of specified dimensions with values calculated by application of a LAMBDA function.'''

def MAP(array1: Array | Cell[Array], *, array2: Optional[Array | Cell[Array]], LAMBDA: Optional[Any]):
    '''Maps each value in the given arrays to a new value by application of a LAMBDA function to each value.'''

def MDETERM(square_matrix: Any):
    '''Returns the matrix determinant of a square matrix specified as an array or range.'''

def MINVERSE(square_matrix: Any):
    '''Returns the multiplicative inverse of a square matrix specified as an array or range.'''

def MMULT(matrix1: Any, matrix2: Any):
    '''Calculates the matrix product of two matrices specified as arrays or ranges.'''

def REDUCE(initial_value: Any, array_OR_range: Array | Range | Cell[Array | Range], LAMBDA: Any):
    '''Reduces an array to an accumulated result by application of a LAMBDA function to each value.'''

def SCAN(initial_value: Any, array_OR_range: Array | Range | Cell[Array | Range], LAMBDA: Any):
    '''Scans an array and produces intermediate values by application of a LAMBDA function to each value. Returns an array of the intermediate values obtained at each step.'''

def SUMPRODUCT(array1: Array | Cell[Array], *, array2: Optional[Array | Cell[Array]]):
    '''Calculates the sum of the products of corresponding entries in two equal-sized arrays or ranges.'''

def SUMX2MY2(array_x: Array | Cell[Array], array_y: Array | Cell[Array]):
    '''Calculates the sum of the differences of the squares of values in two arrays.'''

def SUMX2PY2(array_x: Array | Cell[Array], array_y: Array | Cell[Array]):
    '''Calculates the sum of the sums of the squares of values in two arrays.'''

def SUMXMY2(array_x: Array | Cell[Array], array_y: Array | Cell[Array]):
    '''Calculates the sum of the squares of differences of values in two arrays.'''

def TOCOL(array_OR_range: Array | Range | Cell[Array | Range], ignore: Optional[Any], scan_by_column: Optional[Any]):
    '''Transforms an array or range of cells into a single column.'''

def TOROW(array_OR_range: Array | Range | Cell[Array | Range], ignore: Optional[Any], scan_by_column: Optional[Any]):
    '''Transforms an array or range of cells into a single row.'''

def TRANSPOSE(array_OR_range: Array | Range | Cell[Array | Range]):
    '''Transposes the rows and columns of an array or range of cells.'''

def TREND(known_data_y: Range | Cell[Range], known_data_x: Optional[Range | Cell[Range]], new_data_x: Optional[Range | Cell[Range]], b: Optional[Any]):
    '''Given partial data about a linear trend, fits an ideal linear trend using the least squares method and/or predicts further values.'''

def VSTACK(range1: Range | Cell[Range], *, range2: Optional[Range | Cell[Range]]):
    '''Appends ranges vertically and in sequence to return a larger array.'''

def WRAPCOLS(range: Range | Cell[Range], wrap_count: int | Cell[int], pad_with: Optional[Any]):
    '''Wraps the provided row or column of cells by columns after a specified number of elements to form a new array.'''

def WRAPROWS(range: Range | Cell[Range], wrap_count: int | Cell[int], pad_with: Optional[Any]):
    '''Wraps the provided row or column of cells by rows after a specified number of elements to form a new array.'''

def DAVERAGE(database: Any, field: Any, criteria: Any):
    '''Returns the average of a set of values selected from a database table-like array or range using a SQL-like query.'''

def DCOUNT(database: Any, field: Any, criteria: Any):
    '''Counts numeric values selected from a database table-like array or range using a SQL-like query.'''

def DCOUNTA(database: Any, field: Any, criteria: Any):
    '''Counts values, including text, selected from a database table-like array or range using a SQL-like query.'''

def DGET(database: Any, field: Any, criteria: Any):
    '''Returns a single value from a database table-like array or range using a SQL-like query.'''

def DMAX(database: Any, field: Any, criteria: Any):
    '''Returns the maximum value selected from a database table-like array or range using a SQL-like query.'''

def DMIN(database: Any, field: Any, criteria: Any):
    '''Returns the minimum value selected from a database table-like array or range using a SQL-like query.'''

def DPRODUCT(database: Any, field: Any, criteria: Any):
    '''Returns the product of values selected from a database table-like array or range using a SQL-like query.'''

def DSTDEV(database: Any, field: Any, criteria: Any):
    '''Returns the standard deviation of a population sample selected from a database table-like array or range using a SQL-like query.'''

def DSTDEVP(database: Any, field: Any, criteria: Any):
    '''Returns the standard deviation of an entire population selected from a database table-like array or range using a SQL-like query.'''

def DSUM(database: Any, field: Any, criteria: Any):
    '''Returns the sum of values selected from a database table-like array or range using a SQL-like query.'''

def DVAR(database: Any, field: Any, criteria: Any):
    '''Returns the variance of a population sample selected from a database table-like array or range using a SQL-like query.'''

def DVARP(database: Any, field: Any, criteria: Any):
    '''Returns the variance of an entire population selected from a database table-like array or range using a SQL-like query.'''

def DATE(year: int | Cell[int], month: int | Cell[int], day: int | Cell[int]) -> Date:
    '''Converts a provided year, month, and day into a date.'''

def DATEDIF(start_date: Date | Cell[Date], end_date: Date | Cell[Date], unit: DateUnit | Cell[DateUnit]) -> int:
    '''Calculates the number of days, months, or years between two dates.'''

def DATEVALUE(date_string: Date | Cell[Date]) -> Date:
    '''Converts a provided date string in a known format to a date value.'''

def DAY(date: Date | Cell[Date]):
    '''Returns the day of the month that a specific date falls on, in numeric format.'''

def DAYS(end_date: Date | Cell[Date], start_date: Date | Cell[Date]) -> float:
    '''Returns the number of days between two dates.'''

def DAYS360(start_date: Date | Cell[Date], end_date: Date | Cell[Date], method: Optional[Any]):
    '''Returns the difference between two days based on the 360 day year used in some financial interest calculations.'''

def EDATE(start_date: Date | Cell[Date], months: int | Cell[int]) -> Date:
    '''Returns a date a specified number of months before or after another date.'''

def EOMONTH(start_date: Date | Cell[Date], months: int | Cell[int]) -> Date:
    '''Returns a date representing the last day of a month which falls a specified number of months before or after another date.'''

def EPOCHTODATE(timestamp: Any, unit: Optional[DateUnit | Cell[DateUnit]]) -> Date:
    '''Converts a Unix epoch timestamp in seconds, milliseconds, or microseconds to a datetime in UTC.'''

def HOUR(time: Time | Cell[Time]):
    '''Returns the hour component of a specific time, in numeric format.'''

def ISOWEEKNUM(date: Date | Cell[Date]) -> float:
    '''Returns the number of the ISO week of the year where the provided date falls.'''

def MINUTE(time: Time | Cell[Time]):
    '''Returns the minute component of a specific time, in numeric format.'''

def MONTH(date: Date | Cell[Date]):
    '''Returns the month of the year a specific date falls in, in numeric format.'''

def NETWORKDAYS(start_date: Date | Cell[Date], end_date: Date | Cell[Date], holidays: Optional[Any]) -> float:
    '''Returns the number of net working days between two provided days.'''

def NETWORKDAYS_INTL(start_date: Date | Cell[Date], end_date: Date | Cell[Date], weekend: Optional[Any], holidays: Optional[Any]):
    '''Returns the number of net working days between two provided days excluding specified weekend days and holidays.'''

def NOW() -> Date:
    '''Returns the current date and time as a date value.'''

def SECOND(time: Time | Cell[Time]):
    '''Returns the second component of a specific time, in numeric format.'''

def TIME(hour: Any, minute: Any, second: Any) -> Date:
    '''Converts a provided hour, minute, and second into a time.'''

def TIMEVALUE(time_string: Any):
    '''Returns the fraction of a 24-hour day the time represents.'''

def TODAY() -> Date:
    '''Returns the current date as a date value.'''

def WEEKDAY(date: Date | Cell[Date], type: Optional[Any]) -> float:
    '''Returns a number representing the day of the week of the date provided.'''

def WEEKNUM(date: Date | Cell[Date], type: Optional[Any]) -> float:
    '''Returns a number representing the week of the year where the provided date falls.'''

def WORKDAY(start_date: Date | Cell[Date], num_days: int | Cell[int], holidays: Optional[Any]):
    '''Calculates the end date after a specified number of working days.'''

def WORKDAY_INTL(start_date: Date | Cell[Date], num_days: int | Cell[int], weekend: Optional[Any], holidays: Optional[Any]):
    '''Calculates the date after a specified number of workdays excluding specified weekend days and holidays.'''

def YEAR(date: Date | Cell[Date]):
    '''Returns the year specified by a given date.'''

def YEARFRAC(start_date: Date | Cell[Date], end_date: Date | Cell[Date], day_count_convention: Optional[int | Cell[int]]) -> float:
    '''Returns the number of years, including fractional years, between two dates using a specified day count convention.'''

def BIN2DEC(signed_binary_number: int | Cell[int]):
    '''Converts a signed binary number to decimal format.'''

def BIN2HEX(signed_binary_number: int | Cell[int], significant_digits: Optional[int | Cell[int]]):
    '''Converts a signed binary number to signed hexadecimal format.'''

def BIN2OCT(signed_binary_number: int | Cell[int], significant_digits: Optional[int | Cell[int]]):
    '''Converts a signed binary number to signed octal format.'''

def BITAND(value1: float | Cell[float], value2: float | Cell[float]):
    '''Bitwise boolean AND of two numbers.'''

def BITLSHIFT(value: Any, shift_amount: int | Cell[int]):
    '''Shifts the bits of the input a certain number of places to the left.'''

def BITOR(value1: float | Cell[float], value2: float | Cell[float]):
    '''Bitwise boolean OR of 2 numbers.'''

def BITRSHIFT(value: Any, shift_amount: int | Cell[int]):
    '''Shifts the bits of the input a certain number of places to the right.'''

def BITXOR(value1: float | Cell[float], value2: float | Cell[float]):
    '''Bitwise XOR (exclusive OR) of 2 numbers.'''

def COMPLEX(real_part: Any, imaginary_part: float | Cell[float], suffix: Optional[Any]) -> ComplexNumber:
    '''Creates a complex number given real and imaginary coefficients.'''

def DEC2BIN(decimal_number: int | Cell[int], significant_digits: Optional[int | Cell[int]]):
    '''Converts a decimal number to signed binary format.'''

def DEC2HEX(decimal_number: int | Cell[int], significant_digits: Optional[int | Cell[int]]):
    '''Converts a decimal number to signed hexadecimal format.'''

def DEC2OCT(decimal_number: int | Cell[int], significant_digits: Optional[int | Cell[int]]):
    '''Converts a decimal number to signed octal format.'''

def DELTA(number1: int | Cell[int], number2: Optional[int | Cell[int]]):
    '''Compare two numeric values, returning 1 if they're equal.'''

def ERF(lower_bound: Any, upper_bound: Optional[Any]):
    '''The ERF function returns the integral of the Gauss error function over an interval of values.'''

def ERF_PRECISE(lower_bound: Any, upper_bound: Optional[Any]):
    '''See ERF'''

def GESTEP(value: Any, step: Optional[Any]):
    '''Returns 1 if the rate is strictly greater than or equal to the provided step value or 0 otherwise. If no step value is provided then the default value of 0 will be used.'''

def HEX2BIN(signed_hexadecimal_number: int | Cell[int], significant_digits: Optional[int | Cell[int]]):
    '''Converts a signed hexadecimal number to signed binary format.'''

def HEX2DEC(signed_hexadecimal_number: int | Cell[int]):
    '''Converts a signed hexadecimal number to decimal format.'''

def HEX2OCT(signed_hexadecimal_number: int | Cell[int], significant_digits: int | Cell[int]):
    '''Converts a signed hexadecimal number to signed octal format.'''

def IMABS(number: int | Cell[int]) -> float:
    '''Returns absolute value of a complex number.'''

def IMAGINARY(complex_number: ComplexNumber | Cell[ComplexNumber]) -> float:
    '''Returns the imaginary coefficient of a complex number.'''

def IMCONJUGATE(number: int | Cell[int]) -> float:
    '''Returns the complex conjugate of a number.'''

def IMCOS(number: int | Cell[int]):
    '''The IMCOS function returns the cosine of the given complex number.'''

def IMCOSH(number: int | Cell[int]) -> float:
    '''Returns the hyperbolic cosine of the given complex number. For example, a given complex number "x+yi" returns "cosh(x+yi)."'''

def IMCOT(number: int | Cell[int]) -> float:
    '''Returns the cotangent of the given complex number. For example, a given complex number "x+yi" returns "cot(x+yi)."'''

def IMCOTH(number: int | Cell[int]) -> float:
    '''Returns the hyperbolic cotangent of the given complex number. For example, a given complex number "x+yi" returns "coth(x+yi)."'''

def IMCSC(number: int | Cell[int]) -> float:
    '''Returns the cosecant of the given complex number.'''

def IMCSCH(number: int | Cell[int]) -> float:
    '''Returns the hyperbolic cosecant of the given complex number. For example, a given complex number "x+yi" returns "csch(x+yi)."'''

def IMDIV(dividend: Any, divisor: Any) -> float:
    '''Returns one complex number divided by another.'''

def IMEXP(exponent: Any) -> float:
    '''Returns Euler's number, e (~2.718) raised to a complex power.'''

def IMLOG(value: Any, base: Any) -> float:
    '''Returns the logarithm of a complex number for a specified base.'''

def IMLOG10(value: Any) -> float:
    '''Returns the logarithm of a complex number with base 10.'''

def IMLOG2(value: Any) -> float:
    '''Returns the logarithm of a complex number with base 2.'''

def IMPRODUCT(factor1: Any, *, factor2: Optional[Any]) -> float:
    '''Returns the result of multiplying a series of complex numbers together.'''

def IMREAL(complex_number: ComplexNumber | Cell[ComplexNumber]) -> float:
    '''Returns the real coefficient of a complex number.'''

def IMSEC(number: int | Cell[int]) -> float:
    '''Returns the secant of the given complex number. For example, a given complex number "x+yi" returns "sec(x+yi)."'''

def IMSECH(number: int | Cell[int]) -> float:
    '''Returns the hyperbolic secant of the given complex number. For example, a given complex number "x+yi" returns "sech(x+yi)."'''

def IMSIN(number: int | Cell[int]) -> float:
    '''Returns the sine of the given complex number.'''

def IMSINH(number: int | Cell[int]) -> float:
    '''Returns the hyperbolic sine of the given complex number. For example, a given complex number "x+yi" returns "sinh(x+yi)."'''

def IMSUB(first_number: int | Cell[int], second_number: int | Cell[int]) -> float:
    '''Returns the difference between two complex numbers.'''

def IMSUM(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]) -> float:
    '''Returns the sum of a series of complex numbers.'''

def IMTAN(number: int | Cell[int]) -> float:
    '''Returns the tangent of the given complex number.'''

def IMTANH(number: int | Cell[int]) -> float:
    '''Returns the hyperbolic tangent of the given complex number. For example, a given complex number "x+yi" returns "tanh(x+yi)."'''

def OCT2BIN(signed_octal_number: int | Cell[int], significant_digits: Optional[int | Cell[int]]):
    '''Converts a signed octal number to signed binary format.'''

def OCT2DEC(signed_octal_number: int | Cell[int]):
    '''Converts a signed octal number to decimal format.'''

def OCT2HEX(signed_octal_number: int | Cell[int], significant_digits: Optional[int | Cell[int]]):
    '''Converts a signed octal number to signed hexadecimal format.'''

def FILTER(range: Range | Cell[Range], condition1: Any, condition2: Optional[Any]):
    '''Returns a filtered version of the source range, returning only rows or columns which meet the specified conditions.'''

def SORT(range: Range | Cell[Range], sort_column: Any, is_ascending: Any, sort_column2: Optional[Any], is_ascending2: Optional[Any]):
    '''Sorts the rows of a given array or range by the values in one or more columns.'''

def SORTN(range: Range | Cell[Range], n: Optional[int | Cell[int]], display_ties_mode: Optional[Any], sort_column1: Optional[Any], *, is_ascending1: Optional[Any]):
    '''Returns the first n items in a data set after performing a sort.'''

def UNIQUE(range: Range | Cell[Range]):
    '''Returns unique rows in the provided source range, discarding duplicates. Rows are returned in the order in which they first appear in the source range.'''

def ACCRINT(issue: Any, first_payment: Any, settlement: Any, rate: Any, redemption: Any, frequency: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the accrued interest of a security that has periodic payments.'''

def ACCRINTM(issue: Any, maturity: Any, rate: Any, redemption: Optional[Any], day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the accrued interest of a security that pays interest at maturity.'''

def AMORLINC(cost: Any, purchase_date: Date | Cell[Date], first_period_end: Any, salvage: Any, period: Any, rate: Any, basis: Optional[Any]):
    '''Returns the depreciation for an accounting period, or the prorated depreciation if the asset was purchased in the middle of a period.'''

def COUPDAYBS(settlement: Any, maturity: Any, frequency: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the number of days from the first coupon, or interest payment, until settlement.'''

def COUPDAYS(settlement: Any, maturity: Any, frequency: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the number of days in the coupon, or interest payment, period that contains the specified settlement date.'''

def COUPDAYSNC(settlement: Any, maturity: Any, frequency: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the number of days from the settlement date until the next coupon, or interest payment.'''

def COUPNCD(settlement: Any, maturity: Any, frequency: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates next coupon, or interest payment, date after the settlement date.'''

def COUPNUM(settlement: Any, maturity: Any, frequency: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the number of coupons, or interest payments, between the settlement date and the maturity date of the investment.'''

def COUPPCD(settlement: Any, maturity: Any, frequency: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates last coupon, or interest payment, date before the settlement date.'''

def CUMIPMT(rate: Any, number_of_periods: int | Cell[int], present_value: Any, first_period: Any, last_period: Any, end_OR_beginning: Any):
    '''Calculates the cumulative interest over a range of payment periods for an investment based on constant-amount periodic payments and a constant interest rate.'''

def CUMPRINC(rate: Any, number_of_periods: int | Cell[int], present_value: Any, first_period: Any, last_period: Any, end_OR_beginning: Any):
    '''Calculates the cumulative principal paid over a range of payment periods for an investment based on constant-amount periodic payments and a constant interest rate.'''

def DB(cost: Any, salvage: Any, life: Any, period: Any, month: Optional[int | Cell[int]]):
    '''Calculates the depreciation of an asset for a specified period using the arithmetic declining balance method.'''

def DDB(cost: Any, salvage: Any, life: Any, period: Any, factor: Optional[Any]):
    '''Calculates the depreciation of an asset for a specified period using the double-declining balance method.'''

def DISC(settlement: Any, maturity: Any, price: Any, redemption: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the discount rate of a security based on price.'''

def DOLLARDE(fractional_price: Any, unit: Any):
    '''Converts a price quotation given as a decimal fraction into a decimal value.'''

def DOLLARFR(decimal_price: Any, unit: Any):
    '''Converts a price quotation given as a decimal value into a decimal fraction.'''

def DURATION(settlement: Any, maturity: Any, rate: Any, yield_value: Any, frequency: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the number of compounding periods required for an investment of a specified present value appreciating at a given rate to reach a target value.'''

def EFFECT(nominal_rate: Any, periods_per_year: Any):
    '''Calculates the annual effective interest rate given the nominal rate and number of compounding periods per year.'''

def FV(rate: Any, number_of_periods: int | Cell[int], payment_amount: Any, present_value: Optional[Any], end_OR_beginning: Optional[Any]):
    '''Calculates the future value of an annuity investment based on constant-amount periodic payments and a constant interest rate.'''

def FVSCHEDULE(principal: Any, rate_schedule: Any):
    '''Calculates the future value of some principal based on a specified series of potentially varying interest rates.'''

def INTRATE(buy_date: Date | Cell[Date], sell_date: Date | Cell[Date], buy_price: Any, sell_price: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the effective interest rate generated when an investment is purchased at one price and sold at another with no interest or dividends generated by the investment itself.'''

def IPMT(rate: Any, period: Any, number_of_periods: int | Cell[int], present_value: Any, future_value: Optional[Any], end_OR_beginning: Optional[Any]):
    '''Calculates the payment on interest for an investment based on constant-amount periodic payments and a constant interest rate.'''

def IRR(cashflow_amounts: Any, rate_guess: Optional[Any]):
    '''Calculates the internal rate of return on an investment based on a series of periodic cash flows.'''

def ISPMT(rate: Any, period: Any, number_of_periods: int | Cell[int], present_value: Any):
    '''The ISPMT function calculates the interest paid during a particular period of an investment.'''

def MDURATION(settlement: Any, maturity: Any, rate: Any, yield_value: Any, frequency: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the modified Macaulay duration of a security paying periodic interest, such as a US Treasury Bond, based on expected yield.'''

def MIRR(cashflow_amounts: Any, financing_rate: Any, reinvestment_return_rate: Any):
    '''Calculates the modified internal rate of return on an investment based on a series of periodic cash flows and the difference between the interest rate paid on financing versus the return received on reinvested income.'''

def NOMINAL(effective_rate: Any, periods_per_year: Any):
    '''Calculates the annual nominal interest rate given the effective rate and number of compounding periods per year.'''

def NPER(rate: Any, payment_amount: Any, present_value: Any, future_value: Optional[Any], end_OR_beginning: Optional[Any]):
    '''Calculates the number of payment periods for an investment based on constant-amount periodic payments and a constant interest rate.'''

def NPV(discount: int | Cell[int], cashflow1: Any, *, cashflow2: Optional[Any]):
    '''Calculates the net present value of an investment based on a series of periodic cash flows and a discount rate.'''

def PDURATION(rate: Any, present_value: Any, future_value: Any) -> float:
    '''Returns the number of periods for an investment to reach a specific value at a given rate.'''

def PMT(rate: Any, number_of_periods: int | Cell[int], present_value: Any, future_value: Optional[Any], end_OR_beginning: Optional[Any]):
    '''Calculates the periodic payment for an annuity investment based on constant-amount periodic payments and a constant interest rate.'''

def PPMT(rate: Any, period: Any, number_of_periods: int | Cell[int], present_value: Any, future_value: Optional[Any], end_OR_beginning: Optional[Any]):
    '''Calculates the payment on the principal of an investment based on constant-amount periodic payments and a constant interest rate.'''

def PRICE(settlement: Any, maturity: Any, rate: Any, yield_value: Any, redemption: Any, frequency: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the price of a security paying periodic interest, such as a US Treasury Bond, based on expected yield.'''

def PRICEDISC(settlement: Any, maturity: Any, discount: int | Cell[int], redemption: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the price of a discount (non-interest-bearing) security, based on expected yield.'''

def PRICEMAT(settlement: Any, maturity: Any, issue: Any, rate: Any, yield_value: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the price of a security paying interest at maturity, based on expected yield.'''

def PV(rate: Any, number_of_periods: int | Cell[int], payment_amount: Any, future_value: Optional[Any], end_OR_beginning: Optional[Any]):
    '''Calculates the present value of an annuity investment based on constant-amount periodic payments and a constant interest rate.'''

def RATE(number_of_periods: int | Cell[int], payment_per_period: Any, present_value: Any, future_value: Optional[Any], end_OR_beginning: Optional[Any], rate_guess: Optional[Any]):
    '''Calculates the interest rate of an annuity investment based on constant-amount periodic payments and the assumption of a constant interest rate.'''

def RECEIVED(settlement: Any, maturity: Any, investment: Any, discount: int | Cell[int], day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the amount received at maturity for an investment in fixed-income securities purchased on a given date.'''

def RRI(number_of_periods: int | Cell[int], present_value: Any, future_value: Any) -> float:
    '''Returns the interest rate needed for an investment to reach a specific value within a given number of periods.'''

def SLN(cost: Any, salvage: Any, life: Any):
    '''Calculates the depreciation of an asset for one period using the straight-line method.'''

def SYD(cost: Any, salvage: Any, life: Any, period: Any):
    '''Calculates the depreciation of an asset for a specified period using the sum of years digits method.'''

def TBILLEQ(settlement: Any, maturity: Any, discount: int | Cell[int]):
    '''Calculates the equivalent annualized rate of return of a US Treasury Bill based on discount rate.'''

def TBILLPRICE(settlement: Any, maturity: Any, discount: int | Cell[int]):
    '''Calculates the price of a US Treasury Bill based on discount rate.'''

def TBILLYIELD(settlement: Any, maturity: Any, price: Any):
    '''Calculates the yield of a US Treasury Bill based on price.'''

def VDB(cost: Any, salvage: Any, life: Any, start_period: Any, end_period: Any, factor: Optional[Any], no_switch: Optional[Any]):
    '''Returns the depreciation of an asset for a particular period (or partial period).'''

def XIRR(cashflow_amounts: Any, cashflow_dates: Date | Cell[Date], rate_guess: Optional[Any]):
    '''Calculates the internal rate of return of an investment based on a specified series of potentially irregularly spaced cash flows.'''

def XNPV(discount: int | Cell[int], cashflow_amounts: Any, cashflow_dates: Date | Cell[Date]):
    '''Calculates the net present value of an investment based on a specified series of potentially irregularly spaced cash flows and a discount rate.'''

def YIELD(settlement: Any, maturity: Any, rate: Any, price: Any, redemption: Any, frequency: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the annual yield of a security paying periodic interest, such as a US Treasury Bond, based on price.'''

def YIELDDISC(settlement: Any, maturity: Any, price: Any, redemption: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the annual yield of a discount (non-interest-bearing) security, based on price.'''

def YIELDMAT(settlement: Any, maturity: Any, issue: Any, rate: Any, price: Any, day_count_convention: Optional[int | Cell[int]]):
    '''Calculates the annual yield of a security paying interest at maturity, based on price.'''

def ARRAYFORMULA(array_formula: Array | Cell[Array]):
    '''Enables the display of values returned from an array formula into multiple rows and/or columns and the use of non-array functions with arrays.'''

def DETECTLANGUAGE(text_OR_range: str | Range | Cell[str | Range]):
    '''Identifies the language used in text within the specified range.'''

def GOOGLEFINANCE(ticker: Any, attribute: Optional[Any], start_date: Optional[Date | Cell[Date]], end_date_OR_num_days: Optional[int | Date | Cell[int | Date]], interval: Optional[Any]):
    '''Fetches current or historical securities information from Google Finance.'''

def GOOGLETRANSLATE(text: str | Cell[str], source_language: Optional[LanguageCodes | Cell[LanguageCodes]], target_language: Optional[LanguageCodes | Cell[LanguageCodes]]):
    '''Translates text from one language into anoth'''

def IMAGE(url: URL | Cell[URL], mode: Optional[Any], height: Optional[Any], width: Optional[Any]):
    '''Inserts an image into a cell.'''

def QUERY(data: Any, query: Any, headers: Optional[Any]):
    '''Runs a Google Visualization API Query Language query across data.'''

def SPARKLINE(data: Any, options: Optional[Any]):
    '''Creates a miniature chart contained within a single cell.'''

def ERROR_TYPE(reference: Any) -> float:
    '''Returns a number corresponding to the error value in a different cell.'''

def ISBLANK(value: Any) -> bool:
    '''Checks whether the referenced cell is empty.'''

def ISDATE(value: Any) -> bool:
    '''Returns whether a value is a date.'''

def ISEMAIL(value: Any) -> bool:
    '''Checks whether a value is a valid email address.'''

def ISERR(value: Any) -> bool:
    '''Checks whether a value is an error other than `#N/A`.'''

def ISERROR(value: Any) -> bool:
    '''Checks whether a value is an error.'''

def ISFORMULA(cell: Any) -> bool:
    '''Checks whether a formula is in the referenced cell.'''

def ISLOGICAL(value: Any) -> bool:
    '''Checks whether a value is `TRUE` or `FALSE`.'''

def ISNA(value: Any) -> bool:
    '''Checks whether a value is the error `#N/A`.'''

def ISNONTEXT(value: Any) -> bool:
    '''Checks whether a value is non-textual.'''

def ISNUMBER(value: Any) -> bool:
    '''Checks whether a value is a number.'''

def ISREF(value: Any) -> bool:
    '''Checks whether a value is a valid cell reference.'''

def ISTEXT(value: Any) -> bool:
    '''Checks whether a value is text.'''

def N(value: Any) -> float:
    '''Returns the argument provided as a number.'''

def NA():
    '''Returns the "value not available" error, `#N/A`.'''

def SHEETS(reference: Any) -> float:
    '''Returns the total number of sheets in the referenced spreadsheet. Learn more about the SHEETS functi'''

def TYPE(value: Any) -> float:
    '''Returns a number associated with the type of data passed into the function.'''

def CELLINFO(info_type: Any, reference: Any):
    '''Returns the requested information about the specified cell.'''

def AND(logical_expression1: Any, *, logical_expression2: Optional[Any]) -> bool:
    '''Returns true if all of the provided arguments are logically true, and false if any of the provided arguments are logically false.'''

def FALSE():
    '''Returns the logical value `FALSE`.'''

def IF(logical_expression: Any, value_if_true: Any, value_if_false: Any) -> bool:
    '''Returns one value if a logical expression is `TRUE` and another if it is `FALSE`.'''

def IFERROR(value: Any, value_if_error: Optional[Any]):
    '''Returns the first argument if it is not an error value, otherwise returns the second argument if present, or a blank if the second argument is absent.'''

def IFNA(value: Any, value_if_na: Any):
    '''Evaluates a value. If the value is an #N/A error, returns the specified value.'''

def IFS(condition1: Any, value1: float | Cell[float], condition2: Optional[Any], *, value2: Optional[float | Cell[float]]):
    '''Evaluates multiple conditions and returns a value that corresponds to the first true condition.'''

def LAMBDA(name: Any, formula_expression: Any):
    '''Creates and returns a custom function with a set of names and a formula_expression that uses them. To calculate the formula_expression, you can call the returned function with as many values as the name declares.'''

def LET(name1: Any, value_expression1: Any, *, name2: Optional[Any], value_expression2: Optional[Any], formula_expression: Optional[Any]):
    '''Assigns name with the value_expression results and returns the result of the formula_expression. The formula_expression can use the names defined in the scope of the LET function. The value_expressions are evaluated only once in the LET function even if the following value_expressions or the formula_expression use them multiple times.'''

def NOT(logical_expression: Any) -> bool:
    '''Returns the opposite of a logical value - `NOT(TRUE)` returns `FALSE`; `NOT(FALSE)` returns `TRUE`.'''

def OR(logical_expression1: Any, *, logical_expression2: Optional[Any]) -> bool:
    '''Returns true if any of the provided arguments are logically true, and false if all of the provided arguments are logically false.'''

def SWITCH(expression: Any, case1: Any, value1: float | Cell[float], defaultorcase2: Optional[Any], *, value2: Optional[float | Cell[float]]):
    '''Tests an expression against a list of cases and returns the corresponding value of the first matching case, with an optional default value if nothing else is met.'''

def TRUE():
    '''Returns the logical value `TRUE`.'''

def XOR(logical_expression1: Any, *, logical_expression2: Optional[Any]):
    '''The XOR function performs an exclusive or of 2 numbers that returns a 1 if the numbers are different, and a 0 otherwise.'''

def ADDRESS(row: Any, column: int | Cell[int], absolute_relative_mode: Optional[Any], use_a1_notation: Optional[Any], sheet: Optional[Any]):
    '''Returns a cell reference as a string.'''

def CHOOSE(index: Any, choice1: Any, *, choice2: Optional[Any]):
    '''Returns an element from a list of choices based on index.'''

def COLUMN(cell_reference: Optional[Any]) -> float:
    '''Returns the column number of a specified cell, with `A=1`.'''

def COLUMNS(range: Range | Cell[Range]) -> float:
    '''Returns the number of columns in a specified array or range.'''

def FORMULATEXT(cell: Any):
    '''Returns the formula as a string.'''

def GETPIVOTDATA(value_name: Any, any_pivot_table_cell: Any, *, original_column: Optional[Any], pivot_item: Optional[Any]):
    '''Extracts an aggregated value from a pivot table that corresponds to the specified row and column headings.'''

def HLOOKUP(search_key: Any, range: Range | Cell[Range], index: Any, is_sorted: Optional[Any]):
    '''Horizontal lookup. Searches across the first row of a range for a key and returns the value of a specified cell in the column found.'''

def INDEX(reference: Any, row: Optional[Any], column: Optional[int | Cell[int]]):
    '''Returns the content of a cell, specified by row and column offset.'''

def INDIRECT(cell_reference_as_string: Any, is_A1_notation: Optional[Any]):
    '''Returns a cell reference specified by a string.'''

def LOOKUP(search_key: Any, search_range_OR_search_result_array: Array | Range | Cell[Array | Range], result_range: Optional[Range | Cell[Range]]):
    '''Looks through a row or column for a key and returns the value of the cell in a result range located in the same position as the search row or column.'''

def MATCH(search_key: Any, range: Range | Cell[Range], search_type: Optional[Any]):
    '''Returns the relative position of an item in a range that matches a specified value.'''

def OFFSET(cell_reference: Any, offset_rows: Any, offset_columns: Any, height: Optional[Any], width: Optional[Any]) -> float:
    '''Returns a range reference shifted a specified number of rows and columns from a starting cell reference.'''

def ROW(cell_reference: Optional[Any]) -> float:
    '''Returns the row number of a specified cell.'''

def ROWS(range: Range | Cell[Range]) -> float:
    '''Returns the number of rows in a specified array or range.'''

def SHEET(value: Any) -> float:
    '''Returns the sheet number of the specified sheet or other reference. Learn more about the SHEET functi'''

def VLOOKUP(search_key: Any, range: Range | Cell[Range], index: Any, is_sorted: Optional[Any]):
    '''Vertical lookup. Searches down the first column of a range for a key and returns the value of a specified cell in the row found.'''

def XLOOKUP(search_key: Any, lookup_range: Range | Cell[Range], result_range: Range | Cell[Range], missing_value: Any, match_mode: Optional[Any], search_mode: Optional[Any]):
    '''Returns the values in the result range based on the position where a match was found in the lookup range. If no match is found, it returns the closest match.'''

def ABS(value: float | Cell[float]) -> float:
    '''Returns the absolute value of a number.'''

def ACOS(value: float | Cell[float]) -> float:
    '''Returns the inverse cosine of a value, in radians.'''

def ACOSH(value: float | Cell[float]) -> float:
    '''Returns the inverse hyperbolic cosine of a number.'''

def ACOT(value: float | Cell[float]) -> float:
    '''Returns the inverse cotangent of a value, in radians.'''

def ACOTH(value: float | Cell[float]) -> float:
    '''Returns the inverse hyperbolic cotangent of a value, in radians. Must not be between -1 and 1, inclusive.'''

def ASIN(value: float | Cell[float]) -> float:
    '''Returns the inverse sine of a value, in radians.'''

def ASINH(value: float | Cell[float]) -> float:
    '''Returns the inverse hyperbolic sine of a number.'''

def ATAN(value: float | Cell[float]) -> float:
    '''Returns the inverse tangent of a value, in radians.'''

def ATAN2(x: float | Cell[float], y: float | Cell[float]) -> float:
    '''Returns the angle between the x-axis and a line segment from the origin (0,0) to specified coordinate pair (`x`,`y`), in radians.'''

def ATANH(value: float | Cell[float]) -> float:
    '''Returns the inverse hyperbolic tangent of a number.'''

def BASE(value: float | Cell[float], base: Any, min_length: Optional[int | Cell[int]]) -> float:
    '''Converts a number into a text representation in another base, for example, base 2 for binary.'''

def CEILING(value: float | Cell[float], factor: Optional[Any]) -> int:
    '''Rounds a number up to the nearest integer multiple of specified significance.'''

def CEILING_MATH(number: int | Cell[int], significance: Optional[Any], mode: Optional[Any]) -> int:
    '''Rounds a number up to the nearest integer multiple of specified significance, with negative numbers rounding toward or away from 0 depending on the mode.'''

def CEILING_PRECISE(number: int | Cell[int], significance: Optional[Any]) -> int:
    '''Rounds a number up to the nearest integer multiple of specified significance. If the number is positive or negative, it is rounded up.'''

def COMBIN(n: int | Cell[int], k: Any) -> float:
    '''Returns the number of ways to choose some number of objects from a pool of a given size of objects.'''

def COMBINA(n: int | Cell[int], k: Any) -> float:
    '''Returns the number of ways to choose some number of objects from a pool of a given size of objects, including ways that choose the same object multiple times.'''

def COS(angle: Any) -> float:
    '''Returns the cosine of an angle provided in radians.'''

def COSH(value: float | Cell[float]) -> float:
    '''Returns the hyperbolic cosine of any real number.'''

def COT(angle: Any) -> float:
    '''Cotangent of an angle provided in radians.'''

def COTH(value: float | Cell[float]) -> float:
    '''Returns the hyperbolic cotangent of any real number.'''

def COUNTBLANK(range: Range | Cell[Range]) -> float:
    '''Returns the number of empty cells in a given range.'''

def COUNTIF(range: Range | Cell[Range], criterion: Any):
    '''Returns a conditional count across a range.'''

def COUNTIFS(criteria_range1: Range | Cell[Range], criterion1: Any, criteria_range2: Optional[Range | Cell[Range]], *, criterion2: Optional[Any]):
    '''Returns the count of a range depending on multiple criteria.'''

def COUNTUNIQUE(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]):
    '''Counts the number of unique values in a list of specified values and ranges.'''

def CSC(angle: Any) -> float:
    '''Returns the cosecant of an angle provided in radians.'''

def CSCH(value: float | Cell[float]) -> float:
    '''The CSCH function returns the hyperbolic cosecant of any real number.'''

def DECIMAL(value: float | Cell[float], base: Any) -> float:
    '''The DECIMAL function converts the text representation of a number in another base, to base 10 (decimal).'''

def DEGREES(angle: Any) -> float:
    '''Converts an angle value in radians to degrees.'''

def ERFC(z: Any) -> float:
    '''Returns the complementary Gauss error function of a value.'''

def ERFC_PRECISE(z: Any) -> float:
    '''See ERFC'''

def EVEN(value: float | Cell[float]) -> int:
    '''Rounds a number up to the nearest even integer.'''

def EXP(exponent: Any) -> float:
    '''Returns Euler's number, e (~2.718) raised to a power.'''

def FACT(value: float | Cell[float]) -> float:
    '''Returns the factorial of a number.'''

def FACTDOUBLE(value: float | Cell[float]) -> float:
    '''Returns the "double factorial" of a number.'''

def FLOOR(value: float | Cell[float], factor: Optional[Any]) -> int:
    '''Rounds a number down to the nearest integer multiple of specified significance.'''

def FLOOR_MATH(number: int | Cell[int], significance: Optional[Any], mode: Optional[Any]) -> int:
    '''Rounds a number down to the nearest integer multiple of specified significance, with negative numbers rounding toward or away from 0 depending on the mode.'''

def FLOOR_PRECISE(number: int | Cell[int], significance: Optional[Any]) -> int:
    '''The FLOOR.PRECISE function rounds a number down to the nearest integer or multiple of specified significance.'''

def GAMMALN(value: float | Cell[float]) -> float:
    '''Returns the the logarithm of a specified Gamma function, base e (Euler's number).'''

def GAMMALN_PRECISE(value: float | Cell[float]) -> float:
    '''See GAMMALN'''

def GCD(value1: float | Cell[float], value2: float | Cell[float]) -> int:
    '''Returns the greatest common divisor of one or more integers.'''

def IMLN(complex_value: Any) -> float:
    '''Returns the logarithm of a complex number, base e (Euler's number).'''

def IMPOWER(complex_base: Any, exponent: Any) -> float:
    '''Returns a complex number raised to a power.'''

def IMSQRT(complex_number: ComplexNumber | Cell[ComplexNumber]) -> float:
    '''Computes the square root of a complex number.'''

def INT(value: float | Cell[float]) -> int:
    '''Rounds a number down to the nearest integer that is less than or equal to it.'''

def ISEVEN(value: float | Cell[float]) -> bool:
    '''Checks whether the provided value is even.'''

def ISO_CEILING(number: int | Cell[int], significance: Optional[Any]) -> float:
    '''See CEILING.PRECISE'''

def ISODD(value: float | Cell[float]) -> bool:
    '''Checks whether the provided value is odd.'''

def LCM(value1: float | Cell[float], value2: float | Cell[float]) -> int:
    '''Returns the least common multiple of one or more integers.'''

def LN(value: float | Cell[float]) -> float:
    '''Returns the the logarithm of a number, base e (Euler's number).'''

def LOG(value: float | Cell[float], base: Any) -> float:
    '''Returns the the logarithm of a number given a base.'''

def LOG10(value: float | Cell[float]) -> float:
    '''Returns the the logarithm of a number, base 10.'''

def MOD(dividend: Any, divisor: Any) -> float:
    '''Returns the result of the modulo operator, the remainder after a division operation.'''

def MROUND(value: float | Cell[float], factor: Any) -> int:
    '''Rounds one number to the nearest integer multiple of another.'''

def MULTINOMIAL(value1: float | Cell[float], value2: float | Cell[float]) -> float:
    '''Returns the factorial of the sum of values divided by the product of the values' factorials.'''

def MUNIT(dimension: Any) -> float:
    '''Returns a unit matrix of size dimension x dimension.'''

def ODD(value: float | Cell[float]) -> int:
    '''Rounds a number up to the nearest odd integer.'''

def PI() -> float:
    '''Returns the value of Pi to 14 decimal places.'''

def POWER(base: Any, exponent: Any) -> float:
    '''Returns a number raised to a power.'''

def PRODUCT(factor1: Any, *, factor2: Optional[Any]) -> float:
    '''Returns the result of multiplying a series of numbers together.'''

def QUOTIENT(dividend: Any, divisor: Any) -> float:
    '''Returns one number divided by another.'''

def RADIANS(angle: Any) -> float:
    '''Converts an angle value in degrees to radians.'''

def RAND() -> float:
    '''Returns a random number between 0 inclusive and 1 exclusive.'''

def RANDARRAY(rows: int | Cell[int], columns: Any):
    '''Generates an array of random numbers between 0 and 1.'''

def RANDBETWEEN(low: Any, high: Any) -> int:
    '''Returns a uniformly random integer between two values, inclusive.'''

def ROUND(value: float | Cell[float], places: Optional[Any]) -> float:
    '''Rounds a number to a certain number of decimal places according to standard rules.'''

def ROUNDDOWN(value: float | Cell[float], places: Optional[Any]) -> float:
    '''Rounds a number to a certain number of decimal places, always rounding down to the next valid increment.'''

def ROUNDUP(value: float | Cell[float], places: Optional[Any]) -> float:
    '''Rounds a number to a certain number of decimal places, always rounding up to the next valid increment.'''

def SEC(angle: Any) -> float:
    '''The SEC function returns the secant of an angle, measured in radians.'''

def SECH(value: float | Cell[float]) -> float:
    '''The SECH function returns the hyperbolic secant of an angle.'''

def SEQUENCE(rows: int | Cell[int], columns: Any, start: Any, step: Any) -> float:
    '''Returns an array of sequential numbers, such as 1, 2, 3, 4.'''

def SERIESSUM(x: float | Cell[float], n: int | Cell[int], m: Any, a: Any):
    '''Given parameters x, n, m, and a, returns the power series sum a1xn + a2x(n+m) + ... + aix(n+(i-1)m), where i is the number of entries in range `a`.'''

def SIGN(value: float | Cell[float]) -> float:
    '''Given an input number, returns `-1` if it is negative, `1` if positive, and `0` if it is zero.'''

def SIN(angle: Any) -> float:
    '''Returns the sine of an angle provided in radians.'''

def SINH(value: float | Cell[float]) -> float:
    '''Returns the hyperbolic sine of any real number.'''

def SQRT(value: float | Cell[float]) -> float:
    '''Returns the positive square root of a positive number.'''

def SQRTPI(value: float | Cell[float]) -> float:
    '''Returns the positive square root of the product of Pi and the given positive number.'''

def SUBTOTAL(function_code: Any, range1: Range | Cell[Range], *, range2: Optional[Range | Cell[Range]]):
    '''Returns a subtotal for a vertical range of cells using a specified aggregation function.'''

def SUM(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]) -> float:
    '''Returns the sum of a series of numbers and/or cells.'''

def SUMIF(range: Range | Cell[Range], criterion: Any, sum_range: Optional[Range | Cell[Range]]):
    '''Returns a conditional sum across a range.'''

def SUMIFS(sum_range: Range | Cell[Range], criteria_range1: Range | Cell[Range], criterion1: Any, criteria_range2: Optional[Range | Cell[Range]], *, criterion2: Optional[Any]):
    '''Returns the sum of a range depending on multiple criteria.'''

def SUMSQ(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]) -> float:
    '''Returns the sum of the squares of a series of numbers and/or cells.'''

def TAN(angle: Any) -> float:
    '''Returns the tangent of an angle provided in radians.'''

def TANH(value: float | Cell[float]) -> float:
    '''Returns the hyperbolic tangent of any real number.'''

def TRUNC(value: float | Cell[float], places: Optional[Any]) -> float:
    '''Truncates a number to a certain number of significant digits by omitting less significant digits.'''

def ADD(value1: float | Cell[float], value2: float | Cell[float]) -> float:
    '''Returns the sum of two numbers. Equivalent to the `+` operator.'''

def CONCAT(value1: float | Cell[float], value2: float | Cell[float]):
    '''Returns the concatenation of two values. Equivalent to the `&` operator.'''

def DIVIDE(dividend: Any, divisor: Any) -> float:
    '''Returns one number divided by another. Equivalent to the `/` operator.'''

def EQ(value1: float | Cell[float], value2: float | Cell[float]) -> bool:
    '''Returns `TRUE` if two specified values are equal and `FALSE` otherwise. Equivalent to the `=` operator.'''

def GT(value1: float | Cell[float], value2: float | Cell[float]) -> bool:
    '''Returns `TRUE` if the first argument is strictly greater than the second, and `FALSE` otherwise. Equivalent to the `>` operator.'''

def GTE(value1: float | Cell[float], value2: float | Cell[float]) -> bool:
    '''Returns `TRUE` if the first argument is greater than or equal to the second, and `FALSE` otherwise. Equivalent to the `>=` operator.'''

def ISBETWEEN(value_to_compare: Any, lower_value: Any, upper_value: Any, lower_value_is_inclusive: Any, upper_value_is_inclusive: Any) -> bool:
    '''Checks whether a provided number is between two other numbers either inclusively or exclusively.'''

def LT(value1: float | Cell[float], value2: float | Cell[float]) -> bool:
    '''Returns `TRUE` if the first argument is strictly less than the second, and `FALSE` otherwise. Equivalent to the `<` operator.'''

def LTE(value1: float | Cell[float], value2: float | Cell[float]) -> bool:
    '''Returns `TRUE` if the first argument is less than or equal to the second, and `FALSE` otherwise. Equivalent to the `<=` operator.'''

def MINUS(value1: float | Cell[float], value2: float | Cell[float]) -> float:
    '''Returns the difference of two numbers. Equivalent to the `-` operator.'''

def MULTIPLY(factor1: Any, factor2: Any) -> float:
    '''Returns the product of two numbers. Equivalent to the `*` operator.'''

def NE(value1: float | Cell[float], value2: float | Cell[float]) -> bool:
    '''Returns `TRUE` if two specified values are not equal and `FALSE` otherwise. Equivalent to the `<>` operator.'''

def POW(base: Any, exponent: Any) -> float:
    '''Returns a number raised to a power.'''

def UMINUS(value: Any) -> float:
    '''Returns a number with the sign reversed.'''

def UNARY_PERCENT(percentage: Any):
    '''Returns a value interpreted as a percentage; that is, `UNARY_PERCENT(100)` equals `1`.'''

def UNIQUE(range: Range | Cell[Range], by_column: Any, exactly_once: Any):
    '''Returns unique rows in the provided source range, discarding duplicates. Rows are returned in the order in which they first appear in the source range.'''

def UPLUS(value: Any) -> float:
    '''Returns a specified number, unchanged.'''

def CONVERT(value: Any, start_unit: Any, end_unit: Any):
    '''Converts a numeric value to a different unit of measure.'''

def TO_DATE(value: Any):
    '''Converts a provided number to a date.'''

def TO_DOLLARS(value: Any):
    '''Converts a provided number to a dollar value.'''

def TO_PERCENT(value: Any):
    '''Converts a provided number to a percentage.'''

def TO_PURE_NUMBER(value: Any):
    '''Converts a provided date/time, percentage, currency or other formatted numeric value to a pure number without formatting.'''

def TO_TEXT(value: Any):
    '''Converts a provided numeric value to a text value.'''

def AVEDEV(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]):
    '''Calculates the average of the magnitudes of deviations of data from a dataset's mean.'''

def AVERAGE(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]):
    '''Returns the numerical average value in a dataset, ignoring text.'''

def AVERAGE_WEIGHTED(values: Any, weights: Any, additionalvalues: Optional[Any], additionalweights: Optional[Any]):
    '''Finds the weighted average of a set of values, given the values and the corresponding weights.'''

def AVERAGEA(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]):
    '''Returns the numerical average value in a dataset.'''

def AVERAGEIF(criteria_range: Range | Cell[Range], criterion: Any, average_range: Optional[Range | Cell[Range]]):
    '''Returns the average of a range depending on criteria.'''

def AVERAGEIFS(average_range: Range | Cell[Range], criteria_range1: Range | Cell[Range], criterion1: Any, criteria_range2: Optional[Range | Cell[Range]], *, criterion2: Optional[Any]):
    '''Returns the average of a range depending on multiple criteria.'''

def BETA_DIST(value: Any, alpha: Any, beta: Any, cumulative: bool | Cell[bool], lower_bound: Any, upper_bound: Any):
    '''Returns the probability of a given value as defined by the beta distribution function.'''

def BETA_INV(probability: PercentFloat | Cell[PercentFloat], alpha: Any, beta: Any, lower_bound: Any, upper_bound: Any):
    '''Returns the value of the inverse beta distribution function for a given probability.'''

def BETADIST(value: Any, alpha: Any, beta: Any, lower_bound: Any, upper_bound: Any):
    '''See BETA.DIST'''

def BETAINV(probability: PercentFloat | Cell[PercentFloat], alpha: Any, beta: Any, lower_bound: Any, upper_bound: Any):
    '''See BETA.INV'''

def BINOM_DIST(num_successes: int | Cell[int], num_trials: int | Cell[int], prob_success: Any, cumulative: bool | Cell[bool]):
    '''See BINOMDIST'''

def BINOM_INV(num_trials: int | Cell[int], prob_success: Any, target_prob: Any):
    '''See CRITBINOM'''

def BINOMDIST(num_successes: int | Cell[int], num_trials: int | Cell[int], prob_success: Any, cumulative: bool | Cell[bool]):
    '''Calculates the probability of drawing a certain number of successes (or a maximum number of successes) in a certain number of tries given a population of a certain size containing a certain number of successes, with replacement of draws.'''

def CHIDIST(x: float | Cell[float], degrees_freedom: float | Cell[float]):
    '''Calculates the right-tailed chi-squared distribution, often used in hypothesis testing.'''

def CHIINV(probability: PercentFloat | Cell[PercentFloat], degrees_freedom: float | Cell[float]):
    '''Calculates the inverse of the right-tailed chi-squared distribution.'''

def CHISQ_DIST(x: float | Cell[float], degrees_freedom: float | Cell[float], cumulative: bool | Cell[bool]):
    '''Calculates the left-tailed chi-squared distribution, often used in hypothesis testing.'''

def CHISQ_DIST_RT(x: float | Cell[float], degrees_freedom: float | Cell[float]):
    '''Calculates the right-tailed chi-squared distribution, which is commonly used in hypothesis testing.'''

def CHISQ_INV(probability: PercentFloat | Cell[PercentFloat], degrees_freedom: float | Cell[float]):
    '''Calculates the inverse of the left-tailed chi-squared distribution.'''

def CHISQ_INV_RT(probability: PercentFloat | Cell[PercentFloat], degrees_freedom: float | Cell[float]):
    '''Calculates the inverse of the right-tailed chi-squared distribution.'''

def CHISQ_TEST(observed_range: Range | Cell[Range], expected_range: Range | Cell[Range]):
    '''See CHITEST'''

def CHITEST(observed_range: Range | Cell[Range], expected_range: Range | Cell[Range]):
    '''Returns the probability associated with a Pearson’s chi-squared test on the two ranges of data. Determines the likelihood that the observed categorical data is drawn from an expected distribution.'''

def CONFIDENCE(alpha: Any, standard_deviation: PercentFloat | Cell[PercentFloat], pop_size: Any):
    '''See CONFIDENCE.NORM'''

def CONFIDENCE_NORM(alpha: Any, standard_deviation: PercentFloat | Cell[PercentFloat], pop_size: Any):
    '''Calculates the width of half the confidence interval for a normal distribution.'''

def CONFIDENCE_T(alpha: Any, standard_deviation: PercentFloat | Cell[PercentFloat], size: Any):
    '''Calculates the width of half the confidence interval for a Student’s t-distribution.'''

def CORREL(data_y: Range | Cell[Range], data_x: Range | Cell[Range]):
    '''Calculates r, the Pearson product-moment correlation coefficient of a dataset.'''

def COUNT(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]) -> float:
    '''Returns a count of the number of numeric values in a dataset.'''

def COUNTA(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]) -> float:
    '''Returns a count of the number of values in a dataset.'''

def COVAR(data_y: Range | Cell[Range], data_x: Range | Cell[Range]):
    '''Calculates the covariance of a dataset.'''

def COVARIANCE_P(data_y: Range | Cell[Range], data_x: Range | Cell[Range]):
    '''See COVAR'''

def COVARIANCE_S(data_y: Range | Cell[Range], data_x: Range | Cell[Range]):
    '''Calculates the covariance of a dataset, where the dataset is a sample of the total population.'''

def CRITBINOM(num_trials: int | Cell[int], prob_success: Any, target_prob: Any):
    '''Calculates the smallest value for which the cumulative binomial distribution is greater than or equal to a specified criteria.'''

def DEVSQ(value1: float | Cell[float], value2: float | Cell[float]):
    '''Calculates the sum of squares of deviations based on a sample.'''

def EXPON_DIST(x: float | Cell[float], LAMBDA: Any, cumulative: bool | Cell[bool]):
    '''Returns the value of the exponential distribution function with a specified LAMBDA at a specified value.'''

def EXPONDIST(x: float | Cell[float], LAMBDA: Any, cumulative: bool | Cell[bool]):
    '''See EXPON.DIST'''

def F_DIST(x: float | Cell[float], degrees_freedom1: float | Cell[float], degrees_freedom2: float | Cell[float], cumulative: bool | Cell[bool]):
    '''Calculates the left-tailed F probability distribution (degree of diversity) for two data sets with given input x. Alternately called Fisher-Snedecor distribution or Snedecor's F distribution.'''

def F_DIST_RT(x: float | Cell[float], degrees_freedom1: float | Cell[float], degrees_freedom2: float | Cell[float]):
    '''Calculates the right-tailed F probability distribution (degree of diversity) for two data sets with given input x. Alternately called Fisher-Snedecor distribution or Snedecor's F distribution.'''

def F_INV(probability: PercentFloat | Cell[PercentFloat], degrees_freedom1: float | Cell[float], degrees_freedom2: float | Cell[float]):
    '''Calculates the inverse of the left-tailed F probability distribution. Also called the Fisher-Snedecor distribution or Snedecor’s F distribution.'''

def F_INV_RT(probability: PercentFloat | Cell[PercentFloat], degrees_freedom1: float | Cell[float], degrees_freedom2: float | Cell[float]):
    '''Calculates the inverse of the right-tailed F probability distribution. Also called the Fisher-Snedecor distribution or Snedecor’s F distribution.'''

def F_TEST(range1: Range | Cell[Range], range2: Range | Cell[Range]):
    '''See FTEST'''

def FDIST(x: float | Cell[float], degrees_freedom1: float | Cell[float], degrees_freedom2: float | Cell[float]):
    '''See F.DIST.RT'''

def FINV(probability: PercentFloat | Cell[PercentFloat], degrees_freedom1: float | Cell[float], degrees_freedom2: float | Cell[float]):
    '''See F.INV.RT'''

def FISHER(value: Any):
    '''Returns the Fisher transformation of a specified value.'''

def FISHERINV(value: Any):
    '''Returns the inverse Fisher transformation of a specified value.'''

def FORECAST(x: float | Cell[float], data_y: Range | Cell[Range], data_x: Range | Cell[Range]):
    '''Calculates the expected y-value for a specified x based on a linear regression of a dataset.'''

def FORECAST_LINEAR(x: float | Cell[float], data_y: Range | Cell[Range], data_x: Range | Cell[Range]):
    '''See FORECAST'''

def FTEST(range1: Range | Cell[Range], range2: Range | Cell[Range]):
    '''Returns the probability associated with an F-test for equality of variances. Determines whether two samples are likely to have come from populations with the same variance.'''

def GAMMA(number: int | Cell[int]):
    '''Returns the Gamma function evaluated at the specified value.'''

def GAMMA_DIST(x: float | Cell[float], alpha: Any, beta: Any, cumulative: bool | Cell[bool]):
    '''Calculates the gamma distribution, a two-parameter continuous probability distribution.'''

def GAMMA_INV(probability: PercentFloat | Cell[PercentFloat], alpha: Any, beta: Any):
    '''The GAMMA.INV function returns the value of the inverse gamma cumulative distribution function for the specified probability and alpha and beta parameters.'''

def GAMMADIST(x: float | Cell[float], alpha: Any, beta: Any, cumulative: bool | Cell[bool]):
    '''See GAMMA.DIST'''

def GAMMAINV(probability: PercentFloat | Cell[PercentFloat], alpha: Any, beta: Any):
    '''See GAMMA.INV'''

def GAUSS(z: Any):
    '''The GAUSS function returns the probability that a random variable, drawn from a normal distribution, will be between the mean and z standard deviations above (or below) the mean.'''

def GEOMEAN(value1: float | Cell[float], value2: float | Cell[float]):
    '''Calculates the geometric mean of a dataset.'''

def HARMEAN(value1: float | Cell[float], value2: float | Cell[float]):
    '''Calculates the harmonic mean of a dataset.'''

def HYPGEOM_DIST(num_successes: int | Cell[int], num_draws: int | Cell[int], successes_in_pop: Any, pop_size: Any):
    '''See HYPGEOMDIST'''

def HYPGEOMDIST(num_successes: int | Cell[int], num_draws: int | Cell[int], successes_in_pop: Any, pop_size: Any):
    '''Calculates the probability of drawing a certain number of successes in a certain number of tries given a population of a certain size containing a certain number of successes, without replacement of draws.'''

def INTERCEPT(data_y: Range | Cell[Range], data_x: Range | Cell[Range]):
    '''Calculates the y-value at which the line resulting from linear regression of a dataset will intersect the y-axis (x=0).'''

def KURT(value1: float | Cell[float], value2: float | Cell[float]):
    '''Calculates the kurtosis of a dataset, which describes the shape, and in particular the "peakedness" of that dataset.'''

def LARGE(data: Any, n: int | Cell[int]):
    '''Returns the nth largest element from a data set, where n is user-defined.'''

def LOGINV(x: float | Cell[float], mean: float | Cell[float], standard_deviation: PercentFloat | Cell[PercentFloat]):
    '''Returns the value of the inverse log-normal cumulative distribution with given mean and standard deviation at a specified value.'''

def LOGNORM_DIST(x: float | Cell[float], mean: float | Cell[float], standard_deviation: PercentFloat | Cell[PercentFloat]):
    '''See LOGNORMDIST'''

def LOGNORM_INV(x: float | Cell[float], mean: float | Cell[float], standard_deviation: PercentFloat | Cell[PercentFloat]):
    '''See LOGINV'''

def LOGNORMDIST(x: float | Cell[float], mean: float | Cell[float], standard_deviation: PercentFloat | Cell[PercentFloat]):
    '''Returns the value of the log-normal cumulative distribution with given mean and standard deviation at a specified value.'''

def MARGINOFERROR(range: Range | Cell[Range], confidence: PercentFloat | Cell[PercentFloat]):
    '''Calculates the amount of random sampling error given a range of values and a confidence level.'''

def MAX(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]):
    '''Returns the maximum value in a numeric dataset.'''

def MAXA(value1: float | Cell[float], value2: float | Cell[float]):
    '''Returns the maximum numeric value in a dataset.'''

def MAXIFS(range: Range | Cell[Range], criteria_range1: Range | Cell[Range], criterion1: Any, criteria_range2: Optional[Range | Cell[Range]], *, criterion2: Optional[Any]):
    '''Returns the maximum value in a range of cells, filtered by a set of criteria.'''

def MEDIAN(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]):
    '''Returns the median value in a numeric dataset.'''

def MIN(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]):
    '''Returns the minimum value in a numeric dataset.'''

def MINA(value1: float | Cell[float], value2: float | Cell[float]):
    '''Returns the minimum numeric value in a dataset.'''

def MINIFS(range: Range | Cell[Range], criteria_range1: Range | Cell[Range], criterion1: Any, criteria_range2: Optional[Range | Cell[Range]], *, criterion2: Optional[Any]):
    '''Returns the minimum value in a range of cells, filtered by a set of criteria.'''

def MODE(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]):
    '''Returns the most commonly occurring value in a dataset.'''

def MODE_MULT(value1: float | Cell[float], value2: float | Cell[float]):
    '''Returns the most commonly occurring values in a dataset.'''

def MODE_SNGL(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]):
    '''See MODE'''

def NEGBINOM_DIST(num_failures: int | Cell[int], num_successes: int | Cell[int], prob_success: Any):
    '''See NEGBINOMDIST'''

def NEGBINOMDIST(num_failures: int | Cell[int], num_successes: int | Cell[int], prob_success: Any):
    '''Calculates the probability of drawing a certain number of failures before a certain number of successes given a probability of success in independent trials.'''

def NORM_DIST(x: float | Cell[float], mean: float | Cell[float], standard_deviation: PercentFloat | Cell[PercentFloat], cumulative: bool | Cell[bool]) -> float:
    '''See NORMDIST'''

def NORM_INV(x: float | Cell[float], mean: float | Cell[float], standard_deviation: PercentFloat | Cell[PercentFloat]) -> float:
    '''See NORMINV'''

def NORM_S_DIST(x: float | Cell[float]) -> float:
    '''See NORMSDIST'''

def NORM_S_INV(x: float | Cell[float]) -> float:
    '''See NORMSINV'''

def NORMDIST(x: float | Cell[float], mean: float | Cell[float], standard_deviation: PercentFloat | Cell[PercentFloat], cumulative: bool | Cell[bool]) -> float:
    '''Returns the value of the normal distribution function (or normal cumulative distribution function) for a specified value, mean, and standard deviation.'''

def NORMINV(x: float | Cell[float], mean: float | Cell[float], standard_deviation: PercentFloat | Cell[PercentFloat]) -> float:
    '''Returns the value of the inverse normal distribution function for a specified value, mean, and standard deviation.'''

def NORMSDIST(x: float | Cell[float]) -> float:
    '''Returns the value of the standard normal cumulative distribution function for a specified value.'''

def NORMSINV(x: float | Cell[float]) -> float:
    '''Returns the value of the inverse standard normal distribution function for a specified value.'''

def PEARSON(data_y: Range | Cell[Range], data_x: Range | Cell[Range]):
    '''Calculates r, the Pearson product-moment correlation coefficient of a dataset.'''

def PERCENTILE(data: Any, percentile: PercentFloat | Cell[PercentFloat]):
    '''Returns the value at a given percentile of a dataset.'''

def PERCENTILE_EXC(data: Any, percentile: PercentFloat | Cell[PercentFloat]):
    '''Returns the value at a given percentile of a dataset, exclusive of 0 and 1.'''

def PERCENTILE_INC(data: Any, percentile: PercentFloat | Cell[PercentFloat]):
    '''See PERCENTILE'''

def PERCENTRANK(data: Any, value: Any, significant_digits: Optional[int | Cell[int]]):
    '''Returns the percentage rank (percentile) of a specified value in a dataset.'''

def PERCENTRANK_EXC(data: Any, value: Any, significant_digits: Optional[int | Cell[int]]):
    '''Returns the percentage rank (percentile) from 0 to 1 exclusive of a specified value in a dataset.'''

def PERCENTRANK_INC(data: Any, value: Any, significant_digits: Optional[int | Cell[int]]):
    '''Returns the percentage rank (percentile) from 0 to 1 inclusive of a specified value in a dataset.'''

def PERMUTATIONA(number: int | Cell[int], number_chosen: int | Cell[int]) -> float:
    '''Returns the number of permutations for selecting a group of objects (with replacement) from a total number of objects.'''

def PERMUT(n: int | Cell[int], k: Any) -> float:
    '''Returns the number of ways to choose some number of objects from a pool of a given size of objects, considering order.'''

def PHI(x: float | Cell[float]):
    '''The PHI function returns the value of the normal distribution with mean 0 and standard deviation 1.'''

def POISSON(x: float | Cell[float], mean: float | Cell[float], cumulative: bool | Cell[bool]):
    '''See POISSON.DIST'''

def POISSON_DIST(x: float | Cell[float], mean: float | Cell[float], cumulative: Optional[bool | Cell[bool]]):
    '''Returns the value of the Poisson distribution function (or Poisson cumulative distribution function) for a specified value and mean.'''

def PROB(data: Any, probabilities: Any, low_limit: Any, high_limit: Optional[Any]):
    '''Given a set of values and corresponding probabilities, calculates the probability that a value chosen at random falls between two limits.'''

def QUARTILE(data: Any, quartile_number: int | Cell[int]):
    '''Returns a value nearest to a specified quartile of a dataset.'''

def QUARTILE_EXC(data: Any, quartile_number: int | Cell[int]):
    '''Returns value nearest to a given quartile of a dataset, exclusive of 0 and 4.'''

def QUARTILE_INC(data: Any, quartile_number: int | Cell[int]):
    '''See QUARTILE'''

def RANK(value: Any, data: Any, is_ascending: Optional[Any]):
    '''Returns the rank of a specified value in a dataset.'''

def RANK_AVG(value: Any, data: Any, is_ascending: Optional[Any]):
    '''Returns the rank of a specified value in a dataset. If there is more than one entry of the same value in the dataset, the average rank of the entries will be returned.'''

def RANK_EQ(value: Any, data: Any, is_ascending: Optional[Any]):
    '''Returns the rank of a specified value in a dataset. If there is more than one entry of the same value in the dataset, the top rank of the entries will be returned.'''

def RSQ(data_y: Range | Cell[Range], data_x: Range | Cell[Range]):
    '''Calculates the square of r, the Pearson product-moment correlation coefficient of a dataset.'''

def SKEW(value1: float | Cell[float], value2: float | Cell[float]):
    '''Calculates the skewness of a dataset, which describes the symmetry of that dataset about the mean.'''

def SKEW_P(value1: float | Cell[float], value2: float | Cell[float]):
    '''Calculates the skewness of a dataset that represents the entire population.'''

def SLOPE(data_y: Range | Cell[Range], data_x: Range | Cell[Range]):
    '''Calculates the slope of the line resulting from linear regression of a dataset.'''

def SMALL(data: Any, n: int | Cell[int]):
    '''Returns the nth smallest element from a data set, where n is user-defined.'''

def STANDARDIZE(value: Any, mean: float | Cell[float], standard_deviation: PercentFloat | Cell[PercentFloat]):
    '''Calculates the normalized equivalent of a random variable given mean and standard deviation of the distribution.'''

def STDEV(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]):
    '''Calculates the standard deviation based on a sample.'''

def STDEV_P(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]):
    '''See STDEVP'''

def STDEV_S(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]):
    '''See STDEV'''

def STDEVA(value1: float | Cell[float], value2: float | Cell[float]):
    '''Calculates the standard deviation based on a sample, setting text to the value `0`.'''

def STDEVP(value1: float | Cell[float], value2: float | Cell[float]):
    '''Calculates the standard deviation based on an entire population.'''

def STDEVPA(value1: float | Cell[float], value2: float | Cell[float]):
    '''Calculates the standard deviation based on an entire population, setting text to the value `0`.'''

def STEYX(data_y: Range | Cell[Range], data_x: Range | Cell[Range]):
    '''Calculates the standard error of the predicted y-value for each x in the regression of a dataset.'''

def T_DIST(x: float | Cell[float], degrees_freedom: float | Cell[float], cumulative: bool | Cell[bool]):
    '''Returns the right tailed Student distribution for a value x.'''

def T_DIST_2T(x: float | Cell[float], degrees_freedom: float | Cell[float]):
    '''Returns the two tailed Student distribution for a value x.'''

def T_DIST_RT(x: float | Cell[float], degrees_freedom: float | Cell[float]):
    '''Returns the right tailed Student distribution for a value x.'''

def T_INV(probability: PercentFloat | Cell[PercentFloat], degrees_freedom: float | Cell[float]):
    '''Calculates the negative inverse of the one-tailed TDIST function.'''

def T_INV_2T(probability: PercentFloat | Cell[PercentFloat], degrees_freedom: float | Cell[float]):
    '''Calculates the inverse of the two-tailed TDIST function.'''

def T_TEST(range1: Range | Cell[Range], range2: Range | Cell[Range], tails: Any, type: Any):
    '''Returns the probability associated with Student's t-test. Determines whether two samples are likely to have come from the same two underlying populations that have the same mean.'''

def TDIST(x: float | Cell[float], degrees_freedom: float | Cell[float], tails: Any):
    '''Calculates the probability for Student's t-distribution with a given input (x).'''

def TINV(probability: PercentFloat | Cell[PercentFloat], degrees_freedom: float | Cell[float]):
    '''See T.INV.2T'''

def TRIMMEAN(data: Any, exclude_proportion: Any):
    '''Calculates the mean of a dataset excluding some proportion of data from the high and low ends of the dataset.'''

def TTEST(range1: Range | Cell[Range], range2: Range | Cell[Range], tails: Any, type: Any):
    '''See T.TEST'''

def VAR(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]):
    '''Calculates the variance based on a sample.'''

def VAR_P(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]):
    '''See VARP'''

def VAR_S(value1: float | Cell[float], *, value2: Optional[float | Cell[float]]):
    '''See VAR'''

def VARA(value1: float | Cell[float], value2: float | Cell[float]):
    '''Calculates an estimate of variance based on a sample, setting text to the value `0`.'''

def VARP(value1: float | Cell[float], value2: float | Cell[float]):
    '''Calculates the variance based on an entire population.'''

def VARPA(value1: float | Cell[float], *, value2: float | Cell[float]):
    '''Calculates the variance based on an entire population, setting text to the value `0`.'''

def WEIBULL(x: float | Cell[float], shape: Any, scale: Any, cumulative: bool | Cell[bool]):
    '''Returns the value of the Weibull distribution function (or Weibull cumulative distribution function) for a specified shape and scale.'''

def WEIBULL_DIST(x: float | Cell[float], shape: Any, scale: Any, cumulative: bool | Cell[bool]):
    '''See WEIBU'''

def Z_TEST(data: Any, value: Any, standard_deviation: Optional[PercentFloat | Cell[PercentFloat]]):
    '''Returns the one-tailed P-value of a Z-test with standard distribution.'''

def ZTEST(data: Any, value: Any, standard_deviation: Optional[PercentFloat | Cell[PercentFloat]]):
    '''See Z.TEST'''

def ARABIC(roman_numeral: int | Cell[int]) -> str:
    '''Computes the value of a Roman numeral.'''

def ASC(text: str | Cell[str]) -> str:
    '''Converts full-width ASCII and katakana characters to their half-width counterparts. All standard-width characters will remain unchanged.'''

def CHAR(table_number: int | Cell[int]) -> str:
    '''Convert a number into a character according to the current Unicode table.'''

def CLEAN(text: str | Cell[str]) -> str:
    '''Returns the text with the non-printable ASCII characters removed.'''

def CODE(string: str | Cell[str]) -> int:
    '''Returns the numeric Unicode map value of the first character in the string provided.'''

def CONCATENATE(string1: Any, *, string2: Optional[Any]) -> str:
    '''Appends strings to one another.'''

def DOLLAR(number: int | Cell[int], number_of_places: Optional[int | Cell[int]]) -> str:
    '''Formats a number into the locale-specific currency format.'''

def EXACT(string1: Any, string2: Any) -> bool:
    '''Tests whether two strings are identical.'''

def FIND(search_for: Any, text_to_search: str | Cell[str], starting_at: Optional[Any]) -> int:
    '''Returns the position at which a string is first found within text.'''

def FINDB(search_for: Any, text_to_search: str | Cell[str], starting_at: Optional[Any]) -> int:
    '''Returns the position at which a string is first found within text counting each double-character as 2.'''

def FIXED(number: int | Cell[int], number_of_places: Optional[int | Cell[int]], suppress_separator: Optional[Any]) -> str:
    '''Formats a number with a fixed number of decimal places.'''

def JOIN(delimiter: Any, value_OR_array1: Array | Any | Cell[Array | Any], *, value_OR_array2: Optional[Array | Any | Cell[Array | Any]]) -> str:
    '''Concatenates the elements of one or more one-dimensional arrays using a specified delimiter.'''

def LEFT(string: str | Cell[str], number_of_characters: Optional[int | Cell[int]]) -> str:
    '''Returns a substring from the beginning of a specified string.'''

def LEFTB(string: str | Cell[str], num_of_bytes: int | Cell[int]) -> float:
    '''Returns the left portion of a string up to a certain number of bytes.'''

def LEN(text: str | Cell[str]) -> int:
    '''Returns the length of a string.'''

def LENB(string: str | Cell[str]) -> int:
    '''Returns the length of a string in bytes."'''

def LOWER(text: str | Cell[str]) -> str:
    '''Converts a specified string to lowercase.'''

def MID(string: str | Cell[str], starting_at: Any, extract_length: int | Cell[int]) -> str:
    '''Returns a segment of a string.'''

def MIDB(string: str | Cell[str], starting_at: Any, extract_length_bytes: int | Cell[int]) -> str:
    '''Returns a section of a string starting at a given character and up to a specified number of bytes.'''

def PROPER(text_to_capitalize: str | Cell[str]) -> str:
    '''Capitalizes each word in a specified string.'''

def REGEXEXTRACT(text: str | Cell[str], regular_expression: Any) -> str:
    '''Extracts matching substrings according to a regular expression.'''

def REGEXMATCH(text: str | Cell[str], regular_expression: Any) -> bool:
    '''Whether a piece of text matches a regular expression.'''

def REGEXREPLACE(text: str | Cell[str], regular_expression: Any, replacement: Any) -> str:
    '''Replaces part of a text string with a different text string using regular expressions.'''

def REPLACE(text: str | Cell[str], position: Any, length: int | Cell[int], new_text: str | Cell[str]) -> str:
    '''Replaces part of a text string with a different text string.'''

def REPLACEB(text: str | Cell[str], position: Any, num_bytes: int | Cell[int], new_text: str | Cell[str]) -> str:
    '''Replaces part of a text string, based on a number of bytes, with a different text string.'''

def REPT(text_to_repeat: str | Cell[str], number_of_repetitions: int | Cell[int]) -> float:
    '''Returns specified text repeated a number of times.'''

def RIGHT(string: str | Cell[str], number_of_characters: Optional[int | Cell[int]]) -> str:
    '''Returns a substring from the end of a specified string.'''

def RIGHTB(string: str | Cell[str], num_of_bytes: int | Cell[int]) -> float:
    '''Returns the right portion of a string up to a certain number of bytes.'''

def ROMAN(number: int | Cell[int], rule_relaxation: Optional[Any]) -> str:
    '''Formats a number in Roman numerals.'''

def SEARCH(search_for: Any, text_to_search: str | Cell[str], starting_at: Optional[Any]) -> int:
    '''Returns the position at which a string is first found within text.'''

def SEARCHB(search_for: Any, text_to_search: str | Cell[str], starting_at: Optional[Any]) -> int:
    '''Returns the position at which a string is first found within text counting each double-character as 2.'''

def SPLIT(text: str | Cell[str], delimiter: Any, split_by_each: Optional[Any], remove_empty_text: Optional[str | Cell[str]]) -> str:
    '''Divides text around a specified character or string, and puts each fragment into a separate cell in the row.'''

def SUBSTITUTE(text_to_search: str | Cell[str], search_for: Any, replace_with: Any, occurrence_number: Optional[int | Cell[int]]) -> str:
    '''Replaces existing text with new text in a string.'''

def T(value: Any) -> str:
    '''Returns string arguments as text.'''

def TEXT(number: int | Cell[int], format: Any) -> str:
    '''Converts a number into text according to a specified format.'''

def TEXTJOIN(delimiter: Any, ignore_empty: Any, text1: str | Cell[str], *, text2: Optional[str | Cell[str]]) -> str:
    '''Combines the text from multiple strings and/or arrays, with a specifiable delimiter separating the different texts.'''

def TRIM(text: str | Cell[str]) -> str:
    '''Removes leading and trailing spaces in a specified string.'''

def UNICHAR(number: int | Cell[int]) -> int:
    '''Returns the Unicode character for a number.'''

def UNICODE(text: str | Cell[str]) -> int:
    '''Returns the decimal Unicode value of the first character of the text.'''

def UPPER(text: str | Cell[str]) -> str:
    '''Converts a specified string to uppercase.'''

def VALUE(text: str | Cell[str]) -> float:
    '''Converts a string in any of the date, time or number formats that Google Sheets understands into a number.'''

def ENCODEURL(text: str | Cell[str]) -> URL:
    '''Encodes a string of text for the purpose of using in a URL query.'''

def HYPERLINK(url: URL | Cell[URL], link_label: Optional[Any]) -> URL:
    '''Creates a hyperlink inside a cell.'''

def IMPORTDATA(url: URL | Cell[URL]):
    '''Imports data at a given url in .csv (comma-separated value) or .tsv (tab-separated value) format.'''

def IMPORTFEED(url: URL | Cell[URL], query: Optional[Any], headers: Optional[Any], num_items: Optional[int | Cell[int]]):
    '''Imports a RSS or ATOM feed.'''

def IMPORTHTML(url: URL | Cell[URL], query: Any, index: Any):
    '''Imports data from a table or list within an HTML page.'''

def IMPORTRANGE(spreadsheet_url: URL | Cell[URL], range_string: Range | Cell[Range]):
    '''Imports a range of cells from a specified spreadsheet.'''

def IMPORTXML(url: URL | Cell[URL], xpath_query: Any):
    '''Imports data from any of various structured data types including XML, HTML, CSV, TSV, and RSS and ATOM XML feeds.'''

def ISURL(value: Any) -> bool:
    '''Checks whether a value is a valid URL.'''