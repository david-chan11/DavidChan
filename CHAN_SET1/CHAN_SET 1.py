#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def savings(gross_pay, tax_rate, expenses):

    money = int((gross_pay*(1-tax_rate)) - (expenses))
    return int(money)
savings(1000,0.1,100)


# In[ ]:


def material_waste(total_material, material_units, num_jobs, job_consumption):
    
    waste = total_material - (num_jobs * job_consumption)
    return str(waste) + material_units
    
material_waste(1000, "kg", 5, 10)


# In[ ]:


def interest(principal, rate, periods):
    
    money = (principal * (rate*periods)) + principal
    return(int(money))

interest(1000,0.03, 10)

