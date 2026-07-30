--check loading result

-- select *
-- from daily_sales
-- limit 5;

--first, let's define weekdays
create view daily_sales_with_weekday as
select *,
CASE
    WHEN strftime('%w',"Date") = '0' THEN 'Sunday'
    WHEN strftime('%w',"Date") = '1' THEN 'Monday'
    WHEN strftime('%w',"Date") = '2' THEN 'Tuesday'
    WHEN strftime('%w',"Date") = '3' THEN 'Wednesday'
    WHEN strftime('%w',"Date") = '4' THEN 'Thursday'
    WHEN strftime('%w',"Date") = '5' THEN 'Friday'
    WHEN strftime('%w',"Date") = '6' THEN 'Saturday'
end as weekday
from daily_sales;

--=========================
--KPI Summary
--=========================

--total sales summary
select
sum("Gross Sales") as total_gross_sales,
sum("Net Sales") as total_net_sales,
sum("Closed Orders") as total_orders
from daily_sales;

--now I want to see how much does a order typically cost, 
--so I will calculate the average order value
select sum("Net Sales") / sum("Closed Orders") as average_order_value
from daily_sales;
--this shows the avg of the entire data set

--=========================
--Graphs
--=========================

--I want to see the trend of total $/month for each month 
select
strftime('%Y-%m', "Date") as month,
sum("Net Sales") as monthly_sales
from daily_sales
group by month
order by month;

--I want to see the trend of total $/day for each weekday 
select weekday,
sum("Net Sales") as total_sales,
sum("Closed Orders") as total_orders
from daily_sales_with_weekday
group by weekday
order by weekday;

--I want to see the daily avg $/order through the year 
select "Date", "Net Sales" / "Closed Orders" as daily_average_order_value
from daily_sales
--the goal here is to see the trend of the avg order in a given day throughout the year
order by "Date" asc;

--=========================
--Best and Worst Sales Days
--=========================

--best sales days
select "Date", "Net Sales"
from daily_sales
order by "Net Sales" desc
limit 5;

--similarly, worst sales days
select "Date", "Net Sales"
from daily_sales
order by "Net Sales" asc
limit 5;