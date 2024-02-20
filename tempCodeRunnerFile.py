new_features = pd.DataFrame({
    'current_size': [5.5],
    'assessment_hectares': [0.01],
    'fire_spread_rate': [3],
    'temperature': [28.8],
    'relative_humidity': [37],
    'wind_speed': [11],
    'uc_hectares': [10]
})

mu.use_model(model, new_features)
