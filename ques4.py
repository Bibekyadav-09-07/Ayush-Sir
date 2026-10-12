
from tqdm import tqdm
import time

# Display progress for 20 tasks
for task in tqdm(range(20), desc="Studying Python"):
    time.sleep(0.1)

# Display completion message
print("\n✅ All 20 study tasks completed!")
print("🎉 Great job! Keep learning Python.")
