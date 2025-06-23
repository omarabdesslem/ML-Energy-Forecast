# Power Grid Load Forecasting using Machine Learning Approaches  
**Student:** Omar Abdesslem  
**Institution:** University of Geneva  
**Date:** June 2025  

## Overview  

This project explores statistical and machine learning techniques for medium-term energy load forecasting in the Swiss power grid. Using historical data from Swissgrid and weather forecasts from ECMWF, the study develops and compares models such as AR(1), ARIMA, SARIMA, and SARIMAX.  

The primary goal is to enhance forecasting accuracy and operational decision-making for grid stability by integrating seasonal patterns and external variables such as temperature.

## Key Features  

- **Data Sources**: Swissgrid operational energy data (2021–2025), ECMWF SEAS5 temperature forecasts  
- **Forecasting Horizon**: 8 weeks ahead, weekly granularity  
- **Models Used**:  
  - AR(1) — baseline
  - ARIMA(1,0,1)  
  - ARIMA(1,1,0)  
  - SARIMA(1,0,0)(1,0,0,52)  
  - SARIMAX(1,0,0)(1,0,0,52) with exogenous temperature covariates  
- **Evaluation Metric**: MAPE (Mean Absolute Percentage Error)  
- **Best Performing Model**: SARIMAX with a MAPE of 4.83%  
- **Residual Diagnostics**: KS test confirmed SARIMAX residuals were closest to white noise (KS statistic: 10.47%)

## Conclusion  

SARIMAX with temperature covariates provided the most accurate forecasts and exhibited the cleanest residuals among all tested models. This highlights the importance of integrating exogenous factors in energy forecasting. The approach offers a practical and interpretable solution for improving energy system stability in Switzerland.

## Future Work  

- Extend to additional exogenous variables (humidity, holidays)  
- Implement real-time adaptive models  
- Explore probabilistic forecasting methods  
