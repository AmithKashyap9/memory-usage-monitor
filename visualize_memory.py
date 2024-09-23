import pandas as pd
import matplotlib.pyplot as plt

def plot_memory_usage(log_file):
    df = pd.read_csv(log_file)
    
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    df['Used Memory (GB)'] = df['Used Memory (KB)'] / (1024 * 1024)
    df['Used Swap (GB)'] = df['Used Swap (KB)'] / (1024 * 1024)

    plt.figure(figsize=(12, 6))
    plt.plot(df['Timestamp'], df['Used Memory (GB)'], marker='o', linestyle='-', color='b', label='Used Memory (GB)')
    plt.plot(df['Timestamp'], df['Used Swap (GB)'], marker='x', linestyle='-', color='r', label='Used Swap (GB)')
    
    plt.title('Memory and Swap Usage Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Usage (GB)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()  
    plt.savefig('memory_usage_plot.png') 
    plt.show()

if __name__ == "__main__":
    log_file = 'memory_usage.log'
    plot_memory_usage(log_file)
