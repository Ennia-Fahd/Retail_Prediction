# Retail_Prediction

The objective of this project is to deeply analyze product sales data from a dataset and develop forecasts for each product regarding its sales for the coming year.

# Design the star diagram

The first step is to create a star schema to set up a data warehouse that will serve as the primary source of data.

![model_etoile4](https://github.com/Ennia-Fahd/Retail_Prediction/assets/92646945/9a39497e-2353-42f1-8664-b46765b57a10)

# Implement the Datawarehouse

<h2>During this phase we will establish our Data Warehouse using the SSIS ETL tool, which will allow us to simplify the process of cleaning, normalizing and manipulating data, in order to create tables according to our needs specific.</h2>

1-Dimension Customer:
![Customer](https://github.com/Ennia-Fahd/Retail_Prediction/assets/92646945/70483340-a971-4a22-81e1-6f4d067e196f)

2-Dimension Product:

![Product](https://github.com/Ennia-Fahd/Retail_Prediction/assets/92646945/00314544-d8c8-4f95-aac7-dcdfd7a8f0d4)

3-Dimension Region:
![Region](https://github.com/Ennia-Fahd/Retail_Prediction/assets/92646945/ec540a76-0ed9-43dc-9fad-a405d0b621df)

4-Dimension Supplier:
![Supplier](https://github.com/Ennia-Fahd/Retail_Prediction/assets/92646945/5289aeb9-d8ba-4249-af5e-8dd667ff4344)

5-Dimension Time:

![Time](https://github.com/Ennia-Fahd/Retail_Prediction/assets/92646945/aaa3f30f-fa54-442d-a81c-990c21294d8f)
![script_Temps](https://github.com/Ennia-Fahd/Retail_Prediction/assets/92646945/854fc026-5d0b-4713-b21f-ecfcfa254786)

We generated the time dimension using a script to create a set of dates between 2015 and 2025. This approach will allow us to create multiple time dimensions from Power BI in correspondence with our fact table.

5-Fact Demande:
![diagramme1](https://github.com/Ennia-Fahd/Retail_Prediction/assets/92646945/55e348d3-68b8-4b98-a0f3-7ead5a89c08d)
![factOrder1](https://github.com/Ennia-Fahd/Retail_Prediction/assets/92646945/8f1fd09d-6eb6-4fa9-889e-16a0dcbb0ec8)
![factOrder2](https://github.com/Ennia-Fahd/Retail_Prediction/assets/92646945/d50c1e19-e1fb-4ca4-bcbf-fbc5ea4c2faa)
![factOrder3](https://github.com/Ennia-Fahd/Retail_Prediction/assets/92646945/26bfc521-d6f1-450d-a87e-44a8b7919318)

# Visualization with Dashboard

![datawa_rehouse_Powerbi](https://github.com/Ennia-Fahd/Retail_Prediction/assets/92646945/6d653478-cf78-4b19-8ea1-ba5e30fde93e)
![dashboard1](https://github.com/Ennia-Fahd/Retail_Prediction/assets/92646945/39d49e8b-4b07-4eae-a6af-950a38c9aec2)
![dashboard2](https://github.com/Ennia-Fahd/Retail_Prediction/assets/92646945/9bbd8e3f-6b25-4115-99c7-1a44f83cab50)
![dahsboard3](https://github.com/Ennia-Fahd/Retail_Prediction/assets/92646945/b72afece-3dc1-4fc3-b2a3-20abf4d19627)

In this diagram, we have used a Python script to forecast demand by product as an indicator between 1 and 10, and it also shows the validity of this forecast in days. This forecast is carried out using the exponential smoothing algorithm, a detailed explanation of which can be found in the "Prediction_PowerBI" file. Once the code runs, it generates an Excel "product_prediction_BI.xls" file that we can import directly into Power BI and link to our data model.

![dashboard4](https://github.com/Ennia-Fahd/Retail_Prediction/assets/92646945/16bb0bed-2996-458f-a011-1ff3368e956c)

This diagram was created using the Python script editor built into Power BI, applying the exponential smoothing algorithm in the same way as in the previous code, following the same logic.This code is in the file "scirpt_shema_dashboard4_powerBI.txt".
