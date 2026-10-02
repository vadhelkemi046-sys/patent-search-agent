import pandas as pd

data = {
    "id": ["P1", "P2", "P3", "P4", "P5"],
    "title": [
        "Smart water bottle with hydration tracking",
        "Machine learning based heart disease detection",
        "Solar powered portable phone charger",
        "Voice controlled home automation system",
        "Drone based crop monitoring system",
    ],
    "abstract": [
        "A bottle with sensors that tracks water intake and sends data to a mobile app.",
        "A system using machine learning on ECG signals to predict heart disease risk.",
        "A portable charger with foldable solar panels for charging mobile devices.",
        "A system that controls lights and appliances using voice commands and IoT sensors.",
        "A drone with cameras and AI models to detect crop diseases in farms.",
    ],
}

pd.DataFrame(data).to_csv("data/patents.csv", index=False)
print("patents.csv ban gayi")